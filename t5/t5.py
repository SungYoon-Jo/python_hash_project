import io
from PIL import Image

path = "./test.jpg"
with open(path, "rb") as f:
    data = f.read()
    
data_io = io.BytesIO(data)

img = Image.open(data_io)

output = io.BytesIO()
img_pil.save(   )