from setting import *
from utils import vist_logger
from visit import Visit
import random
import subprocess
from xvfbwrapper import Xvfb
import time 
import os 


class Crawler():
    def __init__(self):
        self.mon_websites_path = mon_websites_path
        self.NB_of_tabs = NB_of_tabs
        self.NB_of_samples = NB_of_samples
        #clean the logs
        subprocess.Popen(['echo start','>',visit_log_path])
        subprocess.Popen(['echo start','>',geckodriver_log_path])
        subprocess.Popen(['echo start','>',parse_log_path])

    def read_mon_websites(self):
        with open(self.mon_websites_path,'r') as f:
            mon_websites = f.read().splitlines() 
        return mon_websites

    def crawler_CW(self):
        #start a new batch at each batch
        p_firefox = subprocess.Popen([tbb_dir+'/Browser/firefox','--headless'])
        vist_logger('[TBB] A New TBB started ')
        time.sleep(25)
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
                os.system('python3 parse.py')
        p_firefox.kill()
        #start a new batch at each batch
        vist_logger('[TBB] The TBB ended ')

    def crawler_OW(self):
        pass
    
vdisplay = Xvfb(width=1920, height=1080)
vdisplay.start()
for i in range(NB_of_batches):
    a = Crawler()
    a.crawler_CW()
vdisplay.stop()