# DECRYPTED BY xXx_not_found_xXx
# Github : https://github.com/hamalord4444
 # uncompyle6 version 3.7.4
# Python bytecode 2.7
# Decompiled from: Python 2.7.18 (default, Aug  8 2021, 22:51:48) 
# [GCC 4.2.1 Compatible Android (6454773 based on r365631c2) Clang 9.0.8 (https:/
# Embedded file name: <tegarid>
import os
from time import sleep
a = '\x1b[92m'
b = '\x1b[91m'
c = '\x1b[0m'
os.system('figlet Sidra ')
print '\x1b[92m================================='
print '\x1b[93m Author   :\x1b[92mSidra ELEzz'
print '\x1b[93m YouTube  : \x1b[92mTermux Tools'
print '\x1b[93m Telegram : \x1b[92mhttps://t.me/TT_RQ'
print '\x1b[92m================================='
print '\nProses..'
sleep(1)
print b + '\n[!] making termux properties directory..'
sleep(1)
try:
    os.mkdir('/data/data/com.termux/files/home/.termux')
except:
    pass

print a + '[!]Success !'
sleep(1)
print b + '\n[!] Making setup file..'
sleep(1)
key = "extra-keys = [['ESC','/','-','_','UP','<','>'],['TAB','CTRL','ALT','LEFT','DOWN','RIGHT','PGDN']]"
kontol = open('/data/data/com.termux/files/home/.termux/termux.properties', 'w')
kontol.write(key)
kontol.close()
sleep(1)
print a + '[!] Success !'
sleep(1)
print b + '\n[!] Setting up..'
sleep(2)
os.system('termux-reload-settings')
print a + '[!] Successfully !! ^^' + c + '\\Sidra ELEzz\nThanks :*\n\n'