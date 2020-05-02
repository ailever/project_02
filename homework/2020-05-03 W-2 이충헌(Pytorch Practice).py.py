# -*- coding: utf-8 -*-
"""PyTorch Chungheon Lee

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1AA--9nTi0MAwRLs1r76HruGdCozkv-66
"""

import torch
# 난수를 생성하는 rand 함수를 사용하여 2행 3열의 텐서 생성
x = torch.rand(2,3)
print(x)

import torch
# 평균0, 표준편차 1의 정규분포 형성
x = torch.randn(2,3)
print(x)

import torch
# int이기에 정수형의 난수를 생성
# range를 0에서 10으로 설정함
# 2행 3열의 텐서 생성
x = torch.randint(0,10,size=(2,3))
print(x)

import torch
 # zeros로 할당하게 되면 해당 행렬에 값이 모두 0이 생성된다.
x = torch.zeros(2,3)
print(x)

import torch
 # reference 된 다른 텐서의 형상과 동일한 텐서 생성.
ref = torch.rand(2,3)
x = torch.zeros_like(ref)
print(x)

import torch
 #ones라고 하면 1로 채워지게 된다.
x = torch.ones(2,3)
print(x)

import torch
 # like()의 괄호 안에 ref 된것이 2행 3열이고, ones는 1로 텐서를 채우라는 뜻이기에
 # 2행 3열이고 1로 채워진 텐서가 생성된다.
ref = torch.rand(2,3)
x = torch.ones_like(ref)
print(x)

import torch
 #텐서의 타입을 물어보는 방법. x.type(), type(x)를 활용하면 된다.
x = torch.rand(2,3)
print(x.type()) # torch.FloatTensor
print(type(x)) # <class 'torch.Tensor'>

import torch

x = torch.rand(2,3) + 1.5  # 앞에서 torch.rand(2,3)은 타입이 FloatTensor라는 것을 알 수 있었다.
int_x = x.type(dtype=torch.IntTensor) # 하지만 여기에서 torch.IntTensor를 통해 정수형으로 변경하였다.
print(int_x)

import torch
import numpy as np
 # 임시 저장공간인 buffer에 2행 3열의 정수형 배열을 생성
x1 = np.ndarray(shape=(2,3), dtype=int, buffer=np.array([1,2,3,4,5,6])) 
print(x1)
# x1을 print를 할 수는 있으나 buffer여서 type이 무엇인지에 대해서는 반환이 되지 않는다
# 앞의 넘파이 배열을 torch를 이용해 텐서로 만들었다.
x2 = torch.from_numpy(x1)
print(x2, x2.type())
 # numpy()로 앞의 텐서를 다시 넘파이 배열로 만들었다.
x3 = x2.numpy()
print(x3)

import torch
 #실수(float)형 텐서 만들기
x = torch.FloatTensor([[1,2,3],[4,5,6]])
print(x)

import torch
 #Tensor를 GPU와 CPU에 옮긴다.
x = torch.FloatTensor([[1,2,3],[4,5,6]])
 
cpu = torch.device('cpu')
gpu = torch.device('cuda')
 
if torch.cuda.is_available():
    x_gpu = x.to(gpu)
    print(x_gpu)
 
x_cpu = x_gpu.to(cpu)
print(x_cpu)

import torch
# 텐서의 크기 확인 
x = torch.FloatTensor(2,3,4,4)
print(x.size()) # torch.Size([2, 3, 4, 4])
print(x.size()[1:2]) torch.Size([3])

import torch
 #텐서의 요소값 접근
x = torch.randn(4,3)
print(x)

print(x[1:3,:])

import torch
 # 인덱스 값으로 지정된 요소값으로 구성된 새로운 텐서 생성. (값을 복사한다.)
x = torch.randn(4,3)
print(x)
 
selected = torch.index_select(x,dim=1,index=torch.LongTensor([0,2]))
print(selected)

import torch
 # 마스크 텐서로 새로운 텐서 생성
 # 마스크 텐서란? - 어디까지가 진짜 데이터고 어디가 더미 데이터인지를 표시한 값.
 # 더미 데이터란? - 패딩을 할 때 무의미한 값으로 채워넣은 것들. 보통 0을 준다.
