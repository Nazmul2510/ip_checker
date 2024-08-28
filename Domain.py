import socket
import pyfiglet
from termcolor import colored

print(colored('*********************DOmain TO IP********************'),'Green')

into = colored(pyfiglet.figlet_format('IP Checker'),'green')

print(into)

Domain = input('Enter Your Domain:')

xpath = socket.gethostbyname(Domain)

print('IP for {} : {}'.format(Domain,xpath))

