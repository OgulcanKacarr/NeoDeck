# -*- coding: utf-8 -*-
from colorama import Fore, Back, Style
from termcolor import colored, cprint
import subprocess as sub
import optparse
import colorama
import socket
import time
import sys
import os


colorama.init()
print Fore.GREEN
os.system("clear")



def sendmessage(message):
	subprocess.Popen(['notify-send', message])
	return



 #===============================================================



HOST = '192.168.1.5' #change this your local ip
PORT = 5050          # dont change because this port default for app
 


#===============================================================


#Add or Changer Process

def OpenBrowser():
	return sub.call(["firefox"],shell=True)

def OpenTryHackme():
	return sub.call(["firefox www.tryhackme.com"],shell=True)

def openTXT():
	return sub.Popen(["leafpad"],shell=True)

def openTERMINAL():
	return sub.Popen(["xterm"],shell=True)

def startApache2():
	return sub.Popen(["service apache2 start"],shell=True)

def openFOLDER():
	return sub.Popen(["nautilus /root"],shell=True)
#===============================================================


#Connect

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
	s.bind((HOST, PORT))
except socket.error as err:
	print Fore.RED
	print 'Bind Failed, Error Code: ' + str(err[0]) + ', Message: ' + err[1]
	sys.exit()

def exitAPP():
        print Fore.BLUE
        print """
                                                                                                                                                       
                                                                                                      .                                                   
                                                   ...'',,.                                         .''''.....                                            
                                              .'''''''''....                     .'''.              .......''.....                                        
                                         ..''.','...''....     '.     ...  .''. .:ddl.               .................                                    
                                       ..','',,''...''''...''',,.    ,od:..:dd:..;dd;  .:cccc:,.      ..'......'''......                                  
                                    ...'','..''.....'...  ..',,''::. ;ddc. ;dd:..'od;.,odc''::c;..,:;'...........,'..'.....                               
                                 ...'''..''..''.........';'':;::';o, .coo:;cdl.  'od,.'lo:.......,:lcclc'........,'..'.........                           
                              ...'...............,cooolc,..lc.:d;.cl...;c;,'',....;l,...,c:::;..lxo::lod;..,;....'...............                         
                              ....''...........;lol,.;odo' 'c:,,,,;c,........ ..................,::::loc'.cddl:,'.....'...........                        
                             .......'.........:dl'.   ;dd;  .',''.,c,....   .;:;'.,:.  .....'....  ..;;..cddl;,col,....''......'....                      
                          ...........'.'.... 'ddo:....ldo;     ''',..       ;olcooc;.     ....          'dd:. .,ldo....','.....'...'..                    
                        .................'.   ,ooollol:'..                 .co:;ll;,.      .            .''. .cddl.  ..........'..'''....                 
                     .............''.   ...    ....';.                      ,llolcc:'                       .cdc'.   ..   .........'.......               
                     .. ..   ......                                           ...'::.                        ..             ................              
                     ......  .                                              .;:cldc,.                                                ......               
                 .........                                                 .lxoccl,                                                   .''......           
                .......                                                     .,;:coo:.                                                   .',...'.          
              .......                                                            .;;.                                                     ........        
            ..'...                                                          ..     .'.                                                       ....'.       
           .....                                                           .;.      ;;'.                                                       ...''.     
          .....                                                            .;,     .;...                                                        ....'.    
         ....                                                               .,;;;;,,.                                                             .....   
        ...                                                                   ...,;'                                                                ....  
                                                                            ..,;cll:.                                                                     
                                                                           .cdocll,                                                                       
                                                                           .,clcloc,.                                                                     
                                                                              ...;cc.                                                                     
                                                                           .,'.  .,:'                                                                     
                                                                           .;ol;;cl;.                       Oğulcan KAÇAR                                             
                                                                            .;oddl;'.                       github.com/OgulcanKacarr                                              
                                                                           .:lloolc:'.                                                                    
                         .....'...'.......''..'.. .''.                       ......                      ..'....'...'.......'.........                    
                                                                           .........                                                                      
                                                                           ..........                                                                     
                                                                           ..........                                                                     
                                                                           .''....'..                                                                     
        """
	print Fore.GREEN
	print "bye bye"
	sendmessage("NeoDeck is Offline")
	exit()

def startApp():
	print Fore.GREEN
	print '[+] Connected App'
	sendmessage("!! NeoDeck is online... !!")
	s.listen(10)
	print Fore.BLUE
	print '[+] Commands is now listening'
	try:
		while 1:
			conn, addr = s.accept()
			print Fore.RED
			print 'Connect with ' + addr[0] + ':' + str(addr[1])
			buf = conn.recv(64)
			
			#print(buf)

			#===============================================================
			##Add your func

			if buf == "value1":     #Default browser   		 [BUTTON1]
				print Fore.GREEN
				OpenBrowser()
				
			if buf == "value2":     #default xterm	   		 [BUTTON2]
				print Fore.RED
				openTERMINAL()
				
			if buf == "value3":     #default start apache2   [BUTTON3]
				print Fore.GREEN
				startApache2()

			if buf == "value4":     # add button	   		 [BUTTON4]	   		 
				print Fore.RED
				print " "

			if buf == "value5":     # add button	   		 [BUTTON5]
				print Fore.GREEN
				print " "

			if buf == "value6":     # add button	   		 [BUTTON6]
				print Fore.RED
				print " "

			if buf == "value7":     # #default folder	   	 [BUTTON7]
				print Fore.GREEN
				openFOLDER()

			if buf == "value8":     # default open leafpad   [BUTTON8]
				print Fore.RED
				openTXT()

			if buf == "value9":     # default tryhackme.com  [BUTTON9]
				print Fore.GREEN
				OpenTryHackme()

			if buf == "value10":    # add button	   		 [BUTTON10]
				print Fore.RED
				print " "

			if buf == "value11":    # add button	   		 [BUTTON11]
				print Fore.GREEN
				print " "

			if buf == "value12":    # add button	   		 [BUTTON12]
				print Fore.RED
				print " "


			#===============================================================



	except:
		exitAPP()

