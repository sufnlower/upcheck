# upcheck
Small wrapper around nmap. Port scans a network and concisely reports which machines are up with available info.
The point of this tool is to display the results, one target machine per line.

```
usage: UpCheck.py [-h] [-n NETWORK] [-p PORTS] [-s]

optional arguments:
  -h, --help            show this help message and exit
  -n NETWORK, --network NETWORK
                        Network to scan in CIDR or something nmap likes
  -p PORTS, --ports PORTS
                        Ports like nmap takes them. Defaults to 80,443,22,445,88.
  -s, --showmisses      Use if you want to see hosts where nothing suggesting up
                        was detected.
  -sT, --useconnectscan
  			Use a connect scan, good for SOCKS proxy
```
