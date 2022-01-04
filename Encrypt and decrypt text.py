import random

try:
    
    from colorama import *

except:
    
    try:
        
        os.system('pip install colorama')
        
    except:

        os.system('pip3 install colorama')
        
def ADD_TEXT(LIST, INPUT, NUMBER):
    
    for i in range(len(INPUT)):
        
        LIST.append(INPUT[NUMBER])
        
        NUMBER+= 1
        
def ENCRYPT(TEXT, INDEX, LIST):
    
    for m in range(len(TEXT)):
        
        TEXT[INDEX:INDEX] = random.choices(LIST, k = 20)
        
        INDEX += 21


print(f'''{Fore.RED}
  ________  __  _____      __
 |___  /  \/  |/ _ \ \    / /
    / /| \  / | (_) \ \  / / 
   / / | |\/| |\__, |\ \/ /  
  / /__| |  | |  / /  \  /   
 /_____|_|  |_| /_/    \/    
''')

print(f'''{Fore.RED}
1 To encrypt
2 To decrypt
''')

List = 'QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm0123456789,./\';][=-<>?:@{}_)(*&^%$£"!'
Choice = input(f'{Fore.RED}> ').strip()
List0 = []
List2 = []
Index0 = 0
Index02 = 0
Index = 1
Index2 = 1

if Choice == '1':
    
    Input = input(f'{Fore.RED}Text : ').strip()
    
    ADD_TEXT(List0, Input, Index0)
    
    ENCRYPT(List0, Index, List)
    
    ADD_TEXT(List2, List0, Index02)
    
    ENCRYPT(List2, Index2, List)
    
    print(''.join(List2))

    print(f'{Fore.RED}Done :)')

    input(f'{Fore.RED}Press enter to close ...')
    
elif Choice == '2':
    
    Input2 = Input = input(f'{Fore.RED}Text : ').strip()
    
    Decrypt = Input2[::21]

    print(Decrypt[::21])

    print(f'{Fore.RED}Done :)')
    
    input(f'{Fore.RED}Press enter to close ...')
    
else:
    
    print(f'{Fore.RED}Wrong input :(')
    
    input(f'{Fore.RED}Press enter to close ...')

