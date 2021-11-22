# tor-traffic-crawler

# Quick Start

## First, start the tor service, and listen at socket 9150.
$bash ./path_to_tbb/firefox  #if you download tbb.tar.xz from TOR project.

## Second 
$python crawler

## You can find all .pcap at results/

## It is recommanded to use the [docker image](https://registry.hub.docker.com/r/sunxueliang96/tor-traffic-crawler). 


## The screenshot
![screenshot](https://github.com/sunxueliang96/tor-traffic-crawler/blob/main/snap_shot/snap_shot.png)

# The Description of FILES
### crawler.py
The core of crawler

### meta_visit.py
Launch one visit to one site

### setting.py
All configs

### visit.py
Launch a set of visits

### parse.py
You must code your own parse script
