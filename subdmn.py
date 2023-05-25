import urllib.request, urllib.error
import threading
import re


def baner():
    print("""
               ~~~~ SUBDOMAIN ENUMERATION TOOL ~~~~
    
Created By :
                 ______                      ________                         
___________  ____  /______________        ______(_)_____ ___      _______ _
_  ___/_  / / /_  __ \  _ \_  ___/        _____  /_  __ `/_ | /| / /  __ `/
/ /__ _  /_/ /_  /_/ /  __/  /            ____  / / /_/ /__ |/ |/ // /_/ / 
\___/ _\__, / /_.___/\___//_/________________  /  \__,_/ ____/|__/ \__,_/  
      /____/                _/_____//_____/___/                            
    """)


def usrResposeReturn(url):
    try:
        conn = urllib.request.urlopen(url)

    except urllib.error.HTTPError as e:    
        print("{} --> [{}]".format(url,e.code))


    except urllib.error.URLError as e:
        pass
    #   print('URLError: {}'.format(e.reason))

    else:  
      print("{} --> [{}]".format(url,"200"))


def mainprocess(fileName):
    file = open("subdmbfld/"+fileName, 'r')
    try:
        for each in file:
           each=each.rstrip('\n')
           url="https://"+each+"."+inpurl

        #    print(url)
        #   print(threading.current_thread().getName())
           usrResposeReturn(url)
           
    except:
        print("finshed {}".format(threading.current_thread().getName()))



def isValidDomain(str):
   
    # domain name.
    regex = "^((?!-)[A-Za-z0-9-]" + "{1,63}(?<!-)\\.)" +"+[A-Za-z]{2,6}"
     
    # Compile the ReGex
    p = re.compile(regex)
 
    if(re.search(p, str)):
        starting()
    else:
        print("It is not a valid domain")


def starting():
    
    t1 = threading.Thread(target=mainprocess, name='t1',args=("t1.txt",))
    t2 = threading.Thread(target=mainprocess, name='t2',args=("t2.txt",))
    t3 =threading.Thread(target=mainprocess,name='t3',args=("t3.txt",))
    t4 =threading.Thread(target=mainprocess,name='t4',args=("t4.txt",))
     
    t1.start()
  
    t2.start()
    t3.start()
    t4.start()


baner()
inpurl=input("\nEnter the url without http/https > ")
isValidDomain(inpurl)


