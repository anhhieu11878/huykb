# Tool By S-TOOl
luc = "\033[1;32m"
trang = "\033[1;37m"
red = "\033[1;31m"
yellow = "\033[0;93m"
lightblue = "\033[1;35m"
xduong = "\033[1;34m"
xnhac = "\033[1;36m"
purple = "\e[35m"
hong = "\033[1;95m"
# Đánh dấu bản quyền
thanh_xau= trang + "~" + red + "[" + luc + "●" + red + "] " + trang + "➩ "
thanh_dep= trang + "~" + red + "[" + luc + "✓" + red + "] " + trang + "➩ "
# useragent
useragent = 'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/12.1 Chrome/79.0.3945.136 Mobile Safari/537.36'
# import lib
import requests, os, sys
from sys import platform
from datetime import datetime        
from time import sleep,strftime
from pystyle import Colors, Colorate
try:
	import requests
except:
	print (luc + "Bạn Chưa Tải Thư Viện \n Bắt Đầu Tải ")
	os.system("pip install requests")
# ==========================[ FUNCTION ]===========================================
banners = f"""
        ███████╗   ████████╗ ██████╗  ██████╗ ██╗
        ██╔════╝   ╚══██╔══╝██╔═══██╗██╔═══██╗██║
        ███████╗█████╗██║   ██║   ██║██║   ██║██║
        ╚════██║╚════╝██║   ██║   ██║██║   ██║██║
        ███████║      ██║   ╚██████╔╝╚██████╔╝███████╗
        ╚══════╝      ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝
"""
# in
def echo(text):
    for i in range(len(text)):
       sys.stdout.write(text[i])
       sys.stdout.flush()
       sleep(0.001)
    print()
#clear
def clear ():
    if platform[0:3] == 'lin':
        os.system("clear")
    else:
	    os.system("cls")
# banner
def banner ():
    global banners
    clear()
    print(Colorate.Horizontal(Colors.blue_to_white, banners))
    echo(yellow+"@PowerByS-TOOL")
    echo(trang + "= "*30)
    echo(thanh_xau + hong + "TOOL AUTO HỦY LỜI MỜI KẾT BẠN")
    echo(thanh_xau + yellow + "Bản Quyền:" + xduong + " S-TOOl ")
    echo(thanh_xau + luc + "Admin: "+ xnhac + "Sói Con ")
    echo(thanh_xau + red + "Viết Code Theo Yêu Cầu LH Zalo: " + xduong + "0765826980")
    echo(trang + "= "*30)
#delay
def nghingoi(delay):
    for x in range(delay,0,-1):
        print ("\r\033[1;93m   S-TOOl \033[1;91m ~>       \033[1;92m LO           \033[1;91m | " + str(x) + " |              \r", end='')
        sleep(0.2)
        print ("\r\033[1;91m   S-TOOl \033[1;91m ~>       \033[1;92m LOA          \033[1;91m | " + str(x) + " |              \r", end='')
        sleep(0.2)
        print ("\r\033[1;92m   S-TOOl \033[1;91m ~>       \033[1;92m LOAD         \033[1;91m | " + str(x) + " |              \r", end='')
        sleep(0.2)
        print ("\r\033[1;95m   S-TOOl \033[1;91m ~>       \033[1;92m LOADI        \033[1;91m | " + str(x) + " |              \r", end='')
        sleep(0.2)
        print ("\r\033[1;96m   S-TOOl \033[1;91m ~>       \033[1;92m LOADIN       \033[1;91m | " + str(x) + " |              \r", end='')
        sleep(0.2)
        print ("\r\033[1;92m   S-TOOl \033[1;91m ~>       \033[1;92m LOADING      \033[1;91m | " + str(x) + " |              \r", end='')
        sleep(0.2)
    print ("\r\033[1;95m  SÓI CON                                  \r", end='')
    sleep(0.5)
# =================[ START ]===========================
banner ()
cookie = input(thanh_xau + luc + "Nhập Cookie Facebook: " + yellow)
delay = int(input(thanh_xau + luc + "Nhập Delay: " + yellow))
head = {
    'host'           : 'mbasic.facebook.com',
    'accept'         : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-language': 'en-US,en;q=0.9',
    'connection'     : 'keep-alive',
    'user-agent'     : useragent,
    'cookie'         : cookie
}
echo(trang + "= "*30)
dem = 0
while True:
    list = requests.get('https://mbasic.facebook.com/friends/center/requests/outgoing/', headers = head).text
    list2 = list.split('/a/friendrequest/cancel/?subject_id=')
    for data in list2:
        check = data.split('"')[0]
        if '100' in check[0:15]:
            dem += 1
            link = check.replace("amp;", "")
            id = link.split('&')[0]
            huy = requests.get('https://mbasic.facebook.com/a/friendrequest/cancel/?subject_id=' + link, headers = head).text
            print ("\r\033[1;32m⌠\033[1;33mS-TOOL\033[1;32m⌡\033[1;35m❯\033[1;36m❯\033[1;31m❯\033[1;34m[\033[1;33m" + str(dem) + "\033[1;34m]\033[1;91m ● \033[1;36m" + xnhac + datetime.now().strftime("%H:%M:%S") + red + " ● " + luc + "HỦY LỜI MỜI" + red + " ● " + luc + str(id))
            nghingoi(delay)