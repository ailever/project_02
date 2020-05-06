
#  Very deep convolutional networks for large-scale image recognition

paper : https://arxiv.org/pdf/1409.1556.pdf

# Abstract
![enter image description here](https://github.com/ailever/project_02/blob/master/Image/1.png)
- 깊이의 영향을 확인하고자 Conv  filter 커널의 사이즈는 가장 작은 3 x 3으로 고정
→ 3x3의 작은 filter만을 사용한 CNN모델

- 16, 19개의 깊은 layers 사용
→ VGG16 / VGG19

##  Overall Architecture

![Architecture](https://github.com/ailever/project_02/blob/master/Image/2.png)

-   13 Convolution Layers + 3 Fully-connected Layers
-   3x3 convolution filters
-   stride: 1 & padding: 1
-   2x2 max pooling (stride : 2)
-   ReLU

![ConvNet Configuration](https://github.com/ailever/project_02/blob/master/Image/3.png)

D : VGG16
- 13 Convolution Layers + 3 Fully-connected Layers
- max pooling
- 3x3 convolution filters
- stride: 1
- padding: 1

E : VGG19
- 16 Convolution Layers + 3 Fully-connected Layers
- max pooling
- 3x3 convolution filters
- stride: 1
- padding: 1


## 3x3 filter

오직 3x3 filter 만을 사용하여 성능 개선을 보임

![3x3 filter](https://github.com/ailever/project_02/blob/master/Image/4.png)
 - 비선형성 증가  
Convolution 연산은 ReLU  함수를 포함  
1-layer 7x7 필터링의 경우 한 번의 비선형 함수가 적용되고,  
3-layer 3x3 필터링은 세 번의 비선형 함수가 적용됨  
→ 레이어가 증가함에 따라 비선형성이 증가하게 됨  

 - 학습 파라미터 수의 감소
Convolutional Network를 학습할 때, 가중치는 filters의 크기에 해당  
--1-layer 7x7에 대한 학습 파라미터 수는 49  
--3-layer 3x3에 대한 학습 파라미터 수는 27(3x3x3)  
→ 파라미터 수가 크게 감소  
--가중치가 적다 = 훈련시켜야 할 것의 갯수가 작아진다 = 학습의 속도가 빨라짐  

## Result
![Result](https://github.com/ailever/project_02/blob/master/Image/5.png)

- 깊이가 깊어질 수록 error율 감소

- D (VGG16)  vs  E (VGG19)
 - error율이 같거나 나쁜 성능을 보임  
 -Vanishing-gradient의 현상으로  해석 가능  
 -Activation-function으로 ReLU를 사용 하였지만  gradient vanishing  현상 발생  
  → E (VGG19)  이후로 더이상 layer을  늘리는 것을 멈춤  

# Prevent  Overfitting


 - 모델을 학습 할 때 모든 입력 이미지의 크기가 224x224로 고정.  
 -> 제한된 데이터 수를 증가 시킬 수 있음. — Data augmentation  

- 객체의 다양한 측면이 반영 될 수 있습니다.  

- 변환 된 이미지가 작을수록 전체 측면을 더 많이 배울 수 있으며,  
이미지가 클수록 학습의 대상이 더 구체적으로 반영 될 수 있습니다.  

## Conclusion

- 네트워크의 깊이가 증가함에 따라 이미지 분류의 정확도가 증가 함을 알 수 있었음.

- 실험에서 네트워크 깊이가 최대 19 개의 계층으로 사용 된 이유는 VGG-19에서 오류율이 수렴 되었기 때문임.

- 많은 훈련 데이터가있는 경우 더 deep한 모델이 더 유용 할 수 있음.

## Compare Alexnet
- 네트워크의 깊이 변화에 따른 top-5 error의 변화

![Result](https://github.com/ailever/project_02/blob/master/Image/6.png)

-  Alexnet과 비교
1. 작은 필터(3x3  필터)만을 사용하였다.
2. 기존보다 훨씬 깊은 레이어를 사용하였다.
3. 작은 필터를 사용하였기 때문에 파라미터의 갯수가 감소하였다.
