#encoding:utf-8
import pandas as pd
import time
import os
import math
import numpy as np
import torch

def read_genome(file):      # 读取genome文件夹中文件，作为训练组
    name=[]
    seq_all=[]
    seq=""
    file=open(file,"r")
    for line in file:
        if line.startswith('>'):
            name.append(line[:-1].split('|')[4].split(' ')[1])
        elif line.startswith('A') or line.startswith('T') or line.startswith('G') or line.startswith('C'):
            seq+=line[:-1]
            continue
    seq_all.append(seq)
    file.close()
    return name,seq_all

def read_fa(file):         # 读取.fa文件: reads.fa,test.fa
    seq=[]
    num=[]
    file=open(file,"r")
    for line in file:
        if line.startswith('>'):
            num.append(line[1:-1])
        elif line.startswith('A') or line.startswith('T') or line.startswith('G') or line.startswith('C'):
            seq.append(line[:-1])
    file.close()
    return num,seq

def get_transmatrix(seq_all, k):
    trans = torch.zeros(4, 4**k).cuda() # 将numpy数据结构改为torch张量，放到GPU上进行后续计算
    dict = {'A': 0, 'T': 1, 'G': 2, 'C': 3}
    for i in range(len(seq_all)-k):
        tmp = seq_all[i:i+k+1]
        flag = True
        for j in range(k+1):
            if tmp[j] not in dict:
                flag = False
                break
        if not flag:
            continue
        id = 0
        for j in range(k):
            id += (4**(k-j-1))*dict[tmp[j]]
        trans[dict[tmp[k]]][id] += 1
    trans = trans / torch.sum(trans, dim=1, keepdim=True) # 使用torch求和函数
    return trans

def score(seq,trans,k):
    score=0
    dict={'A':0,'T':1,'G':2,'C':3}
    for i in range(0,len(seq)-k):
        tmp=seq[i:i+k+1]
        flag=True
        for j in range(k+1):
            if tmp[j] != "A" and tmp[j] != "T" and tmp[j] != "G" and tmp[j] != "C":
                flag=False
                break
            else:
                continue
        if flag == False:
            continue
        id = 0
        for j in range(k):
            id += (4**(k-j-1))*dict[tmp[j]]
        if trans[dict[tmp[k]]][id] == 0:
            score += 100000000
            break
        else:
            score += -math.log(trans[dict[tmp[k]]][id])
    return score

def kmarkov(seq,species_all,trans_all,k):
    all_score = []
    mi = score(seq,trans_all[0],k)
    all_score.append(k)
    all_score.append(mi)
    result = species_all[0]
    for i in range(len(species_all)):
        diff1 = score(seq,trans_all[i],k)
        diff2 = score(seq[::-1],trans_all[i],k)
        diff = min(diff1,diff2)
        all_score.append(diff)
        if diff < mi:
            mi = diff
            result=species_all[i]
    if mi >= 100000000:
        result = "unknown"
    return result,all_score

def tocsv(data,header,file_path):
    dataframe=pd.DataFrame(columns=header,data=data)
    dataframe.to_csv(file_path, index=False, encoding='utf-8')
    return dataframe

if __name__ == '__main__':

    species_dict = {"Baumannia":0,"Psychromonas":1,"Sphingomonas":2,"Roseiflexus":3,"Hydrogenobaculum":4,"Alteromonas":5,"Denitrovibrio":6,"Frankia":7,"Candidatus":8,"Corynebacterium":9}
    for k in range(3,10):
        species_count = np.zeros(10)
        species_all = []
        trans_all = []# 储存物种及其转移矩阵
        start_time = time.process_time()
        print("k=",k)
        for file in os.listdir("../DataSource/genomes"):
            print("正在读取文件: ", file)
            species = read_genome("../DataSource/genomes/"+file)[0][0]
            seq = read_genome("../DataSource/genomes/"+file)[1][0]
            trans = get_transmatrix(seq, k).cuda()
            species_all.append(species)
            trans_all.append(trans)
        name,test_seq = read_fa("../DataSource/test.fa")
        val = pd.read_csv("../DataSource/valid.csv")

        all_score=[]
        real = 0
        unknown = 0
        for i in range(len(name)):
            species_pre,all_score = kmarkov(test_seq[i],species_all,trans_all,k)
            if species_pre == "unknown":
                unknown += 1
            species_valid = val.iloc[i][1]
            if species_valid == species_pre:
                real += 1
                species_count[species_dict[species_pre]] += 1
            output_path = 'out.txt'
            with open(output_path, 'a', encoding='utf-8') as file1:
                print(all_score,file = file1)
        accuracy = real / len(name) * 100
        end_time = time.process_time()
        all_time = end_time - start_time
        print("当k=",k,"时:")
        print("准确率为: ",accuracy,"%。耗时: ",all_time,'s')
        print("未知物种数为: ",unknown)
        print("各种物种数为:")
        for i in range(10):
            print(species_all[i],": ",species_count[i])
