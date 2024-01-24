from PIL import Image
import numpy as np

def cropImage(image,cropImagePath):
    # 자를 영역 지정 (left, upper, right, lower)
    left = 0
    upper = 76
    right = 1080
    lower = 2400

    # 이미지 자르기
    Image.open(image).crop((left, upper, right, lower)).save(cropImagePath)

def mse(image1, image2):
    # 이미지를 배열로 변환
    array1 = np.array(image1)
    array2 = np.array(image2)

    # 두 이미지 간의 Mean Squared Error 계산
    err = np.sum((array1 - array2) ** 2)
    err /= float(array1.shape[0] * array1.shape[1])

    return err

def compare(image_path1,image_path2):

    # 이미지 불러오기
    image1 = Image.open(image_path1)
    image2 = Image.open(image_path2)

    # 이미지 유사도 계산
    similarity = mse(image1, image2)

    # 1에서 100으로 정규화된 유사도 값 계산
    normalized_similarity = 100 - (similarity * 100)

    # 출력 및 판정
    return normalized_similarity