# -*- coding: utf-8 -*-
"""
Created on Thu Feb  2 14:10:49 2023

@author: ADMIN
"""
'''
import ftplib
ftp = ftplib.FTP('127.0.0.1')
ftp.login('DungNguyen','1')
data=[]
ftp.dir(data.append)
ftp.quit()
for i in data:
    print(i)
    '''

'''

import ftplib
ftp = ftplib.FTP('127.0.0.1')
ftp.login('DungNguyen','1')
ftp.encoding='utf-8'
filename = 'testLTM.txt'
with open(filename,'rb') as f:
    ftp.storbinary(f'STOR {filename}',f)
    '''
import netifaces
def get_interfaces():

    interfaces = netifaces.interfaces()
    

    out_interfaces = dict()

    for i in interfaces:
        addrs = netifaces.ifaddresses(i)
        out_addrs = dict()
        if netifaces.AF_INET in addrs.keys():
            out_addrs["ipv4"] = addrs[netifaces.AF_INET]
        if netifaces.AF_INET6 in addrs.keys():
            out_addrs["ipv6"] = addrs[netifaces.AF_INET6]
        out_interfaces[i] = out_addrs

    return out_interfaces

def get_ip4_broadcast_addresses():
    broadcast_addresses = []
    for i in netifaces.interfaces():
        ifaddresses = netifaces.ifaddresses(i)
        for ip in ifaddresses:
            if ip == netifaces.AF_INET:
                address_info = ifaddresses[ip]
                for info in address_info:
                    if "broadcast" in info:
                        broadcast_addresses.append(info['broadcast'])
    
    return broadcast_addresses

if __name__ == '__main__':
    print(get_interfaces())
    #print(get_ip4_broadcast_addresses())

