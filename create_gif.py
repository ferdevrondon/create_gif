import imageio.v3 as iio

filenames = ['cat_01.png','cat_02.png','cat_03.png','cat_4.png','cat_05.png','cat_06.png']
images = [ ]

for filename in filenames:
  images.append(iio.imread(filename))
  iio.imwrite('cats.gif', images, duration = 500, loop = 0)