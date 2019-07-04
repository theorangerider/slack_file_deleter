#!/usr/bin/env python
import sys
import time
from slacker import Slacker

def main(args):
    if len(args) < 2:
        sys.exit(1)
    token = args[1]

    slack = Slacker(token)
    now=time.time()
    limit = 60*60*24*180
    timestamp = now - limit
    result = slack.files.list(ts_to=timestamp)
    for my_file in result.body['files']:
        slack.files.delete(my_file['id'])

if __name__ == '__main__':
    main(sys.argv)
