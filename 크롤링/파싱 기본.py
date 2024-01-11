from bs4 import BeautifulSoup

# HTML 문서
htmlDoc = '''
<html>
  <head>
    <title>Example Page</title>
  </head>
  <body>
    <h1>Hello, Beautiful Soup!</h1>
    <div class="content">
      <p>This is a paragraph.</p>
      <p>This is another paragraph.</p>
    </div>
    <a href="https://www.example.com">ExampleLink</a>
    <a href="https://www.google.com">GoogleLink</a>
  </body>
</html>
'''

# HTML 문서를 파싱하여 BeautifulSoup 객체 생성
soup = BeautifulSoup(htmlDoc, 'html.parser')

# 타이틀 태그 검색
titleTag = soup.title
print(titleTag)

print()

# 클래스가 "content" 인 div 태그 검색
divTags = soup.select('div.content')
for div in divTags:
	print(div)

print()

for div in divTags:
	print(div.text)

# href 속성이 있는 모든 a 태그 검색
aTags = soup.findAll('a', href=True)
for tag in aTags:
	print(aTags)

# 파이썬은 카멜이 아닌 스네이크 표기법을 따른다.