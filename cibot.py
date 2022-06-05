#!/usr/bin/env python3
# CounterIntellingence bot, based on Telegram API
# author: Carmelo C
# email: carmelo.califano@gmail.com
# history, date format ISO 8601:
#  2022-06-05 1.0 Initial version

# Import some modules
import requests      # Python HTTP for Humans
import subprocess    # Subprocess management
import time          # Time access and conversions

# General settings
# source: https://core.telegram.org/api
BASEURL = 'https://api.telegram.org/'
BOT = <BOTNAME>
TOKEN = <TOKEN>
CHAT_ID = <CHAT_ID>
LOGFILE = '/var/log/auth.log'

# Version info
__version__ = "1.0"
__build__ = "20220605"


def tgsend(message):
    headers = {'Accept': 'application/json'}
    url = BASEURL + 'bot' + TOKEN + '/sendMessage?chat_id=' + CHAT_ID + '&text=' + message
    response = requests.post(url = url, headers = headers)


def main():
    # Initialization
    LASTHOUR = time.asctime()[4:13]  # E.g.: 'Jun  5 11'
#    LASTHOUR = 'Jun  5 11'
    BADGUY = 'Invalid'

    try:
        # Parses LOGFILE within LASTHOUR
        grep1 = subprocess.Popen(['grep', LASTHOUR, LOGFILE], stdout = subprocess.PIPE)
        # Searches the above output for BADGUY
        grep2 = subprocess.check_output(['grep', BADGUY], stdin = grep1.stdout)
        count = len(grep2.splitlines())
        print(f'[!] {count} unauthorized access attempts in the last hour')
        msg1 = str(count) + ' unauthorized'
    except:
        print('[+] No access attempts in the last hour')
        msg1 = 'No'

    msg2 = ' access attempts in the last hour'
    tgsend(msg1 + msg2)


# Main function
if __name__ == '__main__':
    main()

