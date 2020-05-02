Summary Alexnet, here.

# ImageNet Classiﬁcation with Deep Convolutional Neural Networks
paper : https://papers.nips.cc/paper/4824-imagenet-classification-with-deep-convolutional-neural-networks.pdf

---

### Overall Architecture
5개의 convolution layer, 3개의 fully-connected layer로 이루어져있음
![OverallArchitecture](https://user-images.githubusercontent.com/63084838/80869888-dce6dd80-8cdd-11ea-8c37-528984a183d3.JPG) 

### ReLU Nonlinearity
- 활성화 함수로Tanh함수 대신 ReLU(rectified linear units) 함수를 사용
- Tanh을 사용하는 것보다 학습속도가 6배 가량 빠름
![ReLUNonlinearity](https://user-images.githubusercontent.com/63084838/80869986-7e6e2f00-8cde-11ea-86ca-768a379f5cc3.JPG)

### Training on Multiple GPUs
- 두 대의 GPU를 병렬 처리
- 메모리 문제를 해결하기 위함

### Local Response Normalization
- 같은 위치의 pixel에 대해 다수의 feature map간의 Normalization
- 세포에서 발생하는 ‘측명억제(lateral inhibition)’ 현상과 같은 효과

### Overlapping Pooling
- conv을 통해 얻은 feature map의 크기를 줄이기 위해 사용
- overlapping은 풀링 커널이 중첩되면서 지나감
- non-overlapping보다 top-1, top-5 에러율을 감소시키는 데 효과적임

### Data Augmentation
- 적은 양의 데이터를 가지고 훈련시킬 경우에 overfitting 될 가능성이 높음
- overfitting을 줄이기 위해 Data Augmentation을 통해 데이터의 양 늘림

### Dropout
- overfitting을 줄이기 위해 Dropout 사용
- 각각 히든 뉴런 값을 50%확률로 0으로 셋팅
- 일부(첫번째,두번째)의 fully-connected layer에 적용하여 학습 진행
