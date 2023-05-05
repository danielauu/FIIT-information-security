import os

with open('johnpw_filelist','rb') as f:
    z = f.readlines()
    john_pw_files = list(z)


# for each john file, 
# we want to go through a regiment of stuff to try


# strategy:
# large word list
# small numbers of variations at a time

wordlists = ['/root/codes/seclists/Passwords/rockyou-50.txt', #100k
             '/root/codes/seclists/Passwords/english.txt', #300k
             '/root/codes/seclists/Passwords/darkc0de.txt',#1M
             '/root/codes/seclists/Passwords/rockyou.txt', #14M
             '/root/codes/wordlists/seattle.txt']

rules=['CMR1',
       'CMRYears',
       'CMR2015',
       'CMRNum',
       'CMRSpec',
       'CMRNumNum',
       'CMRNumSpec',
       'CMRNumNumNum']

scriptfile = 'crack.sh'

with open(scriptfile,'w') as sf:

    sf.write('#!/bin/bash')
    sf.write('\n')

    for rule in rules:
    
        RULES=rule
    
        for wd in wordlists:
    
            WORDLIST=wd 
    
            JOHN_BIN='/root/codes/_sources/john-1.7.9-jumbo-7/run/john'
    
            temp = map(str.strip, john_pw_files)
            john_pw_files = temp
    
            cmd = [JOHN_BIN, '-wordlist:'+WORDLIST, '-rules:'+RULES] + john_pw_files
    
            the_big_one = ' '.join(cmd)
    
            sf.write("\n")
            sf.write("# Wordlist: "+wd+"\n")
            sf.write("# Rule: "+rule+"\n")
            sf.write(the_big_one+"\n\n")

The Result