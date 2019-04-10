from PIL import Image
from pylab import *  # 调用pylab

# 读取图片
img = Image.open(r'C:\Users\Tupeng\Desktop\lena.jpg')

# 输出图片的格式，尺寸以及图像类型
print(img.format, img.size, img.mode)
# 显示
imshow(img)
show()
figure()
# 保存
img.save(r'C:\Users\Tupeng\Desktop\lena2.jpg', 'JPEG')
