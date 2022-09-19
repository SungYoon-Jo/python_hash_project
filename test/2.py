from PIL import Image
img = Image.open('memi.jpg') # 이미지 파일명 또는 파일 위치
img.show() # 이미지 확인
img.save('memi_save.jpg',"JPEG") # 현재 환경에 memi_save라는 이름으로 저장

# 저장된 이미지 확인
img_2 = Image.open('memi_save.jpg') 
img_2.show()