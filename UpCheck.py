#!/usr/bin/python3
import sys
import argparse
import subprocess
import re

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-n','--network', help="Network to scan in CIDR or something nmap likes")
    parser.add_argument('-p','--ports', default="80,443,22,445,88", help="Ports like nmap takes them. Defaults to 80,443,22,445,88.")
    parser.add_argument('-s','--showmisses', action="store_true", help="Use if you want to see hosts where nothing suggesting up was detected.")
    args = parser.parse_args()
    
    nmap_out = subprocess.Popen(['nmap',f'{args.network}','-Pn','-p',f'{args.ports}'], 
                stdout=subprocess.PIPE, 
                stderr=subprocess.STDOUT)
    nmap_out.wait()
    stdout,stderr = nmap_out.communicate()
    
    stdoutStr = str(stdout)

    targets = stdoutStr.split("Nmap scan report for ")

    for target in targets[1:]:
        ip = target[0:13]
        if "open" in target:
             print(f"{ip} appears up due to one of the scanned ports reporting open ({args.ports}).")
             continue
        if "closed" in target:
            print(f"{ip} appears up due to one of the scanned ports reporting closed ({args.ports}).")  
            continue    
        if "unfiltered" in target:
            print(f"{ip} appears up due to one of the scanned ports reporting unfiltered ({args.ports}).")          
        else:
            if(args.showmisses):
                print(f"Nothing detected for {ip}")
       
    if stderr != None:
        print(stderr)

if __name__ == "__main__":
    main()
