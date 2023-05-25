import pandas as pd
import numpy as np

df = pd.read_csv('./Score_reads_Pearson_k=9.csv')

species_list = ['Baumannia', 'Psychromonas', 'Sphingomonas', 'Roseiflexus',
                'Hydrogenobaculum', 'Alteromonas', 'Denitrovibrio',
                'Frankia', 'Candidatus', 'Corynebacterium']

# 计算所有距离的中位数，作为阈值
threshold = np.median(df.values.flatten().astype(float))
#print(threshold)

# 初始化字典
counts = {}
for species in species_list:
    counts[species] = 0

# 找到最小距离
for i in range(len(df)):
    distances = df.iloc[i, :]
    min_distance_index = np.argmin(distances)
    if distances[min_distance_index] <= threshold:
        counts[species_list[min_distance_index]] += 1
    else:
        counts['未知序列'] = counts.get('未知序列', 0) + 1

# 输出结果
for species, count in counts.items():
    print('{}：{}'.format(species, count))
