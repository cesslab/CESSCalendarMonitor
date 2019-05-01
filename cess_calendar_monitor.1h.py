#!/usr/bin/env -S PATH="${PATH}:/usr/local/bin" python3
# -*- coding: utf-8 -*-
#
# CESS Calendar Monitor
#
# <bitbar.title>CESS Calendar Monitor</bitbar.title>
# <bitbar.version>v1.0</bitbar.version>
# <bitbar.author>Anwar A. Ruff</bitbar.author>
# <bitbar.author.github>aaruff</bitbar.author.github>
# <bitbar.desc>
# Checks the CESS calendar for today's sessions.
# </bitbar.desc>
# <bitbar.dependencies>ics,python</bitbar.dependencies>
# <bitbar.image></bitbar.image>
#
# Dependencies:
#   ics (https://icspy.readthedocs.io/en/v0.4/index.html)
#      installable via pip `pip install ics`


from ics import Calendar, Event
from urllib.request import urlopen
from urllib.error import HTTPError, URLError
from datetime import datetime, date

# Enter URL to ics
url = ''


def main():
    try:
        c = Calendar(urlopen(url).read().decode('iso-8859-1'))
        d = date.today()
        today = Event(begin=datetime.combine(d, datetime.min.time()), end=datetime.combine(d, datetime.max.time()))
        print('Experiments')
        print('---')
        if c.events:
            for e in c.events:
                if e.starts_within(today):
                    print("{} - {}: {}".format(e.begin.format('h:mma'), e.end.format('h:mma'), e.name))
        else:
            print('None Today')
    except HTTPError as e:
        print("HTTP connection error.")
    except URLError as e:
        print("URL connection error.")


if __name__ == '__main__':
    main()
