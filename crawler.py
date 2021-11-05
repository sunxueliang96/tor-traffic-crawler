from setting import *
from visit import Visit
import random

class Crawler():
    def __init__(self):
        self.mon_websites_path = mon_websites_path
        self.NB_of_tabs = NB_of_tabs
        self.NB_of_samples = NB_of_samples
    def read_mon_websites(self):
        with open(self.mon_websites_path,'r') as f:
            mon_websites = f.read().splitlines() 
        return mon_websites

    def crawler_CW(self):
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
    
a = Crawler()
a.crawler_CW()