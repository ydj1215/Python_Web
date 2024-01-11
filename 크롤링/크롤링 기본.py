import json  # JSON 형식의 데이터를 처리

# JSON 형식의 문자열
jsonString = '''{"name" : "KH", "id" : 123456, "history" : [
    {"date" : "2023-05-10", "item" : "iPhone 14 Pro"},
    {"date" : "2023-05-24", "item" : "Galuxy S23 Ultra"}
]}'''

# JSON 형식에서 딕셔너리로 변환
dict = json.loads(jsonString)
print(dict)
print(dict["name"])
for h in dict["history"]:
	print(h["date"], h["item"])
