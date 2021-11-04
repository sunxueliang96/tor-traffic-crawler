from tbselenium.tbdriver import TorBrowserDriver
from setting import *
import sys


url = sys.argv[1]
driver = TorBrowserDriver(tbb_dir,socks_port=9150,control_port=9151,tbb_logfile_path=geckodriver_log_path,executable_path=geckodriver_path)
driver.load_url(url)

