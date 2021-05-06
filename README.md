CTF中常见隐写方法的自动化检测

欢迎各位dalao提供新的想法！

环境测试使用ubuntu18.04

## 需要安装的环境

* python2
* python3
* java
* foremost

* zsteg

```bash
# ubuntu安装zsteg
apt install tcllib
apt install ruby
apt install gem
gem install zsteg
```

* pngcheck

```bash
apt install pngcheck
```

* stegpy

```
pip3 install stegpy
```

## 使用方法

```
python3 main.py xxx.jpg
```

## 已经适配的隐写方法

- [x] foremost
- [x] png_idat_check
- [x] pngcheck
- [x] zsteg
- [x] 某lsb隐写脚本
- [x] lsb加密隐写
- [x] stegdetect
- [x] stegbreak
- [x] outguess
- [x] F5
- [x] java盲水印
- [x] stegpy





