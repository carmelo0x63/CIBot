# CIBot
CounterIntelligence bot, based on Telegram API</br>

### Secure your system
You thought you'd get away without the necessary lecture?!?</br>
Security is an active exercise, you need to:
1. assess your threat landscape
2. generate your custom policy
3. apply it
4. make sure it is constantly applied/monitor

Regarding `#2` above, you may want to read a guide:
1. [How To Harden OpenSSH on Ubuntu 20.04](https://www.digitalocean.com/community/tutorials/how-to-harden-openssh-on-ubuntu-20-04): just an example, the article focuses on Ubuntu but it is applicable to other distros with minor, if any, modifications
2. install [Fail2Ban](https://www.fail2ban.org/)

OK, now you're good to go and read the rest :)
 
### Pre-requisites
Telegram's Bot API allows users to create programs capable, for instance, of sending messages.</br>
Telegram Bots are special accounts that do not require an additional phone number to set up. These accounts serve as an interface for code running somewhere on a remote server.</br>
Get started by reading [Bots: An introduction for developers](https://core.telegram.org/bots) or grab the nitty-gritty stuff by delving into [Telegram Bot API](https://core.telegram.org/bots/api).</br>

### Setup and first run
1. Clone the repository and create a virtual environment
```
$ git clone https://github.com/carmelo0x99/CIBot.git

$ cd CIBot/

$ python3 -m venv .

$ source bin/activate

(CIBot) $ python3 -m pip install --upgrade pip setuptools wheel

(CIBot) $ python3 -m pip install requests
```

2. Configure your own setup with the appropriate bot name, token and chat ID. The configuration file, `cibot.json`, looks like this
```
{"BOT": "<somename_bot>", "TOKEN": "<long string>", "CHATID": "<decimal number>"}
```
**NOTE**: details can be found on [Bots: An introduction for developers](https://core.telegram.org/bots)</br>

3. Check
A quick run of the main script would do:
```
$ ./cibot.py
```
If everything has been setup correctly, according to the instructions to be found on Telegram API pages, a ping should hit your mobile phone with an apt message.</br>

### Build Docker container
This part is optional but no README would be complete without the containerization section:
```
$ docker build -t <repository>/<image>:<tag> .

$ docker push <repository>/<image>:<tag>

$ docker run \
    --detach \
    --rm \
    --volume /var/log:/var/log:ro \
    --volume -v $PWD:/usr/local/bin \
    <repository>/<image>:<tag>
```

### Run through crontab
At minute `59` every hour:
```
59 * * * *  (cd /path/to/CIBot; /usr/bin/docker run -d --rm -v /var/log:/var/log:ro -v $PWD:/usr/local/bin <repository>/<image>:<tag>)
```

### What to do when alerts are being received
First and foremost, [DON'T PANIC](https://en.wikipedia.org/wiki/Phrases_from_The_Hitchhiker%27s_Guide_to_the_Galaxy)!!!</br>
If you've secured your system (you have, right?), chances are that any attacks have been unsuccessful.</br>
It won't hurt though to log into your system and:
1. check the logs
2. run a scan with [Lynis](https://cisofy.com/lynis/) or [chkrootkit](http://www.chkrootkit.org) for instance
3. verify that your security policies are still applied
4. just for fun, check where the attackers came from

