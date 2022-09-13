# upcheck
Small wrapper around nmap. Port scans a network and concisely reports which machines are up with available info.
The point of this tool is to display the results, one target machine per line.

You can achieve the same thing by outputting nmap results and grepping so this tool is a little redundant.
```
nmap 10.10.10.0/24 -p 80,139,443,22,445,88 -oA output
cat output.gnmap | grep -E "open|unfiltered|closed" | cut -d "(" -f 1 | sed 's/Host: //g'
```

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
