from PIL import Image
import numpy as np

from sklearn import linear_model
import matplotlib.pyplot as plt

im = Image.open('C:/Users/MAGI/Desktop/image.JPG')
data=np.array(im.getdata()).reshape([im.height,im.width,3])

x = np.arange(0, im.width)
X = np.array([x, x**2.0, x**3.0, x**4.0, x**5.0]).transpose()

y = data[0, :, 2]

b = data[0, :, 2]
g = data[0, :, 1]
r = data[0, :, 0]

plt.plot(r,'-r',g,'-g',b,'-b')

lm = linear_model.LinearRegression()
lm.fit(X, y)
predicted = lm.predict(X)

bits_per_channel = 3
#1 bit fo minus or plus
# 4 => 3 bits for colors 2^3 = 8
threshold = 2**(bits_per_channel-1)-1

newData=np.clip(-threshold,threshold,data)


diff = y - predicted
diff = np.clip(diff, -threshold, threshold)

y = predicted + diff
y = np.clip(np.round(y), 0, 255)

mas = [[0]*3 for i in range(im.height)]
for i in range(im.height):
    for j in range(3):
            y = data[i, :, j]
            lm = linear_model.LinearRegression()
            lm.fit(X, y)
            predicted = lm.predict(X)
            diff = y - predicted
            diff = np.clip(diff, -threshold, threshold)
            y = predicted + diff
            y = np.clip(np.round(y), 0, 255)
            mas[i][j] = y.astype(int)

pix = im.load()
for i in range(im.height):
    for j in range(im.width):
        for k in range(3):
            _list = list(pix[j, i])
            _list[k] = mas[i][k][j]
            pix[j, i] = tuple(_list)


im.save('ready.png')







