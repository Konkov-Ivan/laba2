with open('titanic.csv', encoding='utf-8')as f:
    header = f.readline().strip().split(',')
    rows = [line.strip().split(',') for line in f]
print(header)
print(len(rows),'Строк')
print(rows[0])