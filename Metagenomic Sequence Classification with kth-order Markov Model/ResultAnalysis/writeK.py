import csv

# 定义数据列表
data = [
    {'k': 3, '未知序列': 0, 'Baumannia': 274.0, 'Psychromonas': 109.0,
     'Sphingomonas': 100.0, 'Roseiflexus': 319.0, 'Hydrogenobaculum': 161.0,
     'Alteromonas': 234.0, 'Denitrovibrio': 177.0, 'Frankia': 91.0,
     'Candidatus': 219.0, 'Corynebacterium': 192.0},
    {'k': 4, '未知序列': 0, 'Baumannia': 273.0, 'Psychromonas': 113.0,
     'Sphingomonas': 92.0, 'Roseiflexus': 328.0, 'Hydrogenobaculum': 153.0,
     'Alteromonas': 235.0, 'Denitrovibrio': 179.0, 'Frankia': 90.0,
     'Candidatus': 222.0, 'Corynebacterium': 191.0},
    {'k': 5, '未知序列': 0, 'Baumannia': 280.0, 'Psychromonas': 106.0,
     'Sphingomonas': 89.0, 'Roseiflexus': 334.0, 'Hydrogenobaculum': 151.0,
     'Alteromonas': 244.0, 'Denitrovibrio': 174.0, 'Frankia': 90.0,
     'Candidatus': 225.0, 'Corynebacterium': 183.0},
    {'k': 6, '未知序列': 0, 'Baumannia': 280.0, 'Psychromonas': 114.0,
     'Sphingomonas': 88.0, 'Roseiflexus': 341.0, 'Hydrogenobaculum': 150.0,
     'Alteromonas': 233.0, 'Denitrovibrio': 165.0, 'Frankia': 86.0,
     'Candidatus': 236.0, 'Corynebacterium': 183.0},
    {'k': 7, '未知序列': 0, 'Baumannia': 280.0, 'Psychromonas': 104.0,
     'Sphingomonas': 85.0, 'Roseiflexus': 345.0, 'Hydrogenobaculum': 142.0,
     'Alteromonas': 240.0, 'Denitrovibrio': 159.0, 'Frankia': 73.0,
     'Candidatus': 254.0, 'Corynebacterium': 194.0},
    {'k': 8, '未知序列': 1, 'Baumannia': 286.0, 'Psychromonas': 78.0,
     'Sphingomonas': 82.0, 'Roseiflexus': 355.0, 'Hydrogenobaculum': 110.0,
     'Alteromonas': 264.0, 'Denitrovibrio': 143.0, 'Frankia': 49.0,
     'Candidatus': 297.0, 'Corynebacterium': 211.0},
    {'k': 9, '未知序列': 20, 'Baumannia': 294.0, 'Psychromonas': 26.0,
     'Sphingomonas': 77.0, 'Roseiflexus': 373.0, 'Hydrogenobaculum': 101.0,
     'Alteromonas': 272.0, 'Denitrovibrio': 109.0, 'Frankia': 27.0,
     'Candidatus': 346.0, 'Corynebacterium': 231.0}
]

# 将数据写入csv文件
with open('KMM_result.csv', mode='w', newline='') as file:
    fieldnames = ['k', '未知序列', 'Baumannia', 'Psychromonas', 'Sphingomonas',
                  'Roseiflexus', 'Hydrogenobaculum', 'Alteromonas', 'Denitrovibrio',
                  'Frankia', 'Candidatus', 'Corynebacterium']
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(data)

