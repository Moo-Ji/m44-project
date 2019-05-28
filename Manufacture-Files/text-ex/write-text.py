# 파일을 여는 함수 open ('파일 이름', 'open option',
# r: 읽기  # w: 쓰기 (overwrite) #a: 추가 ( append)

# f = open('mulcam.txt', 'w')  # 연 파일의 객체를 반환.
# for i in range(5):
#     f.write(f'Happy Hacking {i + 1}\n')
# f.close()  # 종료 명령이 없으면 데이터가 기록되지 않은 채 날아갈 수 있다.

'''
파이썬에서 with 구문은 '컨텍스트 매니저'이다.
with 블럭을 통해 명시적으로 파일을 불러서 작업하는 코드 블럭을 만들 수 있다.
with 블럭이 종료되면 자동으로 파일을 닫는다.
'''
with open('mulcam.txt', 'w') as f:  # close를 작성하지 않아도 자동으로 열고 닫음
    f = open('mulcam.txt', 'w')  # 연 파일의 객체를 반환.
    for i in range(5):
        f.write(f'Happy Hacking {i + 1}\n')
