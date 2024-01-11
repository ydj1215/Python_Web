import matplotlib.pyplot as plt # 데이터 시각화를 위한 matplotlib 라이브러리
from sklearn.neighbors import KNeighborsClassifier # KNN 알고리즘을 사용하기 위한 scikit-learn 라이브러리

# 도미 데이터 준비
# 도미의 길이와 무게 데이터
bream_length = [25.4, 26.3, 26.5, 29.0, 29.0, 29.7, 29.7, 30.0, 30.0, 30.7, 31.0, 31.0,
                31.5, 32.0, 32.0, 32.0, 33.0, 33.0, 33.5, 33.5, 34.0, 34.0, 34.5, 35.0,
                35.0, 35.0, 35.0, 36.0, 36.0, 37.0, 38.5, 38.5, 39.5, 41.0, 41.0]
bream_weight = [242.0, 290.0, 340.0, 363.0, 430.0, 450.0, 500.0, 390.0, 450.0, 500.0, 475.0, 500.0,
                500.0, 340.0, 600.0, 600.0, 700.0, 700.0, 610.0, 650.0, 575.0, 685.0, 620.0, 680.0,
                700.0, 725.0, 720.0, 714.0, 850.0, 1000.0, 920.0, 955.0, 925.0, 975.0, 950.0]

# 빙어 데이터 준비
# 빙어의 길이와 무게 데이터
smelt_length = [9.8, 10.5, 10.6, 11.0, 11.2, 11.3, 11.8, 11.8, 12.0, 12.2, 12.4, 13.0, 14.3, 15.0]
smelt_weight = [6.7, 7.5, 7.0, 9.7, 9.8, 8.7, 10.0, 9.9, 9.8, 12.2, 13.4, 12.2, 19.7, 19.9]

# 가장 간단한 머신러닝 프로그램
# K-최근접 이웃 알고리즘 : 입력받은 데이터 위치가 어디에 가까운지를 판단해 결정하는 것
# 빙어와 도미 데이터를 하나의 데이터셋으로 결합
length = bream_length + smelt_length
weight = bream_weight + smelt_weight
fish_data = [[l, w] for l, w in zip(length, weight)]
print(fish_data)

# 빙어와 도미 구분 레이블 준비
# 도미(1)는 35마리, 빙어(0)는 14마리
fish_target = [1] * 35 + [0] * 14
print(fish_target)

# KNN 모델 생성 및 훈련
kn = KNeighborsClassifier()
kn.fit(fish_data, fish_target) # fit() 메소드를 사용하여 모델 훈련

# 모델의 정확도 평가
x = kn.score(fish_data, fish_target) # score() 메소드로 정확도 평가, 실행 결과가 1이면 모든 fish_data의 답을 맞췄다는 의미
print(x)

# 데이터 시각화
plt.scatter(bream_length, bream_weight) # 도미 데이터 시각화
plt.scatter(smelt_length, smelt_weight) # 빙어 데이터 시각화
plt.scatter(30, 600, marker='^') # 새로운 데이터 포인트 (30, 600) 시각화
plt.xlabel('length') # x축 라벨
plt.ylabel('weight') # y축 라벨
plt.show()

# 새로운 데이터 포인트에 대한 예측
kn.predict([[30, 600]]) # predict() 메소드로 새로운 데이터 (30, 600) 분류

# 훈련된 데이터셋 확인
print("kn_fit_X : " + kn._fit_X) # 훈련된 데이터셋의 특성
print("kn_fit_Y : " + kn._y) # 훈련된 데이터셋의 레이블

# 이웃의 수를 49로 설정한 KNN 모델 생성 및 훈련
kn49 = KNeighborsClassifier(n_neighbors=49)
kn49.fit(fish_data, fish_target) # 모델 훈련
kn49.score(fish_data, fish_target) # 모델의 정확도 평가

# 새롭게 입력된 데이터를 머신 러닝 모델이 도미로 분류할 확률
print(35/49)
