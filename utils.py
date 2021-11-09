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

def parse_logger(content):
    localtime = time.asctime(time.localtime(time.time()))
    with open(parse_log_path,'a+') as f:
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

def start_capture(labels,time_gaps,counts):
    #get labels of urls first
    labels = '_'.join(labels)
    time_gaps = '_'.join(list(map(str,time_gaps)))

    cmd = 'sudo tshark -w '+ capture_path +'/'+ labels + '-' + time_gaps + '-' + counts + '.cap -i any -f "port '+ str(sniff_port )+ '"'
    tshark = subprocess.Popen(cmd,stdout=subprocess.PIPE,shell=True)
    return tshark

def stop_capture(process):
    pids = get_pid('tshark')
    for pid in pids:
        cmd1 = "sudo kill -9 %s" % pid# . # -9 to kill force fully
        os.system(cmd1)
    if (process.wait())==-9 : # this will print -9 if killed force fully, else -15.
       print('tshark killed force fully')

    cmd_chmod = 'sudo chmod -R 777 '+ capture_path
    chmod = subprocess.Popen(cmd_chmod,stdout=subprocess.PIPE,shell=True)

def get_pid(name):
    try:
        pids = subprocess.check_output(["pidof",name]).split()
        pids_1 = []
        [pids_1.append(int(pid)) for pid in pids]
        return pids_1
    except:
        return [999999]#non-exit pid