x = torch.randn(2,3)
print(x)
 
mask = torch.BoolTensor([[False, False, True],[False,True,False]])
out = torch.masked_select(x, mask)
print(out)

import torch
 # 두 개의 텐서의 결합.
x = torch.FloatTensor([[1,2,3],[4,5,6]])
y = torch.FloatTensor([[-1,-2,-3],[-4,-5,-6]])
 
z1 = torch.cat([x,y], dim=0)
print(z1)
 
z2 = torch.cat([x,y], dim=1)
print(z2)

#dim이 2이라면 어떻게 될까?
z3 = torch.cat([x,y], dim=2)
print(z3)
#에러가 출력됨.

import torch
 # stack 함수를 활용해 2개의 텐서 결합하기
x = torch.FloatTensor([[1,2,3],[4,5,6]])
x_stack = torch.stack([x,x,x,x],dim=0)
print(x_stack)

#dim을 1로 설정.
y_stack = torch.stack([x,x,x,x],dim=1)
print(y_stack)

import torch
 # 하나의 텐서를 n개로 분해하기.
z1 = torch.FloatTensor([
    [ 1.,  2.,  3.],
    [ 4.,  5.,  6.],
    [-1., -2., -3.],
    [-4., -5., -6.]
])
x_1,x_2 = torch.chunk(z1,2,dim=0)
print(x_1,x_2,sep='\n')
 
y_1,y_2 = torch.chunk(z1,2,dim=1)
print(y_1,y_2,sep='\n')

import torch
 #하나의 텐서를 분리하는 다른 방법들.
z1 = torch.FloatTensor([
    [ 1.,  2.,  3.],
    [ 4.,  5.,  6.],
    [-1., -2., -3.],
    [-4., -5., -6.]
])
x1,x2 = torch.split(z1,2,dim=0)
print(x1,x2,sep='\n')
 
y1,y2 = torch.split(z1,2,dim=1)
print(y1,y2,sep='\n')
 
y = torch.split(z1,2,dim=1)
for i in y:
    print(i)

import torch
 #1개의 요소를 갖는 축 제거
x1 = torch.FloatTensor(10,1,3,1,4)
x2 = torch.squeeze(x1)
# 축의 개수 지정
print(x1.size(),x2.size())

import torch
 #Unsqueeze 연산
x1 = torch.FloatTensor(10,3,4)
x2 = torch.unsqueeze(x1, dim=0)
print(x1.size(),x2.size())
 
x3 = torch.unsqueeze(x1, dim=1)
print(x1.size(),x3.size())

import torch
import torch.nn.init as init
 #다양한 분포를 갖는 텐서 만들기
x1 = init.uniform_(torch.FloatTensor(3,4),a=0,b=9)
print(x1)
#표준편차 
x2 = init.normal_(torch.FloatTensor(3,4),std=0.2)
print(x2)

x3 = init.constant_(torch.FloatTensor(3,4),3.1415926)
print(x3)

# 텐서 간의 합을 하는 방법
x1 = torch.FloatTensor([[1,2,3],[4,5,6]])
x2 = torch.FloatTensor([[1,2,3],[4,5,6]])
 
add1 = torch.add(x1,x2)
print(add1)
 
add2 = x1+x2
print(add2)

#텐서의 브로드캐스트 합
 # 10을 그대로 가져다가 각각 더해준다.
x1 = torch.FloatTensor([[1,2,3],[4,5,6]])
x2 = x1 + 10
print(x2)

# 텐서의 곱
x1 = torch.FloatTensor([[1,2,3],[4,5,6]])
x2 = torch.FloatTensor([[1,2,3],[4,5,6]])
 
x3 = torch.mul(x1,x2)
print(x3)
 
x4 = x1*x2
print(x4)

# 텐서의 나눗셈
x1 = torch.FloatTensor([[1,2,3],[4,5,6]])
x2 = torch.FloatTensor([[1,2,3],[4,5,6]])
 
x3 = torch.div(x1,x2)
print(x3)
 
x4 = x1/x2
print(x4)

import torch
 #텐서의 제곱
