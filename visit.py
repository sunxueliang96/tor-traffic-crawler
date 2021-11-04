import subprocess
from setting import *
from utils import get_pid_firefox, vist_logger
import time 
import random


class Visit():
    def __init__(self): #urls->lists
        self.tbb_dir = tbb_dir
        #the time sleep between the tabs visit
        self.gap_between_tabs = gap_between_tabs
        self.gap_between_visits = gap_between_visits
        #prepare the tor socket and keep the pid
        self.protected_pid = get_pid_firefox()

    def visits(self,urls): 
        #random choose the time gap
        time_gaps = []
        for gap in urls:
            gap = random.randint(self.gap_between_tabs[0],self.gap_between_tabs[1])
            time_gaps.append(gap+base_gap)
        time_gaps = time_gaps[:-1]
        time_gaps.append(self.gap_between_visits)
        vist_logger(str(urls) + str(time_gaps))
        processes = []
        for url,gap in zip(urls,time_gaps):
            print("loading the "+str(url)+" and then sleep " + str(gap))
            processes.append(subprocess.Popen(['python','meta_visit.py',url]))
            time.sleep(int(gap))
        #time to kill ext firefox.real but keep the sockets 
        pid_now = get_pid_firefox()
        for pid in pid_now:
            if pid not in self.protected_pid:
                subprocess.Popen(['kill',pid])
                print(pid + 'is killed')
        
urls = ['https://www.google.com','http://www.facebook.com','http://www.wikipedia.org']
urls1 = ['http://www.amazon.com','http://www.bing.com']
test = Visit()
test.visits(urls)
test.visits(urls1)
#vist_logger("dsafdsa")

