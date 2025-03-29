#PREREQUISITE: pip install pillow
from PIL import Image

piecesize = 57
edgesize = 6
boardsize = (piecesize * 8) + (edgesize * 2)


boardimage = Image.new('RGB', (boardsize, boardsize), (0, 0, 0))

imw = Image.open('images_input/vacantonwhite.jpg', mode='r')
imw.convert('RGB')
imb = Image.open('images_input/vacantonblack.jpg', mode='r')
imb.convert('RGB')
for i in range(8):
    for j in range(8):
        if (i + j) % 2 == 0:
            boardimage.paste(imw, (edgesize + (i * piecesize), edgesize + (j * piecesize)))
        else:
            boardimage.paste(imb, (edgesize + (i * piecesize), edgesize + (j * piecesize)))

pieceimage = Image.open('images_input/whitekingonwhite.jpg', mode='r')
pieceimage.convert('RGB')
boardimage.paste(pieceimage, (edgesize + piecesize, edgesize + piecesize))

pieceimage = Image.open('images_input/blackkingonwhite.jpg', mode='r')
pieceimage.convert('RGB')
boardimage.paste(pieceimage, (edgesize + (3 * piecesize), edgesize + (3 * piecesize)))

pieceimage = Image.open('images_input/whiterookonblack.jpg', mode='r')
pieceimage.convert('RGB')
boardimage.paste(pieceimage, (edgesize + (2 * piecesize), edgesize + (5 * piecesize)))

boardimage.save('images_output/image.png')