x1 = torch.FloatTensor([[1,2,3],[4,5,6]])
 
x2 = torch.pow(x1,2)
print(x2)

x3 = x1**2
print(x3)

import torch
 # exponential. 지수계산.
x1 = torch.FloatTensor([[1,2,3],[4,5,6]])
x2 = torch.exp(x1)
print(x2)

import torch
 # 로그 연산
x1 = torch.FloatTensor([[1,2,3],[4,5,6]])
x2 = torch.log(x1)
print(x2)

import torch
 # 행렬곱
x1 = torch.FloatTensor([[1,2,3],[4,5,6]])
x2 = torch.FloatTensor([[1,2,3],[4,5,6],[7,8,9]])
x3 = torch.mm(x1,x2)
print(x3)

import torch
 #배치 행렬곱 연산.
 # 앞에 하나 뒤에 하나 해서 같은 값이 출력됨.
x1 = torch.FloatTensor([
    [[1,2,3],[4,5,6]],
    [[1,2,3],[4,5,6]],
])
x2 = torch.FloatTensor([
    [[1,2,3],[4,5,6],[7,8,9]],
    [[1,2,3],[4,5,6],[7,8,9]],
])
x3 = torch.bmm(x1,x2)
print(x3)

# x1의 두번째 배치를 바꾸니 두 번째 값만 달라지는 것 확인
x1 = torch.FloatTensor([
    [[1,2,3],[4,5,6]],
    [[1,2,3],[4,5,7]],
])
x2 = torch.FloatTensor([
    [[1,2,3],[4,5,6],[7,8,9]],
    [[1,2,3],[4,5,6],[7,8,9]],
])
x3 = torch.bmm(x1,x2)
print(x3)

import torch
 # 벡터의 내적
x1 = torch.tensor([1,2,3,4])
x2 = torch.tensor([2,3,4,5])
x3 = torch.dot(x1,x2)
print(x3)

import torch
 # 텐서의 전치
 # 행과 열이 바뀌었다.
 # transpose
x1 = torch.tensor([[1,2,3],[4,5,6],[7,8,9]])
print(x1)
x2 = x1.t()
print(x2)

import torch
 # 텐서의 내부 차원 간 바꿈
hwc_img_data = torch.rand(100, 64, 32, 3)
print(hwc_img_data.size())
chw_img_data = hwc_img_data.transpose(1,2)
print(chw_img_data.size())
chw_img_data = chw_img_data.transpose(1,3)
print(chw_img_data.size())

# 값 바꾸기 실험
# 2,1 로 할 때는 내용이 같지만 3,1 로 하면 값이 달라지는 것을 확인
hwc_img_data = torch.rand(100, 64, 32, 3)
print(hwc_img_data.size())
chw_img_data = hwc_img_data.transpose(3,1)
print(chw_img_data.size())

import torch
 #벡터의 내적, 행렬과 벡터의 곱, 행렬간 곱 총정리.
m = torch.randn(100,10)
v = torch.randn(10)
 
d = torch.matmul(v,v)
print(d)
 
v2 = torch.matmul(m,v)
 
m2 = torch.matmul(m.t(), m)
print(m2)

import torch
 # 다항분포 확률값 기반의 샘플링
 # 확률이기에 매번 값이 달라진다.
  # 다항 분포는 여러 개의 값을 가질 수 있는 독립 확률변수들에 대한 확률분포로, 
  # 여러 번의 독립적 시행에서 각각의 값이 특정 횟수가 나타날 확률을 정의한다.
x1 = torch.FloatTensor(
    [
        [1,2,3,4,5,6,7,8,9],
        [9,8,7,6,5,4,3,2,1],
        [1,2,3,4,5,6,7,8,9],
        [9,8,7,6,5,4,3,2,1]
    ]
)
i = torch.multinomial(x1.exp(), 1)
print(i)

import torch
 # 상위 n개 가져오기
x = torch.rand(10)
print(x)
 # torch.topk: 예측 값에서 argmax가 아닌 top-k에 대한 결과 값을 받고 싶을 때 사용
scores, indices = torch.topk(x, 3)

 
for i in range(0,3):
    print(indices[i].item(), scores[i].item())