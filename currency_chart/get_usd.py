from bs4 import BeautifulSoup
import requests

url = "https://finance.naver.com/marketindex/"
html = requests.get(url).text
soup = BeautifulSoup(html, 'html.parser')
# print(soup.prettify())

usd = soup.select_one(
    "#exchangeList > li:nth-of-type(1) > a.head.usd > div > span.value")  # class 가 'value' 인 span tag

# print(usd, type(usd), float(usd))
print("usd=", usd, float(usd.string.replace(',', '')))          # .string 메소드로 태그 벗겨준다

