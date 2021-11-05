import subprocess
from setting import *
from utils import *
import time 
import random


class Visit():
    def __init__(self): #urls->lists
        self.tbb_dir = tbb_dir
        #the time sleep between the tabs visit
        self.gap_between_tabs = gap_between_tabs
        self.gap_between_visits = gap_between_visits
        #prepare the tor socket and keep the pid safe
        self.protected_pid = get_pid_firefox()
        self.capture_path = capture_path
        self.sniff_port = sniff_port


    def visits(self,urls,labels,counts): 
        #random choose the time gap
        time_gaps = []
        for gap in urls:
            gap = random.randint(self.gap_between_tabs[0],self.gap_between_tabs[1])
            time_gaps.append(gap+base_gap)
        time_gaps = time_gaps[:-1]
        time_gaps.append(self.gap_between_visits)
        vist_logger(str(urls) + str(time_gaps))
        #start traffic capture
        p_tshark = start_capture(labels,time_gaps,counts)
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
                #print(pid + 'is killed')
        print('all Tor Browsers are killed')
        #kill tshark
        stop_capture(p_tshark)
#for test 
#urls = ['https://www.google.com','http://www.facebook.com','http://www.wikipedia.org']
#urls1 = ['http://www.amazon.com','http://www.bing.com']
#test = Visit()
#test.visits(urls,['0','1','2'])
#test.visits(urls1,['3','4'])
