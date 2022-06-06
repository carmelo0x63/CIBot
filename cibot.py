#!/usr/bin/env python3
# CounterIntellingence bot, based on Telegram API
# author: Carmelo C
# email: carmelo.califano@gmail.com
# history, date format ISO 8601:
#  2022-06-06 1.1 Replaced plain print statements with logging module
#  2022-06-05 1.0 Initial version

# Import some modules
import json                                   # JSON encoder and decoder
import logging                                # Logging facility for Python
import os                                     # Miscellaneous operating system interfaces
import requests                               # Python HTTP for Humans
import subprocess                             # Subprocess management
import time                                   # Time access and conversions

# General settings
# source: https://core.telegram.org/api
BASEURL = 'https://api.telegram.org/'
LOGFILE = '/var/log/auth.log'

# Version info
__version__ = "1.1"
__build__ = "20220606"


def readConf():
    """ 
    read_conf() reads the application's configuration from an external file.
    The file is JSON-formatted and contains:
      the bot name,
      the token,
      the chat ID.
    """
    with open('cibot.json', 'r') as config_in:
        config_json = json.load(config_in)
    return config_json


def tgSend(message, token, chatid):
    """
    tgSend() consumes Telegram API sendMessage method to publish a message on the chat.
    Required arguments are:
      the token,
      the chat ID.
    """
    headers = {'Accept': 'application/json'}
    url = BASEURL + 'bot' + token + '/sendMessage?chat_id=' + chatid + '&text=' + message
    response = requests.post(url = url, headers = headers)


def main():
    # Initialization, cibot.log shall be stored in the same directory
    logging.basicConfig(filename = 'cibot.log', level = logging.INFO)

    LASTHOUR = time.asctime()[4:13]  # E.g.: 'Jun  5 11'
#    LASTHOUR = 'Jun  5 11'
    BADGUY = 'Invalid'
    config = readConf()
#    bot = config['BOT']
    token = config['TOKEN']
    chatid = config['CHATID']
    count = 0
    msg2 = ' access attempts in the last hour'

    try:
        # Parses LOGFILE within LASTHOUR
        grep1 = subprocess.Popen(['grep', LASTHOUR, LOGFILE], stdout = subprocess.PIPE)
        # Searches the above output for BADGUY then counts the number of lines
        grep2 = subprocess.check_output(['grep', BADGUY], stdin = grep1.stdout)
        count = len(grep2.splitlines())
    except:
        pass

    if count:
        logging.info(f'[!] {os.path.basename(__file__)}: {count} unauthorized' + msg2)
        msg1 = str(count) + ' unauthorized'
        tgSend(msg1 + msg2, token, chatid)
    else:
        logging.info(f'[+] {os.path.basename(__file__)}: No' + msg2)

# Main function
if __name__ == '__main__':
    main()

