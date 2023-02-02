import os, sys, time

from colorama import Fore

def show_loading():
    clear()
    print(Fore.RESET +
        '      _______ _______________    ' + Fore.BLUE + '   _______         ______________ _____ \n' + Fore.RESET +
        '      ___    |____  _/___    |   ' + Fore.BLUE + '   ___    |____  ________  /___(_)__  /_\n' + Fore.RESET +
        '      __  /| | __  /  __  /| |   ' + Fore.BLUE + '   __  /| |_  / / /_  __  / __  / _  __/\n' + Fore.RESET +
        '      _  ___ |__/ /   _  ___ |   ' + Fore.BLUE + '   _  ___ |/ /_/ / / /_/ /  _  /  / /_  \n' + Fore.RESET +
        '      /_/  |_|/___/   /_/  |_|   ' + Fore.BLUE + '   /_/  |_|\\__,_/  \\__,_/   /_/   \\__/  \n' + Fore.RED)
    loading_status = 0
    loading_tick = 0
    icon_states = ['\\', '|', '/', '-']
    is_loading = True
    while is_loading:
        original_str = "\r[*] Starting the AIA Audit framework ..."
        for i in range(0, len(original_str)):
            new_str = "\r"
            for k in range(0, len(original_str)):
                if k <= 4 or k >= len(original_str) - 4:
                    new_str += original_str[k]
                else:
                    if i == k:
                        if original_str[k] == " ":
                            new_str += " "
                        if original_str[i].isupper():
                            new_str += original_str[k].lower()
                        elif original_str[i].islower():
                            new_str += original_str[k].upper()
                    else:
                        new_str += original_str[k]
            new_str += icon_states[loading_status]
            sys.stdout.write(new_str)
            sys.stdout.flush()
            time.sleep(0.300)
            if loading_status == 3:
                loading_status = 0
            else:
                loading_status += 1
            loading_tick += 1
            if loading_tick > 5:
                sys.stdout.write("\r")
                sys.stdout.flush()
                is_loading = False

def clear():
    os.system('cls' if os.name=='nt' else 'clear')

def show_running(ip, port):
    clear()
    print(Fore.RESET +
          '      _______ _______________    ' + Fore.BLUE + '   _______         ______________ _____ \n' + Fore.RESET +
          '      ___    |____  _/___    |   ' + Fore.BLUE + '   ___    |____  ________  /___(_)__  /_\n' + Fore.RESET +
          '      __  /| | __  /  __  /| |   ' + Fore.BLUE + '   __  /| |_  / / /_  __  / __  / _  __/\n' + Fore.RESET +
          '      _  ___ |__/ /   _  ___ |   ' + Fore.BLUE + '   _  ___ |/ /_/ / / /_/ /  _  /  / /_  \n' + Fore.RESET +
          '      /_/  |_|/___/   /_/  |_|   ' + Fore.BLUE + '   /_/  |_|\\__,_/  \\__,_/   /_/   \\__/  \n' + Fore.RED)
    print(Fore.RESET +
          "       =[ " + Fore.RED + "AIA Audit Framework v0.1 " + Fore.RESET + "                       ]\n" +
          "+ -- --=[ 2230 exploits - 1177 auxiliary - 398 post       ]\n" +
          "+ -- --=[ 867 payloads - 45 encoders - 11 nops            ]\n" +
          "+ -- --=[ 9 evasion                                       ]\n" +
          "                                                           \n" +
          "       =[ " + Fore.RED + "Website running on http://" + ip + ":" + port + Fore.RESET + "          ]\n" + Fore.RED)