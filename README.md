# LogBot

LogBot is a lighweight customizable google chat bot designed to read log files and report of events of a specified logging level.

* Author(s): David Marienburg
* Contributors(s):
* Maintainer(s): David Marienburg
* Version: 1.0b
* Last Updated: 2022-07-21

## Getting Started

Initial setup of LogBot:
* For every script you want the bot to monitor add a new entry into the Library/data/log_details.json file
  * Each of these entries must use a format matching the extant entries.<br><br>
* If you want LogBot to report into a different google chat change the url starting on line 13 of the logbot.py script.
  * Directions for how to do this can be found here: [https://developers.google.com/chat/how-tos/webhooks](https://developers.google.com/chat/how-tos/webhooks)

## ToDo

|Component            |Not Started|In Progress|Testing|Complete|Notes                                                          |
|:-------------------:|:---------:|:---------:|:-----:|:------:|--------------------------------------------------------------:|
|log_details_reader   |           |           |       |X       |                                                               |
|logbot (main class)  |           |           |       |X       |                                                               |


## Contribute
