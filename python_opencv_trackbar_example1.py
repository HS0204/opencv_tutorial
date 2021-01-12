import numpy as np
import cv2

def nothing(x):
    print(x)

img = np.zeros((300,512,3), np.uint8)
cv2.namedWindow('image')

cv2.createTrackbar('B', 'image', 0, 255, nothing) # 트랙바 범위 0부터 255까지
cv2.createTrackbar('G', 'image', 0, 255, nothing)
cv2.createTrackbar('R', 'image', 0, 255, nothing)

switch = '0 : OFF\n 1 : ON'
cv2.createTrackbar(switch, 'image', 0, 1, nothing)

while(1):
    cv2.imshow('image', img)
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break

    b = cv2.getTrackbarPos('B', 'image') # 트랙바 속성 추출
    g = cv2.getTrackbarPos('G', 'image')
    r = cv2.getTrackbarPos('R', 'image')
    s = cv2.getTrackbarPos(switch, 'image')

    if s == 0: # 스위치가 0일 때 img는 변하지 않음
        img[:] = 0
    else:
        img[:] = [b,g,r] # 앞서 추출한 속성으로 img 색상 조정

cv2.destroyAllWindows()