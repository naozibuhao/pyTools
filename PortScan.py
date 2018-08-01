#-*- coding: UTF-8 -*-

import socket

import threading


lock = threading.Lock()

threads = []

def Get_ip(domain):  

    try:  

        return socket.gethostbyname(domain)  

    except socket.error,e:  

        print '[-]%s: %s'%(domain,e)  

        return 0 

 

def PortScan(ip,port):

    try:

        s=socket.socket() 

        s.settimeout(0.1)

        s.connect((ip,port))

        lock.acquire()

        openstr= "[-] PORT:"+str(port) +" OPEN "

        print openstr

        lock.release()

        s.close()

    except:

        pass

def main():

    banner = '''

                      _                       

     _ __   ___  _ __| |_ ___  ___ __ _ _ __  

    | '_ \ / _ \| '__| __/ __|/ __/ _` | '_ \ 

    | |_) | (_) | |  | |_\__ \ (_| (_| | | | |

    | .__/ \___/|_|   \__|___/\___\__,_|_| |_|

    |_|                                       



            '''

    print banner

    domain = raw_input("PLEASE INPUT YOUR TARGET:")

    ip = Get_ip(domain)

    print '[-] IP:'+ip

    for n in range(1,76):

        for p in range((n-1)*880,n*880):

            t = threading.Thread(target=PortScan,args=(ip,p))

            threads.append(t)

            t.start()     



        for t in threads:

            t.join()

    print ' This scan completed !'

if __name__=='__main__':  

    main()

    