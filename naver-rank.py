from bs4 import BeautifulSoup
import requests

response = requests.get('https://www.naver.com/')

html = response.text

soup = BeautifulSoup(html, 'html.parser')  # html.parser를 사용해서 soup에 넣겠다
# soup.find_all("span", class_="ah_k")
# select('."태그명"') #.은 클래스를 나타냄. 태그는 그냥 이름을 바로 쓰면 된다. .
# 같은 라인의 클래스는 .으로 연결함. 한칸을 띄워 쓰면 안의 클래스에 접근하겠다.
# div.클래스 명.클래스 명 span.클래스명 이렇게 입력하면 된다.
key = []
for tag in soup.select('span[class="ah_k"]'):
    key.append(tag.text)
print('현재 급상승 검색어는')
for i in range(1, 11):
    print(f'{i} {key[i - 1]}')

print('입니다.')
