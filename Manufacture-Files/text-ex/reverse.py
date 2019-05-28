# 파일을 읽어와서 각 줄을 리스트의 요소로 담기
with open('numbers.txt', 'r') as f:
    lines = f.readlines()

# 내용을 뒤집어서 다시 쓰기.
with open('numbers.txt', 'w') as f:
    for re_line in reversed(lines):
        f.write(re_line.rstrip() + '\n') # 가장 아래 빈 줄이 없어도 문자를 각 줄에 나누었음.
