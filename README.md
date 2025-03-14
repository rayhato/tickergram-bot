
<p align="center">
  <img alt="tickergram-logo" src="media/tickergram_logo.png">
</p>

# What's Tickergram?

Tickergram is a Telegram bot to look up quotes, charts, general market sentiment and more. It can be used collaboratively in group chats or by talking directly to it. Users can also keep a watchlist and receive price information notifications.
Support original author Alberto Ortega here: https://github.com/sponsors/a0rtega


## Bot commands

- `/quote` **\<ticker\>** get quote
- `/chart` **\<ticker\> \[1y,6m,5d\]** get price and volume chart
- `/news` **\<ticker\>** get the latest news related to the ticker
- `/watch` **list\|add\|del \[ticker\]** list, add or remove ticker from your watchlist
- `/watchlist` get an overview of your watchlist
- `/watchlistnotify` toggle the automatic watchlist notifications on and off
- `/overview` get an overview of global markets
- `/feargreed` get picture of CNN's Fear & Greed Index

<p align="center">
  <img alt="quote and chart" src="media/quote_chart.jpg">
  <img alt="watchlist" src="media/watchlist.jpg">
</p>

## Requirements


- [yfinance](https://github.com/ranaroussi/yfinance), which is used to get financial information. The data provider may change in the future.
- [TA-Lib] (https://github.com/mrjbq7/ta-lib), for technical analysis of financial market data.
- [Redis](https://redis.io/), used as database to keep both permanent and temporary data (cache).
- (_Optional_) Firefox is used by bot commands that take website screenshots, such as `/feargreed`.

## Installation

- Install Python 3.9+
- Install Redis.
- Talk to the [@BotFather](https://t.me/botfather) to create a new bot and get its token.
- Install Tickergram and its dependencies by running `python setup.py install` or `pip install https://github.com/rayhato/tickergram-bot/archive/refs/heads/main.zip`.
- Run the bot with HTTP API token

```
$ tickergram-bot -h
usage: tickergram-bot [-h] [-p PASSWORD] [-a ALLOW] [-r REDIS] [-l PORT] [-d DB] token

Tickergram bot

positional arguments:
  token                 Telegram Bot API token

optional arguments:
  -h, --help            show this help message and exit
  -p PASSWORD, --password PASSWORD
                        Set a password required to interact with the bot (enables the /auth command)
  -a ALLOW, --allow ALLOW
                        Allow certain commands without requiring the password, comma-separated list (example: /quote,/chart)
  -r REDIS, --redis REDIS
                        redis host to use
  -l PORT, --port PORT  redis port to use
  -d DB, --db DB        redis database to use
```

If Tickergram is running correctly, the output should be similar to this:

```
$ tickergram-bot <token>
2021-09-28 19:52:58,820 Checking Telegram API token ...
2021-09-28 19:52:58,942 Telegram API token is valid
2021-09-28 19:52:58,942 Testing Redis connectivity ...
2021-09-28 19:52:58,944 Redis connection is ok
```

## Usage

After sending the Telegram message `/start` or `/help` to the bot, it will reply with the supported bot commands.

The bot administrator can notify chat watchlists (when notifications are enabled) with the command `tickergram-notify`. It may be a good idea to run this command on a regular basis (for example at market open) using crontab.

## License

[MIT](LICENSE)
