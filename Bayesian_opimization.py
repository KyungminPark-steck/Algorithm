def black_box_function(x, y):

    return -x ** 2 - (y - 1) ** 2 + 1
  # 입력 파라미터들의 범위(공간)
pbounds = {'x': (2, 4), 'y': (-3, 3)}

from bayes_opt import BayesianOptimization

# 최적화할 함수와, 입력 파라미터의 범위를 입력 받아서 BayesianOptimization 객체 생성 
optimizer = BayesianOptimization(
    f=black_box_function,
    pbounds=pbounds,
    random_state=1
)

# 함수 반환값을 최대화 할 수 있는 입력 파라미터 값과 반환값을 iteration하면서 최적 검색 
optimizer.maximize(
    init_points=2, #초기 랜덤하게 반복
    n_iter=5, #최적화 총 반복 
)

import numpy as np

result = -9999
x_val = -9999
y_val = -9999
iter_count = 0

for x in np.arange(2, 4.1, 0.1): #2에서 4까지 0.1씩 
    for y in np.arange(-3, 3, 0.1): #-3부터 2.9까지 0.1씩 
        current_result = black_box_function(x, y)
        iter_count += 1
        if current_result > result: #최댓값 찾는 반복문 
            result = current_result 
            x_val = x #그때 X
            y_val = y #그때때 Y

print('iteration count:', iter_count, 'max result:', result, 'x value:', x_val, 'y value:', y_val)

# 입력 파라미터들의 범위(공간)
pbounds = {'x': (2, 40), 'y': (-3, 30)}

optimizer = BayesianOptimization(
    f=black_box_function,
    pbounds=pbounds,
    random_state=1,
)

optimizer.maximize(
    init_points=2,
    n_iter=10,
)

import numpy as np

result = -9999
x_val = -9999
y_val = -9999
iter_count = 0
for x in np.arange(2, 40.1, 0.1):
    for y in np.arange(-3, 30, 0.1):
        current_result = black_box_function(x, y)
        iter_count += 1
        if current_result > result:
            result = current_result
            x_val = x
            y_val = y

print('iteration count:', iter_count, 'max result:', result, 'x value:', x_val, 'y value:', y_val)

