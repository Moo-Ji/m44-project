#   dummy-ex 폴더 내의 모든 txt파일의 지원자_ => 합격자_ 로 변경
# 'abc'.replace('b', 'e') => aec

import os

filename = os.path.splitext(r'D:\pycharm_WS\m44-project\Manufacture-Files\Dummy-ex\Dummy.py')  # r 이스케이프 시퀀시 무시.

os.chdir(r'D:\pycharm_WS\m44-project\Manufacture-Files\Dummy-ex')
filenames = os.listdir('.')

for filename in filenames:
    os.path.splitext(filename)
    new_name = filename.replace('지원자_', '합격자_')
    os.rename(filename, new_name)
    print(filename)

# for filename in filenames:
#     txt = os.path.splitext(filename)[1]
#     if txt == '.txt':
#         newFilename = filename.replace('지원자_','합격자_')
#         # print(newFilename)
#         os.rename(filename, newFilename)
