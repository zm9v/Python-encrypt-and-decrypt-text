import random

import os

try:
    
    from colorama import *

except:
    
    try:
        
        os.system('pip install colorama')
        
    except:

        os.system('pip3 install colorama')        

print(f'''{Fore.RED}
1 To encrypt
2 To decrypt
''')

Choice,Text,Index0,List,Index = input(f'{Fore.RED}> ').strip(),[],0,'QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm0123456789,./\';][=-<>?:@{}_)(*&^%$£"!',1

if Choice == '1':
    
    Input = input(f'{Fore.RED}Text : ').strip()
    
    for i in range(len(Input)):
        
        Text.append(Input[Index0])
        
        Index0 += 1
        
    for m in range(len(Text)):
        
        Text[Index:Index] = random.choices(List, k = 2)
        
        Index += 3
        
    print(''.join(Text))
    
    input(f'{Fore.RED}Press enter to close ...')
    
elif Choice == '2':
    
    Input2 = Input = input(f'{Fore.RED}Text : ').strip()
    
    print(Input2[::3])
    
    input(f'{Fore.RED}Press enter to close ...')
    
else:
    
    print(f'{Fore.RED}Wrong input :(')
    
    input(f'{Fore.RED}Press enter to close ...')
