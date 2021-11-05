
#the path to TBB firefox
tbb_dir = './tor-browser_en-US'
geckodriver_path = '/home/xmu/Desktop/tor_crawler/geckodriver'
mon_websites_path = './targets/alexa_top_100.txt'

#the path to the logs
visit_log_path = '/home/xmu/Desktop/tor_crawler/logs/visit_log.txt'
geckodriver_log_path = '/home/xmu/Desktop/tor_crawler/logs/firefox.txt'

#path to cap results
capture_path = './results'

#visit setting
gap_between_tabs = [1,10]
gap_between_visits = 20
base_gap = 15 #base time for lanunching browser
sniff_port = 9150

#crawler setting
NB_of_tabs = 2
NB_of_samples = 3