# CIBot
CounterIntelligence bot, based on Telegram API</br>

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
*NOTE*: details can be found on [Bots: An introduction for developers](https://core.telegram.org/bots)</br>

3. Check
A quick run of the main script would do:
```
$ ./cibot.py
```
If everything has been setup correctly, according to the instructions to be found on Telegram API pages, a ping should hit your mobile phone with an apt message.</br>

### Build Docker container
This part is optional but no README would be complete without the containerization section:
```
docker build -t <repository>/<image>:<tag> .

docker push <repository>/<image>:<tag>

docker run \
    --detach \
    --rm \
    --volume /var/log:/var/log:ro \
    <repository>/<image>:<tag>
```

