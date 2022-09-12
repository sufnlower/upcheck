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
    parser.add_argument('-sT','--useconnectscan', action="store_true", help="Use a connect scan, good for SOCKS proxy")
    args = parser.parse_args()
    
    connect = ''
    if(args.useconnectscan):
    	cmd = ['nmap',f'{args.network}','-Pn','-p',f'{args.ports}','-sT']
    else:
    	cmd = ['nmap',f'{args.network}','-Pn','-p',f'{args.ports}']
    print("Running the nmap command...")
    nmap_out = subprocess.Popen(cmd, 
                stdout=subprocess.PIPE, 
                stderr=subprocess.STDOUT)
    nmap_out.wait()
    stdout,stderr = nmap_out.communicate()
    
    stdoutStr = str(stdout)

    targets = stdoutStr.split("Nmap scan report for ")

    for target in targets[1:]:
        ip = target[:target.index("\\n")]
        results = target[target.index("SERVICE\\n")+9:]
        result_lines = results.split("\\n")
        openPorts = []
        closedPorts = []
        unfilteredPorts = []
        for line in result_lines:
        	if "open" in line:
        		openPorts.append(line[:line.index("/")])
        	if "closed" in line:
        		closedPorts.append(line[:line.index("/")])
        	if "unfiltered" in line:
        		unfilteredPorts.append(line[:line.index("/")])
        if len(openPorts) + len(closedPorts) + len(unfilteredPorts) != 0:
        	print(f"{ip} appears up due to the following: Open {openPorts}. Closed {closedPorts}. Unfiltered {unfilteredPorts}")
        else:
            if(args.showmisses):
                print(f"Nothing detected for {ip}")
       
    if stderr != None:
        print(stderr)

if __name__ == "__main__":
    main()
