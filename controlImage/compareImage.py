from PIL import Image
from PIL import ImageChops

def cropImage(image,cropImagePath):
    # 자를 영역 지정 (left, upper, right, lower)
    left = 0
    upper = 76
    right = 1080
    lower = 2400

    # 이미지 자르기
    Image.open(image).crop((left, upper, right, lower)).save(cropImagePath)

def imageSimilarity(image1, image2, threshold=95):
    # 이미지 열기
    img1 = Image.open(image1)
    img2 = Image.open(image2)

    # 이미지 차이 계산
    diff = ImageChops.difference(img1, img2)

    # 차이 계산 결과를 0-255 사이 값으로 변환
    diff = diff.convert('L')

    # 이미지 유사성 계산
    bbox = diff.getbbox()
    if bbox:
        similarity = (bbox[2] * bbox[3] * 100) / (img1.size[0] * img1.size[1])
        print(similarity)
        # 유사성이 지정된 임계값 이상인지 확인
        if similarity >= threshold:
            return "pass"
        else:
            return "fail"
    else:
        # 차이가 없는 경우
        return "pass"