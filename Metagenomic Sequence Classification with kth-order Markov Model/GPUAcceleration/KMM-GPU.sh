#!/bin/bash
#PBS -S /bin/bash
#PBS -N KMM
#PBS -q gpuq                        #指定使用GPU
#PBS –l nodes=1:ppn=2
#PBS –W x=GRES:gpu@1
#PBS -o KMM.out                    
#PBS -e KMM.err              

source /home/apps/anaconda3/etc/profile.d/conda.sh
conda activate pytorch-gpu
# 执行Python脚本
python GPU.py

# 释放GPU资源
#nvidia-smi --gpu-reset -i 0
