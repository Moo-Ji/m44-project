import os

#   os.chdir('폴더 경로') 지정한 폴더로 이동
#   os.listdir('폴더 이름') 폴더에 저장된 전체 파일 목록을 리스트로 반환
#   os.rename('현재 파일명', '바꿀 파일명') 파일 이름 변경
#   os.path.splitext('파일 이름') 파일 경로와 확장자를 분리하여 반환
#   더미 파일 경로 D:\pycharm_WS\m44-project\Manufacture-Files\Dummy-ex

filename = os.path.splitext(r'D:\pycharm_WS\m44-project\Manufacture-Files\Dummy-ex\Dummy.py')  # r 이스케이프 시퀀시 무시.
print(filename)

os.chdir(r'D:\pycharm_WS\m44-project\Manufacture-Files\Dummy-ex')
filenames = os.listdir('.')
print(filenames)

for filename in filenames:
    txt = os.path.splitext(filename)[-1]
    if txt == '.txt':  # 앞에 지원자_를 붙인다.
        os.rename(filename, f'지원자_{filename}')
    # print(filename)


