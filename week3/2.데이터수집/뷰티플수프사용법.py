#https://hleecaster.com/python-web-crawling-with-beautifulsoup/

#pip install beautifulsoup4




import requests
webpage = requests.get("https://www.daangn.com/hot_articles")
#print(webpage.text)


import requests
from bs4 import BeautifulSoup
webpage = requests.get("https://www.daangn.com/hot_articles")
soup = BeautifulSoup(webpage.content, "html.parser")
#print(soup)

#뷰티플 스프에서 메소드는 두개를 기본적으로 알면 된다.
#find 메소드
#select 메소드

tag = '''<p class='example' id='test01'> Hello World! </p>
<p class='example' id='test02'> Hello World! </p>
'''

soup = BeautifulSoup(tag, "html.parser")

# 태그 이름만 특정
print(soup.find('p'))

# 태그 속성만 특정
print(soup.find(class_='example'))
#print(soup.find(attrs = {'class':'exmaple'}))

# 태그 이름과 속성 모두 특정
print(soup.find('p', class_='example'))

print(soup.select('.example'))
print(soup.select_one('.example').text)

print(soup.select_one('#test02').text)





from bs4 import BeautifulSoup
html = """<html><head></head><body>test data</body></html> """
soup = BeautifulSoup(html, 'html.parser')
print(soup.select_one('body').text)