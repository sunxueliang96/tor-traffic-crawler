# log to file
import time
import os
from setting import *
import subprocess


def capture_logger(file_name):
    localtime = time.asctime( time.localtime(time.time()) )
    fsize = os.path.getsize(file_name)
    f_kb = fsize/float(1024)
    with open('logs/log_successed.txt','a') as f:
        f.write(str(localtime)+' '+str(f_kb)+'kb saved in '+ str(file_name)+'\n')

def vist_logger(content):
    localtime = time.asctime(time.localtime(time.time()))
    with open(visit_log_path,'a+') as f:
        print((str(localtime)+' '+str(content)+' \n'))
        f.write(str(localtime)+' '+str(content)+' \n')

#return the pid of firefox.real -> list
def get_pid_firefox():
    p = subprocess.Popen(['pidof', 'firefox.real'],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            )
    p.wait()
    out = p.stdout.read()
    out = out[:-2].split(' ')
    #print(out)
    return out