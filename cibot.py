#!/usr/bin/env python3
# CounterIntellingence bot, based on Telegram API
# author: Carmelo C
# email: carmelo.califano@gmail.com
# history, date format ISO 8601:
#  2022-07-28 2.0 Added a summary of the offending IPs
#  2022-07-27 1.2 Small refactoring, moved len(...) to separate function, countLines()
#  2022-06-06 1.1 Replaced plain print statements with logging module
#  2022-06-05 1.0 Initial version

# Import some modules
import json           # JSON encoder and decoder
import logging        # Logging facility for Python
import os             # Miscellaneous operating system interfaces
import re             # Regular expression operations
import requests       # Python HTTP for Humans
import subprocess     # Subprocess management
import time           # Time access and conversions

# General settings
# source: https://core.telegram.org/api
BASEURL = 'https://api.telegram.org/'
LOGFILE = '/var/log/auth.log'

# Version info
__version__ = "2.0"
__build__ = "20220728"


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


def countLines(string):
    return len(string.splitlines())


def groupIPs(string):
    match1 = re.findall(r'from\b.+\bport', string.decode('utf-8'))
    match2 = [m.lstrip('from ').rstrip(' port') for m in match1]
    res = {}
    for ip_addr in match2:
        res[ip_addr] = match2.count(ip_addr)
    return res

def main():
    # Initialization, cibot.log shall be stored in the same directory
    logging.basicConfig(filename = 'cibot.log', level = logging.INFO)

    LASTHOUR = time.asctime()[4:13]  # E.g.: 'Jun  5 11'
    BADGUY = 'Invalid'
    config = readConf()
#    bot = config['BOT']
    token = config['TOKEN']
    chatid = config['CHATID']
    count = 0
    msg2 = ' access attempts in the last hour'

    try:
        # Parses LOGFILE within LASTHOUR, sends to PIPE
        filtered_auth_temp = subprocess.Popen(['grep', LASTHOUR, LOGFILE], stdout = subprocess.PIPE)
        # Reads from PIPE to search for BADGUY
        filtered_auth = subprocess.check_output(['grep', BADGUY], stdin = filtered_auth_temp.stdout)

        # Eventually, we'll get an output that only shows the interesting lines:
        # b'<timestamp> <hostname> sshd[12786]: Invalid user <attacker> from <ip_address> port <portN>\n ..."
        # the type will be 'bytes'

        # Finally the output will be split based on newline ('\n') characters
        count = countLines(filtered_auth)
        ip_list = groupIPs(filtered_auth)
    except:
        pass

    if count:
        logging.info(f'[!] {os.path.basename(__file__)}: {count} unauthorized' + msg2)
        msg1 = str(count) + ' unauthorized'
        tgSend(msg1 + msg2, token, chatid)
        tgSend(str(ip_list), token, chatid)
    else:
        logging.info(f'[+] {os.path.basename(__file__)}: No' + msg2)


# Main function
if __name__ == '__main__':
    main()

