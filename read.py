with open('titanic.csv', encoding='utf-8')as f:
    header = f.readline().strip().split(',')
    rows = [line.strip().split(',') for line in f]
print(header)
print(len(rows),'Строк')
print(rows[0],'\n')

#Шаг4
cols = {h: [] for h in header}
for r in rows:
    for h,v in zip(header,r):
        if v == '':
        
            continue

        try:
            cols[h].append(float(v))

        except ValueError:
            cols[h].append(v)

print(cols['age'][:10])