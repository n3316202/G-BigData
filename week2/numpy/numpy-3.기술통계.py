#https://datascienceschool.net/01%20python/03.04%20%EA%B8%B0%EC%88%A0%20%ED%86%B5%EA%B3%84.html
import numpy as np
# 넘파이는 다음과 같은 데이터 집합에 대해 간단한 통계를 계산하는 함수를 제공한다. 이러한 값들을 통틀어 기술 통계(descriptive statistics)라고 한다.
# 데이터의 개수(count)
# 평균(mean, average)
# 분산(variance)
# 표준 편차(standard deviation)
# 최댓값(maximum)
# 최솟값(minimum)
# 중앙값(median)
# 사분위수(quartile)

#x={18,5,10,23,19,−8,10,0,0,5,2,15,8,2,5,4,15,−1,4,−7,−24,7,9,−6,23,−13}

x = np.array([18,   5,  10,  23,  19,  -8,  10,   0,   0,   5,   2,  15,   8,
              2,   5,   4,  15,  -1,   4,  -7, -24,   7,   9,  -6,  23, -13])

print(len(x)) # 갯수
print(np.mean(x))  # 평균
print(np.var(x))  # 분산
print(np.std(x))  #표본 표준편차
print(np.max(x))
print(np.min(x))

#사분위수¶
#사분위수(quartile)는 데이터를 가장 작은 수부터 가장 큰 수까지 크기가 커지는
# 순서대로 정렬하였을 때 1/4, 2/4, 3/4 위치에 있는 수를 말한다. 각각 1사분위수, 2사분위수, 3사분위수라고 한다. 1/4의 위치란 전체 데이터의 수가 만약 100개이면 25번째 순서, 즉 하위 25%를 말한다. 따라서 2사분위수는 중앙값과 같다.
#때로는 위치를 1/100 단위로 나눈 백분위수(percentile)을 사용하기도 한다.
# 1사분위수는 25% 백분위수와 같다.

print(np.percentile(x, 0))  # 최소값
print(np.percentile(x, 25)) # 1사분위 수
print(np.percentile(x, 50)) # 2사분위 수
print(np.percentile(x, 75)) # 3사분위 수
print(np.percentile(x, 100)) # 최대값

