import csv

# 将结果存入字典中
results = {
    3: {"Baumannia": 457, "Psychromonas": 8, "Sphingomonas": 53, "Roseiflexus": 59, "Hydrogenobaculum": 134,
        "Alteromonas": 35, "Denitrovibrio": 36, "Frankia": 101, "Candidatus": 126, "Corynebacterium": 865,
        "未知序列": 1},
    4: {"Baumannia": 359, "Psychromonas": 9, "Sphingomonas": 61, "Roseiflexus": 76, "Hydrogenobaculum": 153,
        "Alteromonas": 55, "Denitrovibrio": 40, "Frankia": 136, "Candidatus": 183, "Corynebacterium": 800,
        "未知序列": 3},
    5: {"Baumannia": 323, "Psychromonas": 11, "Sphingomonas": 60, "Roseiflexus": 96, "Hydrogenobaculum": 166,
        "Alteromonas": 62, "Denitrovibrio": 43, "Frankia": 172, "Candidatus": 202, "Corynebacterium": 734,
        "未知序列": 6},
    6: {"Baumannia": 284, "Psychromonas": 15, "Sphingomonas": 50, "Roseiflexus": 120, "Hydrogenobaculum": 142,
        "Alteromonas": 76, "Denitrovibrio": 62, "Frankia": 173, "Candidatus": 230, "Corynebacterium": 717,
        "未知序列": 6},
    7: {"Baumannia": 261, "Psychromonas": 21, "Sphingomonas": 50, "Roseiflexus": 183, "Hydrogenobaculum": 130,
        "Alteromonas": 92, "Denitrovibrio": 81, "Frankia": 183, "Candidatus": 224, "Corynebacterium": 642,
        "未知序列": 8},
    8: {"Baumannia": 246, "Psychromonas": 23, "Sphingomonas": 48, "Roseiflexus": 204, "Hydrogenobaculum": 122,
        "Alteromonas": 107, "Denitrovibrio": 95, "Frankia": 185, "Candidatus": 221, "Corynebacterium": 617,
        "未知序列": 7},
    9: {"Baumannia": 219, "Psychromonas": 43, "Sphingomonas": 38, "Roseiflexus": 219, "Hydrogenobaculum": 140,
        "Alteromonas": 127, "Denitrovibrio": 123, "Frankia": 206, "Candidatus": 160, "Corynebacterium": 592,
        "未知序列": 8}
}

# 将字典写入 CSV 文件
with open("Pearson_results.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    # 写入表头
    writer.writerow(["k", "Baumannia", "Psychromonas", "Sphingomonas", "Roseiflexus", "Hydrogenobaculum",
                     "Alteromonas", "Denitrovibrio", "Frankia", "Candidatus", "Corynebacterium", "未知序列"])
    # 写入每一行数据
    for k, row in results.items():
        writer.writerow([k] + list(row.values()))
