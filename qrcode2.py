import qrcode

meu_qrcode = qrcode.make("https://django1-art.herokuapp.com/")
meu_qrcode.save("qrcode_art.png")