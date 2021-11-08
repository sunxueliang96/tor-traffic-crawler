# tor-traffic-crawler

# Quick Start

## First, start the tor service, and listen at socket 9150.
$bash ./path_to_tbb/firefox  #if you download tbb.tar.xz from TOR project.

## Second 
$python crawler

## You can find all .pcap at results/


## The screenshot
![screenshot](https://github.com/sunxueliang96/tor-traffic-crawler/blob/main/snap_shot/snap_shot.png)

# The Description of FILES
crawler.py
### the core of crawler

meta_visit.py
### launch one visit to one site

setting.py
### all configs

utils.py
### some utils/func

visit.py
### launch a set of visits
