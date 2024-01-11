import numpy as np  # 과학적 계산을 위한 핵심 라이브러리

data1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # 리스트
a1 = np.array(data1)  # 리스트 -> 넘파이 배열로 변환
print(a1)

data2 = [0, 1, 2, 3, 4, 5, 3.15, 0.234]
a2 = np.array(data2)
print(a2)  # 묵시적 타입 개스팅 = 자동 형 변환

x = np.array([0.1, 2, 1.3, 4])
print(x)
print(x.shape)  # 배열의 형태
print(x.dtype)  # 배열 요소의 타입 확인

y = np.array(([1, 2, 3], [4, 5, 6]))
print(y)
print(y.shape)  # 2행 3열
print(y.dtype)

# 범위를 지정해 배열 생성
a3 = np.arange(0, 10, 2)  # 0~10 미만 배열 생성, 간격은 2
print(a3)

a4 = np.arange(1, 20)  # 1 이상 20 미만 배열 생성, 간격은 1 = 생략
print(a4)

# 배열 형태 변경
a5 = np.arange(12)  # 0~12
print(a5)

# 배열 형태 변경
aa = np.arange(12).reshape(4, 3)  # 배열의 구조를 변경
print(aa)
print(aa.shape)

# 배열의 시작과 끝 지정, 그리고 데이터의 개수를 지정해 배열 생성, 간격 자동
a6 = np.linspace(1, 10, 20)
print(a6)

a7 = np.linspace(0, np.pi, 20)
print(a7)

# 특별한 형태의 배열 생성
# 1차원 배열
a8 = np.zeros(10)
print(a8)
a9 = np.zeros((3, 4))
print(a9)
a10 = np.ones(10)
print(a10)
a11 = np.ones((5, 5))
print(a11)

# 단위 행렬 생성 :  n*n 정사각형의 행렬에서 주 내각선이 모두 1
a12 = np.eye(4)
print(a12)

# 배열의 타입 변환 : 숫자 뿐
a13 = np.array(['1.5', '0.62', '2', '3.15', '3.1415929'])
print(a13)
print(a13.dtype)  # 데이터 형식이 유니코드이며, 문자의 최대 크기

num_a13 = a13.astype(float)  # 문자열을 실수 타입으로 변환
print(num_a13)

# 난수 배열의 생성 : 0~1 미만의 임의의 실수를 난수
a14 = np.random.rand(2, 3) # 2차원(2 * 3) 난수 배열
print(a14)
a15 = np.random.rand(2, 3, 4) # 3차원(2 * 3 * 4) 난수 배열
print(a15)

# 지정한 범위에 해당하는 정수로 난수 배열 생성
a16 = np.random.randint(10, size=(3, 10))
print(a16)

# 배열의 연산 : 넘파이 배열의 형태가 같다면 사칙 연산 수행 가능
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
result = arr1 ** arr2
print(result)

# 요소별 연산 : true, false 반환
arr3 = np.array([10, 20, 30, 40, 50])
print(arr3 > 20)

# 통계를 위한 연산 : 배열의 합, 평균, 표준편차, 분산, 최소값, 최대값, 누적합, 누적동 등의 통계에서 많이 사용
arr4 = np.arange(5)
print(arr4)
print(f"합계 : {arr4.sum()}")
print(f"평균 : {arr4.mean()}")
print(f"표준편차 : {arr4.std()}")
print(f"분산 : {arr4.var()}")
print(f"최소값 : {arr4.min()}")
print(f"최대값 : {arr4.max()}")

# 배열 인덱싱
arr5 = np.arange(1,6)
print(arr5[3])
print(arr5[0])

# 슬라이싱
new_arr5 = arr5[1:3]
print(new_arr5)

# Universal 함수 : 배열의 원소별 연산을 지원하는 함수
# 산술 연산 : add(), substarct(), multiply(), divide(), power()
# 삼각 함수 : sin(), cos(), tan()
# 집계 함수 : sum(), mean(), max(), min()
# 논리 함수 : logical_and(), logical_or(), logical_not

xx = np.arange(0, 2*np.pi, 0.1)
print(xx)
yy = np.sin(xx)
print(yy)

matrix1 = np.array([[1,2], [4,5]])
matrix2 = np.array([[5,6], [7,8]])
print(matrix1+matrix2)

# 정렬과 탐색
xxx = np.array([9,8,6,4,5,1,6,11])
print(np.amin(xxx)) # 배열 내의 최소값
print(np.amax(xxx)) # 배열 내의 최대값
print(np.max(xxx)) # 배열 내의 최대값, amax와 동일하나 호출 방식의 차이
print(np.argmin(xxx)) # 배열 내의 최소값의 위치
print(np.sort(xxx)) # 오름차순
print(np.argsort(xxx)) # 오름차순 정렬 했을 때의 값의 인덱스

# 브로드 캐스팅 : 배열의 크기가 다른 경우에 연산을 수행
ax = np.array([1,2,3]) # 1차원 배열
bx = np.array([[4], [5], [6]]) # 2차원 배열
cx = ax + bx
print(cx)

