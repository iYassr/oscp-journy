# OSCP Journy - Yasser 
in the name of Allah, the most gracful the most merciful  
2019-05-20 23:43:53

## Table of Content






Linux 
==========================
- ssh
  - ssh tunnel listen on port 8888, quiet, compression, no command execution, background   
  `sudo ssh -D 8888 -f -C -q -N root@$ip`
  - enable X11 on WSL  
    - install vcxsrv
    - `export DISPLAY=localhost:0.0`
- networking
  - set dhcp 
    - /etc/network/interfaces  
     `` auto eth0   
    iface eth0 inet dhcp/static``
- find files modfied last 60 min  
 ` find / -cmin 60 `  
- use vim bindings terminal  
  `set -o vi`







Windows 
==========================


Enumration 
==========================

Port Scanning 
------------------------

- ping scan  
`nmap -sP $ip`
- no reverse dns lookup  
`nmap -n $ip`
- ICMP Echo, timestamp, network mask request discovery
`nmap -PE/PP/PM $ip`
- Syn Packet Discovery   
`nmap -PS  $ip`
- Ack Packet Discovery  
`nmap -PA  $ip`
- TCP Scan most common 3574 ports   
`nmap -sT --top-ports 3674 $ip`
- UDP Scan most common 1017 ports   
`nmap -sU --top-ports 1017 $ip`
- Spoof source address, works with tcp? don't no  
`nmap -S 10.10.10.10 $ip`
- debugging mode, every info you need  
`nmap -d $ip`
- filtered, why?   
`nmap --reason $ip` 
- which host responded? is it the same host or the firewall?   
`nmap --packet-trace $ip`
- change source port, use DNS for ex to bypass some firewalls  
` nmap --source-port 53 $ip`

- good mass scan from external  
`nmap -sP -PE -PS21,22,23,25,80,113,31339,443,445,3389,111 -PA80,113,44,10042 --source-port 53 -iL ips.txt`


- SSH
- DNS
- SMTP
- POP3
- Netbios 
- SMB
- NFS
- RPC
- SMTP
- SNMP
- HTTP



Buffer Over Flow 
==========================


Privilege Escalation
==========================



VMware
==========================
- mount shared_folder  
    - windows 
    `sudo vmhgfs-fuse .host:/ /root/shared_folder -o allow_other -o uid=1000`
    - linux  
    `sudo vmhgfs-fuse .host:/ /mnt/hgfs/ -o allow_other -o uid=1000`