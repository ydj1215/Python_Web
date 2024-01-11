# 동적 : 셀리니움

import requests # 리액트의 axios 통신처럼, 파이썬에서 HTTP 요청을 보내기 위해 사용하는 모듈
import json
from bs4 import BeautifulSoup

url = 'https://search.daum.net/search?nil_suggest=btn&w=tot&DA=SBC&q=%EC%98%81%ED%99%94%EC%88%9C%EC%9C%84'

# User-Agent : 클라이언트가 어떤 종류의 브라우저나 디바이스로 인식되길 원하는지를 서버에게 알려주는 역할을 수행,
# 아래 코드에서는 일반적인 브라우저(Chorme과 같은)으로 설정
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36'
}

# 지정한 도메인에 지정한 헤더를 넣어서 요청
response = requests.get(url, headers=headers)

# Beautiful Soup을 사용하여 HTML 파싱 : HTML 문서를 분석하고, 그 안에서 원하는 정보를 추출하는 프로세스
# response.text : HTTP 응답에서 가져온 데이터의 본문을 의미
soup = BeautifulSoup(response.text, 'html.parser')

# HTML 에서 영화 정보가 들어있는 태그를 찾고, 각각의 영화 정보를 리스트로 저장
# 'ol', attrs={'class': 'movie_list'}) : <ol> 태그 중에서 클래스가 movie_list인 첫 번째 태그를 탐색
# ol = ordered list, li = list item
# if문 이전에 얻은 데이터를 리스트에 저장하고, false, 즉 해당 태그 혹욘 요소고 HTML에 존재하지 않는 경우에는 빈 배열을 반환
# aatrs :  Beautiful Soup에서 요소를 검색할 때, 사용되는 속성들을 가르키는 매개변수이다. (class, id 등)
movieInfoList = soup.find('ol', attrs={'class': 'movie_list'}).find_all('li') if soup.find('ol', attrs={
    'class': 'movie_list'}) else []

movie_data = []

for movieInfo in movieInfoList:
    movieRank = movieInfo.find('span', attrs={'class': 'img_number'}) # img_number이라는 클래스를 가진 <span>을 탐색
    movieImg = movieInfo.find('img')
    movieTitle = movieInfo.find('a', attrs={'class': 'tit_main'})
    movieScore = movieInfo.find('em', attrs={'class': 'rate'})
    movieScoreCnt = movieInfo.find('a', attrs={'class': 'link_count'})
    ticketSalesAndOpenDate = movieInfo.find_all('dd', attrs={'class': 'cont'})
    if len(ticketSalesAndOpenDate) > 1: # 찾은 <dd> 태그가 두 개 이상인 경우에만 아래 코드 블록를 실행
        # 이는 티켓 판매 정보와 개봉일 정보가 함께 있는 경우를 고려한 것, 함께 있다면 한 개일 것
        movieTicketSales = ticketSalesAndOpenDate[0]
        movieOpenDate = ticketSalesAndOpenDate[1]
    else:  # 함께 있는 경우
        movieTicketSales = ticketSalesAndOpenDate[0]
        movieOpenDate = None

    movie_data.append({
        'rank': movieRank.get_text() if movieRank else "X",
        'image': movieImg['src'] if movieImg else "X",
        'title': movieTitle.get_text().strip() if movieTitle else "X",
        'score': movieScore.get_text() if movieScore else "X",
        'eval_num': movieScoreCnt.get_text() if movieScoreCnt else "X",
        'reservation': movieTicketSales.get_text().strip() if movieTicketSales else "X",
        'open_date': movieOpenDate.get_text().strip() if movieOpenDate else "X"
    })

# 각각의 요소가 딕셔너리 형태를 하고 있는 리스트를 JSON 형식으로 변환
# ensure_ascii=False : ASCII 로 인코딩하지 말라는 옵션으로, 한글과 같은 비 ASCII 문자를 그대로 유지
# indent : 문자열을 보기 쉽게 들여쓰기를 설정
# dump : 일반적으로 데이터를 파일에 쓰는 작업을 의미, 그러나 여기서는 dumps이기 때문에,
# dumps : 문자열로 반환한다는 의미
json_data = json.dumps(movie_data, ensure_ascii=False, indent=4)
print(json_data)

# 스프링 서버에 데이터 전송
server_url = 'http://localhost:8080/movies/insert'
headers = {"Content-Type": "application/json; charset=utf-8"}
response = requests.post(server_url, data=json_data.encode('utf-8'), headers=headers)

if response.status_code == 200:
    print("Data sent to the server successfully!")
else:
    print(f"Data transmission failed with status code: {response.status_code}")
    print(response.text)  # 실패 시의 응답의 내용을 출력
