# -*- coding:UTF-8 -*-
from PIL import Image
import sys

def mod(x,y):
    return x%y;

def toasc(strr):
 
    return int(strr, 2)

#le为所要提取的信息的长度，str1为加密载体图片的路径，str2为提取文件的保存路径
def func(le,str1,str2):
    a="" 
    b="" 
    im = Image.open(str1) 
    lenth = le*8
    width = im.size[0]
    height = im.size[1]
    count = 0
    for h in range(0, height): 
        for w in range(0, width):
             #获得(w,h)点像素的值
            pixel = im.getpixel((w, h))
            #此处余3，依次从R、G、B三个颜色通道获得最低位的隐藏信息 
            if count%3==0:
                count+=1
                b=b+str((mod(int(pixel[0]),2)))
                if count ==lenth:
                    break 
            if count%3==1:
                count+=1
                b=b+str((mod(int(pixel[1]),2)))
                if count ==lenth:
                    break 
            if count%3==2:
                count+=1
                b=b+str((mod(int(pixel[2]),2))) 
                if count ==lenth: 
                    break
        if count == lenth: 
            break
    with open(str2,"wb") as f: 
        flag = ''
        for i in range(0,len(b),8):
             #以每8位为一组二进制，转换为十进制
            stra = toasc(b[i:i+8])
            #将转换后的十进制数视为ascii码，再转换为字符串写入到文件中 
            flag += chr(stra)
            f.write(chr(stra)) 
            stra ="" 
    f.closed 
    print flag

if len(sys.argv)!=3:
    print 'Usage: ./this Stegano_PNG OutPut'
    sys.exit(2)
image_name = sys.argv[1]
tiqu = sys.argv[2]
#文件长度 
le = 80 

func(le,image_name,tiqu)