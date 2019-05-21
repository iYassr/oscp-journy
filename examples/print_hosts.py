import os

urls = open('hosts.com','r')

for url in urls:
    print('>>> url: {}'.format(url))
    print(os.system('host {}'.format(url)))
