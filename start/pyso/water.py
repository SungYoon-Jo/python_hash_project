import os
from PIL import Image, ImageFont, ImageDraw
from IPython.display import display
 
## 현재 디렉토리에 존재하는 파일들 가져오기: file_li
file_li = os.listdir()
print(file_li[:5])
 
### file_li중에서 그림파일(.png, .jpg)만 가져오기: image_li
image_li = [i for i in file_li if ('.png' in i) or ('.jpg' in i)]
print(image_li[:5])
 
### 그림 1개만 예시로 보기: image_li[0]
img_PIL = Image.open(f"{image_li[0]}")
img_PIL.show()
display(img_PIL)
 
## ImageDraw.Draw()를 이용해 이미지에 글자쓰기
font = ImageFont.truetype("/usr/share/fonts/dejavu/DejaVuSans.ttf", 25)
for file in image_li:
    img = Image.open(f"{file}")
    draw = ImageDraw.Draw(img)
    draw.text((0,10), f"{file}", (0,0,0), font=font)
    draw = ImageDraw.Draw(img)
    img.save(f"./After_process/{file.split('.')[0]}.png")
 
## 이미지에 글자쓴것 주피터로 보기
for file in image_li:
    img_PIL = Image.open(f"./After_process/{file.split('.')[0]}.png")
    img_PIL.show()
    display(img_PIL)
 
## 이미지 사이즈 변환: resize
size = 300,300
for file in image_li:
    img = Image.open(f"./After_process/{file.split('.')[0]}.png")
    img.thumbnail(size, Image.ANTIALIAS)
    display(img)
    img.save('저장할 파일이름.png') # resize 이미지 저장