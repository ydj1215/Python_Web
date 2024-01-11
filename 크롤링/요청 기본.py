import requests
from bs4 import BeautifulSoup


# res = requests.get("http://naver.com")
res = requests.get("http://google.com")

print("응답 코드 : ", res.status_code)
res.raise_for_status() # 문제가 있으면 에러 출력하고 끝냄
print(len(res.text)) # 문자열의 길이 반환

with open("google.html", "w", encoding="utf-8") as f:
    f.write(res.text)

# soup = BeautifulSoup(res.text, 'html.parser')

# if res.status_code == requests.codes.ok:
#     print("정상 입니다.")
#     print(soup)
# else :
#     print("네트워크 오류 : [에러코드 ", res.status_code, "]");