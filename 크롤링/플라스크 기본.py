# 스케줄 기능이 아니라 플라스크를 사용하는 이유?
# 실시간 요청에 대한 처리가 스케줄 기능을 사용하면 불가능

# 마이크로 서비스 아키텍처 : 하나의 애플리케이션을 여러 개의 작은 독립적인 서비스로 분류하는 것
# 독립적인 서비스 : 자체적으로 기능을 수행하고, 자신 만의 데이터 베이스를 가질 수 있으며, 다른 서비스와의 의존성을 최소화 하는 것

# 예를 들자면 스프링에서 컨트롤러로 기능을 세분화 하는 것은 컨트롤러가 모두 하나의 앱에서 작동하므로 마이크로 서비스 아키텍처가 아니다.

# 아래가 마이크로 서비스 아키텍처의 예시이다.
# 1. 파이썬 프로젝트가 웹에서 크롤링을 통해 데이터를 수집하고, 이를 JSON 형태로 반환한다.
# 2. 스프링 프로젝트가 이 크롤링 서비스의 API를 호출하여 데이터를 받아온 후, 이를 데이터 베이스에 저장한다.

from flask import Flask, jsonify, Response, request
from bs4 import BeautifulSoup
import requests
import json

# 웹 애플리케이션의 핵심이 되는 플라스크 객체를 생성
#  __name__ : 현재 실행 중인 모듈의 이름을 전달하는 것이다.
app = Flask(__name__)

# 임의의 데이터를 정의
data = {
    'stations': ['강남역', '역삼역', '서울역'],
    'ridership': [1000, 800, 1200]
}

# GET 요청을 처리하는 라우터
@app.route('/api/data/', methods=['GET'])
def get_data():
    #  정의된 데이터를 JSON 형식으로 변환하여 클라이언트에 응답
    res = Response(json.dumps(data, ensure_ascii=False), mimetype='application/json; charset=utf-8')
    return res

@app.route('/api/weather/', methods=['GET'])
def get_weather():
    url = "http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108"

    # HTTP GET 요청
    response = requests.get(url)
    # HTML 파싱
    soup = BeautifulSoup(response.text, "html.parser")
    output = ""

    for loc in soup.select("location"):
        output += f"<h3>{loc.select_one('city').string}<h3>"
        output += f"날씨 : {loc.select_one('wf').string}</br>"
        output += f"최저/최고 기온 : {loc.select_one('tmn')}/{loc.select_one('tmx')}</hr>"
    # HTML 형식으로 반환
    return output

@app.route('/api/query', methods=['GET'])
def get_query():
    output = ""
    item_type = request.args.get('type', default=None, type=None)
    item_color = request.args.get('color', default=None, type=None)
    output += f"<h1>{item_type}</h1>"
    output += f"<h1>{item_color}</h1>"
    # HTML 형식으로 반환
    return output

# 서버 실행
# if __name__ == '__main__' : 해당 모듈, 즉 "플라스크 기본.py"를 직접 실행 할때는 if문의 실행되고,
# 다른 파일에서 "플라스크 기본.py"를 import한 후에 실행 시, else(존재한다면)문이 실행될 것이다.
if __name__ == '__main__':
    app.run(debug=True) 
    # debug=True : 코드에 수정사항이 존재할 때, 자동으로 서버를 재시작

# Flask 앱은 기본적으로 http://127.0.0.1:5000/ 에서 실행되기 때문에,
# http://127.0.0.1:5000/api/data/ 와 같이 직접 주소를 입력해야 한다.


