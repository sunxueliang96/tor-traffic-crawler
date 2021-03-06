
#the path to TBB firefox
tbb_dir = '/root/tor_crawler/tor-browser_en-US'
geckodriver_path = '/root/tor_crawler/geckodriver'
mon_websites_path = './targets/alexa_top_100.txt'

#the path to the logs
visit_log_path = '/root/tor_crawler/logs/visit_log.txt'
geckodriver_log_path = '/root/tor_crawler/logs/firefox.txt'
parse_log_path = '/root/tor_crawler/logs/parse.txt'
#path to cap results
capture_path = './results'

#visit setting
gap_between_tabs = [1,10]
gap_between_visits = 20
base_gap = 15 #base time for lanunching browser
sniff_port = 9150

#crawler setting
NB_of_tabs = 2
NB_of_samples = 4
NB_of_batches = 20
