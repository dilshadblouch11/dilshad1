#!/usr/bin/python2
#coding=utf-8
#The Credit For This Code Goes To dilshad jamali
#If You Wanna Take Credits For This Code, Please Look Yourself Again...
#Reserved2020


import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib,requests,mechanize
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser


reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]


def keluar():
	print "\x1b[1;91mExit"
	os.sys.exit()


def acak(b):
    w = 'ahtdzjc'
    d = ''
    for i in x:
        d += '!'+w[random.randint(0,len(w)-1)]+i
    return cetak(d)


def cetak(b):
    w = 'ahtdzjc'
    for i in w:
        j = w.index(i)
        x= x.replace('!%s'%i,'\033[%s;1m'%str(31+j))
    x += '\033[0m'
    x = x.replace('!0','\033[0m')
    sys.stdout.write(x+'\n')


def jalan(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.01)
##### LOGO #####
logo = """
\033[1;96m
\033[1;96m
\033[1;96m
\033[1;96m
\033[1;96m
\033[1;96m
░DILSHAD Ali JAMALI        ██═══╝░╚═╝░░╚═╝
\033[1;96m
\033[1;96m
\033[1;96m
\033[1;96m
\033[1;96m
                     
          Arial ASCII Art
Image:    prev  next patorjk.com
¤´¯`·.¸.·•´¯`•·.¸¸.·´ Ýôgi ßëår `·.¸¸.·•´¯`•·.¸.·´¯`¤. 
                         ƒôr                       •Å(V)åö 
         ;' ·,       ,         GANOOK98         •98• 
         ;     '·, ,'·,  ' ·, 
         ',       ,'   ' ·,    ' ·, 
  , · " " ·,     :',       '·,      ' · ,          ,   ·  ' ; 
,"::' ·,::   ", ,':::' ,       ' · ,   ,  ,' ·  '            ; 
¦::                 ' ··,:::::':·,......  , ' 
",:::      ,":::::          ' ··,::,::,'_._._._._._._._._._', 
         ,"::::::          ´   , "      „ „",  ,"      „ „', 
        ,"::::                 ;     „"   ,"   ;     „"  ," 
        ;::::                   "„    ", "     ",  „ "„ " ; 
        ;:::       , "  "   "   "   "     „"·::::::::::::::"„- , 
        ;::      ,"                         "„·:::::::::::::·„" 
        ;::      ;                             "„·:::::::„" 
        ",::    ;         ,·'                       ", " 
          ",::   ",       '·,         ˆ ·,         ,·'    ,ˆ 
            ",::   ",                     ˆ · , ,' , · ˆ    ," 
            _",:::   ",_._._._._._._.      _._._ ," 
          ,'                             ,":::",          ', 
        ,'                            ,"::::::::",          ', 
       ,'                           ,' ",::::::::,",          ', 
      ,',.,. ,.,.,.,.,.,.,.,.,.,.,.,"   "::::"    ", 
         ,":::::                       ,":::",        º² "Jamali
       ,":::                          ,"::::::",            ", 
      ,"::                          ,":::::::::",            ", 
     ,"::                          ,":::::::::::",            ", 
        ‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹«•š
     
  

   |___'|.·´    Dilshad JaMali    -«
\033[1;97m:•◈•▬ ▬ ▬ ▬ ▬ ▬ ▬ •◈•\033[1;94mdilshadjamali\033[1;97m•◈•▬ ▬ ▬ ▬ ▬ ▬ ▬•◈•
\033[1;96m:•◈•╔╗─────────╔╗───────╔╗
\033[1;96m:•◈•
\033[1;96m:•◈•
\033[1;96m:•◈•
\033[1;96m:•◈•
\033[1;96m:•◈•
\033[1;97m:•◈•▬ ▬ ▬ ▬ ▬ ▬ ▬ •◈•\033[1;94mdilshadjamali\033[1;97m•◈•▬ ▬ ▬ ▬ ▬ ▬ ▬ •◈•
		print("\r\x1b[1;93mPlease Wait \x1b[1;93m"+o),;sys.stdout.flush();time.sleep(1)


back = 0
successfull = []
checkpoint = []
oks = []
id = []
