from PIL import Image, ImageDraw, ImageFont
                        #(가로, 세로)
img = Image.new("RGBA", (500,100), 0)

soimg = Image.open(f"./img/so/2.jpg")

fnt = ImageFont.truetype("arial.ttf", 100)

d = ImageDraw.Draw(soimg)

d.text((0,0), "20220919", font=fnt, fill=(0,0,0))

d = ImageDraw.Draw(soimg)

soimg.save('./img/save/temp.png')

soimg.show()