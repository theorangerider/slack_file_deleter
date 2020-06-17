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
    # Slack addded show_files_hidden_by_limit as a flag that will include
    # files that are now hidden by the 5 GB limit. See 
    # https://api.slack.com/changelog/2019-03-wild-west-for-files-no-more
    # This isn't handled by Slacker unless I use the 'get' method.
    #result = slack.files.list(ts_to=timestamp)
    result = slack.files.get('files.list',params={'ts_to':timestamp,
                             'show_files_hidden_by_limit':True})
    for my_file in result.body['files']:
        slack.files.delete(my_file['id'])

if __name__ == '__main__':
    main(sys.argv)
