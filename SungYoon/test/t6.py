from stegano import lsb

secret = lsb.hide("./img/img.png", "goodday")
secret.save("hide.png")