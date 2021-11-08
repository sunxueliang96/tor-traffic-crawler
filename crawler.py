from setting import *
from utils import get_pid_firefox
from visit import Visit
import random
import subprocess
from xvfbwrapper import Xvfb
import time 

class Crawler():
    def __init__(self):
        self.mon_websites_path = mon_websites_path
        self.NB_of_tabs = NB_of_tabs
        self.NB_of_samples = NB_of_samples
    def read_mon_websites(self):
        with open(self.mon_websites_path,'r') as f:
            mon_websites = f.read().splitlines() 
        return mon_websites
    def restartTBB(self):
        #kill all tbb firstly.
        pid_now = get_pid_firefox()
        for pid in pid_now:
            subprocess.Popen(['kill',pid])
        print('all Tor Browsers are killed')
        #start the TBB at default port
        subprocess.Popen([tbb_dir+'/Browser/firefox','--headless'])
        time.sleep(25)
        print('Sleep 25 sec for waiting TBB launching')
    def crawler_CW(self):
        self.restartTBB()
        mons = self.read_mon_websites()
        for target in mons:
            urls = []
            labels = []
            urls.append(target)
            labels.append(str(mons.index(target)))
            for i in range(self.NB_of_tabs-1):
                new_tab = random.choice(mons)
                urls.append(new_tab)
                labels.append(str(mons.index(new_tab)))
            mon_visit = Visit()
            for count in range(self.NB_of_samples):
                mon_visit.visits(urls,labels,str(count))
            #print(urls)
            #print(labels)

    def crawler_OW(self):
        pass
    
vdisplay = Xvfb(width=1920, height=1080)
vdisplay.start()
a = Crawler()
a.crawler_CW()
vdisplay.stop()