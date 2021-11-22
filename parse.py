from scapy.all import *
import pyshark
from setting import *


threshold = 511

def get_directions(pkt):
    src = pkt[IP].src
    #if src == '8.8.8.8':
    #	return 'sp'
    if src[:3]=='172':
        #send = -1
        return -1
    else:
        #recv = -1 
        return 1

def write_to_file(f,time,direc,size):
    f.writelines(str(time))
    f.writelines('\t')
    f.writelines(str(direc))
    f.writelines('\t')
    f.writelines(str(size))
    f.writelines('\n')

def read_tls(pcap_target):

    packets = rdpcap(pcap_target)
    flags = []
    tls_reader = pyshark.FileCapture(pcap_target)
    [flags.append(str(p.layers)) for p in tls_reader]
    tls_reader.close()

    #tls_reader.set_debug()
    first_pkt = packets[0]
    start_time = float(first_pkt.time)
    counts_packet_del = 0
    counts_packet_nottls = 0

    f = open(pcap_target+'.cell','w')

    for packet,flag in zip(packets,flags):
        #print(flag)
        #if('SSL Layer' or 'TLS Layer' in flag):
        size = len(packet)
        if '8.8.8.8' in packet:
            write_to_file('split_point\n')
        if size<=88:
            counts_packet_del = counts_packet_del + 1
        else:
            try:
                time = float(packet.time) - start_time
                direc = get_directions(packet)
                #print(time,direc,size)
                #for i in range(int(size/threshold)):
                write_to_file(f,time,direc,size)
            except:
                pass
    f.close()
    print('{} tcp packets ({}%) are droped'.format(counts_packet_nottls,round(100*counts_packet_nottls/len(packets),2)))
    num_res = len(packets)-counts_packet_nottls
    print('{} tls records ({}%) droped beacuse of less than threshold in {}'.format(counts_packet_del,round(100*counts_packet_del/num_res,2),pcap_target))
def parse_all_pcaps():
    pcaps = os.listdir(capture_path)
    for pcap in pcaps:
        try:
            target = capture_path+'/'+pcap
            #print(target)
            if 'cell' not in target:
                print('parsing and moving' + target)
                read_tls(target)
                os.system('rm '+target)#+' ./pcaps')
        except:
            #palce holder
            pass
parse_all_pcaps()
#read_tls('results/0_81-22_20-1.cap')
