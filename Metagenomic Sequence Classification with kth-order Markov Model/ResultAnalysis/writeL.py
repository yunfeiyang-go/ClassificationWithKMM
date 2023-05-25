import csv

# 将结果存入字典中
results = {
    3: {"Baumannia": 302, "Psychromonas": 94, "Sphingomonas": 125, "Roseiflexus": 270, "Hydrogenobaculum": 157,
        "Alteromonas": 313, "Denitrovibrio": 97, "Frankia": 98, "Candidatus": 167, "Corynebacterium": 168,
        "未知序列": 84},
    4: {"Baumannia": 522, "Psychromonas": 24, "Sphingomonas": 290, "Roseiflexus": 113, "Hydrogenobaculum": 391,
        "Alteromonas": 23, "Denitrovibrio": 46, "Frankia": 235, "Candidatus": 63, "Corynebacterium": 128,
        "未知序列": 40},
    5: {"Baumannia": 453, "Psychromonas": 16, "Sphingomonas": 396, "Roseiflexus": 101, "Hydrogenobaculum": 492,
        "Alteromonas": 18, "Denitrovibrio": 41, "Frankia": 194, "Candidatus": 53, "Corynebacterium": 85,
        "未知序列": 26},
    6: {"Baumannia": 436, "Psychromonas": 21, "Sphingomonas": 379, "Roseiflexus": 135, "Hydrogenobaculum": 490,
        "Alteromonas": 23, "Denitrovibrio": 50, "Frankia": 151, "Candidatus": 56, "Corynebacterium": 113,
        "未知序列": 21},
    7: {"Baumannia": 140, "Psychromonas": 8, "Sphingomonas": 244, "Roseiflexus": 122, "Hydrogenobaculum": 265,
        "Alteromonas": 3, "Denitrovibrio": 10, "Frankia": 121, "Candidatus": 54, "Corynebacterium": 113,
        "未知序列": 5},
    8: {"Baumannia": 539, "Psychromonas": 21, "Sphingomonas": 323, "Roseiflexus": 176, "Hydrogenobaculum": 368,
        "Alteromonas": 37, "Denitrovibrio": 54, "Frankia": 121, "Candidatus": 80, "Corynebacterium": 143,
        "未知序列": 13},
    9: {"Baumannia": 836, "Psychromonas": 2, "Sphingomonas": 281, "Roseiflexus": 184, "Hydrogenobaculum": 223,
        "Alteromonas": 11, "Denitrovibrio": 23, "Frankia": 103, "Candidatus": 50, "Corynebacterium": 160,
        "未知序列": 2}
}

# 将字典写入 CSV 文件
with open("L1_results.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    # 写入表头
    writer.writerow(["k", "Baumannia", "Psychromonas", "Sphingomonas", "Roseiflexus", "Hydrogenobaculum",
                     "Alteromonas", "Denitrovibrio", "Frankia", "Candidatus", "Corynebacterium", "未知序列"])
    # 写入每一行数据
    for k, row in results.items():
        writer.writerow([k] + list(row.values()))
