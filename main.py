import os
import sys

tools_dir = "tools/"
result_dir = "result/"
png_idat_check_dir = tools_dir + "png/png-idat-check.py"
lsb_dec_1_dir = tools_dir + "png/lsb_dec_1.py"
lsb_dec_jiami_dir = tools_dir + "png/cloacked-pixel-master/lsb.py"
outguess_dir = tools_dir + 'jpg/outguess'
password = ['123456','654321','admin','password']
stegdetect_dir = tools_dir + "jpg/stegdetect/stegdetect"
stegbreak_dir = tools_dir + "jpg/stegdetect/stegbreak"
F5_dir = tools_dir + "jpg/F5-steganography"
java_blind_water_mark_dir = tools_dir + "normal/BlindWatermark-v0.0.3-linux-x86_64.jar"

def show_tools():
    tools_list=os.listdir(tools_dir)
    print('共发现{}种工具：'.format(str(len(tools_list))))
    for i in tools_list:
        print(i)
    return tools_list

def foremost(target):
    print("\n\033[34m[+] Running foremost!\033[0m\n")
    os.system('foremost {} -T -o ./result/foremost_out'.format(target))
    print("\n\033[32m[-] Run foremost finish!\033[0m\n")

def png_idat_check(target):
    print("\n\033[34m[+] Running png_idat_check!\033[0m\n")
    os.system('python2 {} {}'.format(png_idat_check_dir,target))
    print("\n\033[32m[-] Run png_idat_check finish!\033[0m\n")

def IDAT_Chunk(target):
    print("\n\033[34m[+] Running IDAT Chunk check!\033[0m\n")
    os.system('pngcheck -v {}'.format(target))
    print("\n\033[32m[-] Run IDAT Chunk check finish!\033[0m\n")

def LSB_check(target):
    print("\n\033[34m[+] Running LSB check!\033[0m\n")
    os.system('zsteg {}'.format(target))
    print("\n\033[32m[-] Run LSB check finish!\033[0m\n")
    print("[+] 提取方法示例：zsteg -E \"b1,rgb,lsb,xy\" lsb-1.png > out.jpg \n")

def LSB_check_2(target):
    print("\n\033[34m[+] Running LSB check2!\033[0m\n")
    os.system('python2 {} {} {}'.format(lsb_dec_1_dir,target,result_dir+"lsbout-2"))
    print("\n\033[32m[-] Run LSB check2 finish!\033[0m\n")


# 带加密的lsb隐写
def LSB_jiami_check(target):
    print("\n\033[34m[+] Running LSB 加密 check!\033[0m\n")
    print("[+] LSB 加密隐写，正在准备爆破! \n")
    for i in password:
        print("\n[+] Trying {}".format(i))
        os.system('python2 {} extract {} {} {}'.format(lsb_dec_jiami_dir,target,result_dir+"lsb_jiami_out",i))
    print("\n\033[32m[-] Run LSB 加密 check finish!\033[0m\n")

def stegdetect(target):
    print("\n\033[34m[+] Running stegdetect check!\033[0m\n")
    os.system('{} -tjopi -s 10.0 {}'.format(stegdetect_dir,target))
    print("\n\033[32m[-] Run stegdetect check finish!\033[0m\n")

def stegbreak(target):
    print("\n\033[34m[+] Running stegbreak check!\033[0m\n")
    os.system('{} -r ./tools/jpg/stegdetect/rules.ini -f ./tools/jpg/stegdetect/password.txt -t p {}'.format(stegbreak_dir,target))
    print("\n[+] 这里只能提取出密码，jphide[v5](这里是密码)，请使用tool文件夹下的jphs05进行提取")
    print("\n\033[32m[-] Run stegbreak check finish!\033[0m\n")

# 带密码的outguess
def outguess(target):
    print("\n\033[34m[+] Running outguess check!\033[0m\n")
    print("[+] outguess 加密隐写，正在准备爆破! \n")
    os.system('{} -r {} {} ; cat {}'.format(outguess_dir,target,result_dir+"outguess_out",result_dir+"outguess_out"))
    for i in password:
        print("\n[+] Trying {}".format(i))
        os.system('{} -k {} -r {} {} ; cat {}'.format(outguess_dir,i,target,result_dir+"outguess_out",result_dir+"outguess_out"))
    print("\n\033[32m[-] Run outguess check finish!\033[0m\n")

def F5(target):
    print("\n\033[34m[+] Running F5 check!\033[0m\n")
    os.system('cd {} ; java Extract ../../../{} -e ../../../result/f5_out ; cat ../../../result/f5_out'.format(F5_dir,target))
    for i in password:
        print("\n[+] Trying {}".format(i))
        os.system('cd {} ; java Extract ../../../{} -p {} -e ../../../result/f5_out_{} ; cat ../../../result/f5_out_{}'.format(F5_dir,target,i,i,i))
    print("\n\033[32m[-] Run F5 check finish!\033[0m\n")

def java_blind_water_mark(target):
    print("\n\033[34m[+] Running stegdetect check!\033[0m\n")
    os.system('java -jar {} decode -c {} result/java_blind_out.jpg'.format(java_blind_water_mark_dir,target))
    print("\n[+] 解出的图片请去result目录查看! \n")
    print("\n\033[32m[-] Run stegdetect check finish!\033[0m\n")


def stegpy(target):
    print("\n\033[34m[+] Running stegpy check!\033[0m\n")
    print("[+] stegpy 加密隐写，正在准备爆破! \n")
    os.system('stegpy {}'.format(target))
    for i in password:
        print("\n[+] Trying {}".format(i))
        os.system('stegpy {} -p {}'.format(target,i))
    print("\n\033[32m[-] Run stegpy check finish!\033[0m\n")

def main(target):

    print("\033[33m[+] 正在分离图片\033[0m")

    foremost(target)
    input("\033[33m[+] Continue?\033[0m\n")

    print("\033[33m[+] 正在检查png图片类型隐写\033[0m")

    png_idat_check(target)
    input("\033[33m[+] Continue?\033[0m\n")

    IDAT_Chunk(target)
    input("\033[33m[+] Continue?\033[0m\n")

    LSB_check(target)
    input("\033[33m[+] Continue?\033[0m\n")

    LSB_check_2(target)
    input("\033[33m[+] Continue?\033[0m\n")

    LSB_jiami_check(target)
    input("\033[33m[+] Continue?\033[0m\n")

    print("\033[33m[+] 正在检查jpg图片类型隐写\033[0m")

    stegdetect(target)
    input("\033[33m[+] Continue?\033[0m\n")

    stegbreak(target)
    input("\033[33m[+] Continue?\033[0m\n")

    outguess(target)
    input("\033[33m[+] Continue?\033[0m\n")

    F5(target)
    input("\033[33m[+] Continue?\033[0m\n")

    print("\033[33m[+] 正在使用通用工具进行检查\033[0m")

    java_blind_water_mark(target)
    input("\033[33m[+] Continue?\033[0m\n")

    stegpy(target)
    input("\033[33m[+] Continue?\033[0m\n")

main(sys.argv[1])
