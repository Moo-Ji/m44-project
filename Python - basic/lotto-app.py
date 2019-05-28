# 로또 번호 생성기
import random

lotto = range(1, 46)

number = random.sample(lotto, 6)

print(f'행운의 숫자는 {number}입니다.')
