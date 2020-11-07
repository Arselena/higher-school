import os
from glob import glob
from PIL import Image, ImageDraw, ImageColor, ImageFont

def convert(ext1, ext2):
    List = glob('*.' + ext1)
    for im in List:
        im_name = os.path.splitext(im)[0]  # Имя без расширения
        with Image.open(im) as im_tmp:
            #im_tmp.save((im_name + '.' + ext2), "JPEG")
            im_tmp.convert('RGB').save(im_name + '.' + ext2, "JPEG")

def draw_rectangle(im):
    with Image.open(im) as im_tmp:
        draw = ImageDraw.Draw(im_tmp)
        sz = im_tmp.size # Размер изображение
        H = 250 # Размер квадрата
        sq_sz = [sz[0]/2-H,sz[1]/2-H, sz[0]/2+H,sz[1]/2+H] # Координаты квардата
        draw.rectangle(sq_sz, outline="red", width=5) # Рисуем красный квадрат
        my_font = ImageFont.truetype("arial", 64) # Шрифт и размер текста
        draw.multiline_text((sq_sz[0]+H/2,sq_sz[1]+H/2), 'Hello,\nWorld', \
                             fill=30, font=my_font, align="center")
        im_tmp.save('test2.jpg')  # Схраняем файл
        del draw # Удаляем холст
        im_tmp.show() # Выыводим на экран

os.chdir(r'C:\Users\work-pc\Desktop\Python')
convert('png', 'jpg')
draw_rectangle('test.jpg')