print Fore.GREEN
print """

	
	NNNNNNNN        NNNNNNNNEEEEEEEEEEEEEEEEEEEEEE     OOOOOOOOO     DDDDDDDDDDDDD      EEEEEEEEEEEEEEEEEEEEEE       CCCCCCCCCCCCCKKKKKKKKK    KKKKKKK
N:::::::N       N::::::NE::::::::::::::::::::E   OO:::::::::OO   D::::::::::::DDD   E::::::::::::::::::::E    CCC::::::::::::CK:::::::K    K:::::K
N::::::::N      N::::::NE::::::::::::::::::::E OO:::::::::::::OO D:::::::::::::::DD E::::::::::::::::::::E  CC:::::::::::::::CK:::::::K    K:::::K
N:::::::::N     N::::::NEE::::::EEEEEEEEE::::EO:::::::OOO:::::::ODDD:::::DDDDD:::::DEE::::::EEEEEEEEE::::E C:::::CCCCCCCC::::CK:::::::K   K::::::K
N::::::::::N    N::::::N  E:::::E       EEEEEEO::::::O   O::::::O  D:::::D    D:::::D E:::::E       EEEEEEC:::::C       CCCCCCKK::::::K  K:::::KKK
N:::::::::::N   N::::::N  E:::::E             O:::::O     O:::::O  D:::::D     D:::::DE:::::E            C:::::C                K:::::K K:::::K   
N:::::::N::::N  N::::::N  E::::::EEEEEEEEEE   O:::::O     O:::::O  D:::::D     D:::::DE::::::EEEEEEEEEE  C:::::C                K::::::K:::::K    
N::::::N N::::N N::::::N  E:::::::::::::::E   O:::::O     O:::::O  D:::::D     D:::::DE:::::::::::::::E  C:::::C                K:::::::::::K     
N::::::N  N::::N:::::::N  E:::::::::::::::E   O:::::O     O:::::O  D:::::D     D:::::DE:::::::::::::::E  C:::::C                K:::::::::::K     
N::::::N   N:::::::::::N  E::::::EEEEEEEEEE   O:::::O     O:::::O  D:::::D     D:::::DE::::::EEEEEEEEEE  C:::::C                K::::::K:::::K    
N::::::N    N::::::::::N  E:::::E             O:::::O     O:::::O  D:::::D     D:::::DE:::::E            C:::::C                K:::::K K:::::K   
N::::::N     N:::::::::N  E:::::E       EEEEEEO::::::O   O::::::O  D:::::D    D:::::D E:::::E       EEEEEEC:::::C       CCCCCCKK::::::K  K:::::KKK
N::::::N      N::::::::NEE::::::EEEEEEEE:::::EO:::::::OOO:::::::ODDD:::::DDDDD:::::DEE::::::EEEEEEEE:::::E C:::::CCCCCCCC::::CK:::::::K   K::::::K
N::::::N       N:::::::NE::::::::::::::::::::E OO:::::::::::::OO D:::::::::::::::DD E::::::::::::::::::::E  CC:::::::::::::::CK:::::::K    K:::::K
N::::::N        N::::::NE::::::::::::::::::::E   OO:::::::::OO   D::::::::::::DDD   E::::::::::::::::::::E    CCC::::::::::::CK:::::::K    K:::::K
NNNNNNNN         NNNNNNNEEEEEEEEEEEEEEEEEEEEEE     OOOOOOOOO     DDDDDDDDDDDDD      EEEEEEEEEEEEEEEEEEEEEE       CCCCCCCCCCCCCKKKKKKKKK    KKKKKKK
																																				  
  


  [+]  Please do not forget to download the application from google play. !!!




  - Created by Oğulcan KAÇAR



	 """




parseObject = optparse.OptionParser()
print(Fore.GREEN)
parseObject.add_option("-c","--console",dest="startConsole",help=" python NeoDesk.py -c startConsole")
parseObject.add_option("-v","--version",dest="version",help="python NeoDesk.py -v version")


(userSelect,arguments) = parseObject.parse_args()


if sys.argv < 2:
	print Fore.RED
	print "Please use to python NeoDeck.py -h\n"
	exit()


if userSelect.startConsole == "startConsole":
	startApp()
elif userSelect.version == "version":
	print Fore.GREEN
	print "Version: 1.0\n"	
else:
	print Fore.RED
	print "Please use to python NeoDeck.py -h\n"




s.close()   