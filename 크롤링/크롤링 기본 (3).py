import requests
import json

# 딕셔너리 형태의 JSON 데이터 생성
data = {
	"id" : "aaa",
	"password" : "aaa1234A",
	"name" : "유동재",
}

# JSON 데이터를 서버로 전달하기
url = "http://localhost:8080/test/python"
headers = {"Content-Type" : "application/json;charset=UTF-8"} # 헤더 설정
res = requests.post(url, data=json.dumps(data), headers=headers)

# 서버의 응답 확인
if res.status_code == 200:
	print("데이터가 성공적으로 전송되었습니다.", res.status_code)
else :
	print("데이터 전송에 실패했습니다.", res.status_code)