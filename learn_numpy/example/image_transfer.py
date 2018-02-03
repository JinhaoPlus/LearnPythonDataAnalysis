import numpy as np
from PIL import Image

print(Image.open("/Users/jinhaoplus/Desktop/pic.jpg", 'r'))
im = np.array(Image.open("/Users/jinhaoplus/Desktop/pic.jpg", 'r'))
# im = np.array(Image.open("/Users/jinhaoplus/Desktop/ppp.png", 'r'))
print(im.shape, im.dtype)
print(im)

trans_im = [255, 255, 255] - im
trans = Image.fromarray(trans_im.astype('uint8'))
trans.save("/Users/jinhaoplus/Desktop/trans_pic.jpg")

a = np.array(Image.open("/Users/jinhaoplus/Desktop/pic.jpg", 'r').convert('L'))
print(a.shape, a.dtype)
print(a)
b = 255 - a
transs = Image.fromarray(b.astype('uint8'))
transs.save("/Users/jinhaoplus/Desktop/l_pic.jpg")
