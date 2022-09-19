from PIL import Image, ImageDraw, ImageFont
                        #(가로, 세로)
img = Image.new("RGBA", (500,100), 0)
d = ImageDraw.Draw(img)

fnt = ImageFont.truetype("arial.ttf", 100)
d.text((0,0), "20220919", font=fnt, fill=(0,0,0))
img.save('./img/save/temp.png')
img.show()