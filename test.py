import controlImage.compareImage as compareImage

#스크린샷 이미지 경로
screenshotImage = 'C:/mobile_automation_testing/niceCheck/niceCheck_Login/controlImage/image/Screen.png'

#비교군 이미지 경로
guideImage = 'C:/mobile_automation_testing/niceCheck/niceCheck_Login/controlImage/image/guide.png'

#이미지 비교 및 결과를 result에 저장
result = compareImage.imageSimilarity(guideImage, screenshotImage)

print(result)
