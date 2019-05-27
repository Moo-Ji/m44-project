from bs4 import BeautifulSoup
import requests

response = requests.get('https://www.naver.com/')

html = response.text

soup = BeautifulSoup(html, 'html.parser')  # html.parser를 사용해서 soup에 넣겠다
# soup.find_all("span", class_="ah_k")

key = []
for tag in soup.select('span[class="ah_k"]'):
    key.append(tag.text)
print('현재 급상승 검색어는')
for i in range(1, 11):
    print(f'{i} {key[i - 1]}')

print('입니다.')
