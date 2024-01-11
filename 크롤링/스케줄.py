import schedule
import time
import requests
from bs4 import BeautifulSoup

def perform_web_crowling():
    # 웹 크롤링 작업 수행
    url = "http://www.naver.com"
    res = requests.get(url)
    if res.status_code == 200:
        print("요청 성공!")
        soup = BeautifulSoup(res.text, "html.parser")
        print(soup)
    else :
        print("요청 실패!")

def job():
    print("웹 크롤링을 수행 합니다.")
    perform_web_crowling()

# 매일 정해진 시간에 동작하도록 구현
schedule.every().day.at("09:44").do(job)

# 1분에 한번씩 크롤링
# schedule.every(1).minutes.do(job)

while True:
    schedule.run_pending() # schedule 모듈에 등록딘 예약된 작업들 중 실행해야 할 작업이 있는지 확인 후 실행
    time.sleep(1) # 각 루프마다 1초씩 휴식, 꼭 넣어주자, sleep()이 없으면, 가능한 가장 빠른 속도로 확인을 진행하여 CPU 리소스를 과도하게 많이 소모하게 된다.