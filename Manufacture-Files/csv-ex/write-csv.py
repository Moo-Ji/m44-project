lunch = {
    '20층': '123-234',
    '양자강': '345-435',
    '백수산': '234-234'

}

# 1. String formatting
with open('lunch.csv', 'w', encoding='utf-8') as f:
    for item in lunch.items():  # items를 통해 키 밸류가 리스트로 나옴.
        f.write(f'{item[0]},{item[1]}\n')

# 2. Join mathod 활용
with open('lunch2.csv', 'w', encoding='utf-8') as f:
    for item in lunch.items():
        f.write(','.join(item) + '\n')

# 3. csv.writer

import csv

with open('lunch3.csv', 'w', newline='', encoding='utf-8') as f:
    csv_writer = csv.writer(f)
    for item in lunch.items():
        csv_writer.writerow(item)
