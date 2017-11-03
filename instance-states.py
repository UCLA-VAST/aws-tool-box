#!/bin/env python
import sys
import json
import subprocess
from datetime import datetime, date, time
import dateutil.parser

# Usage: python instance-states.py [key_name]
# Example 1: Show the instances of comaniac
#   python instance-states.py comaniac
# Example 2: Show all instances
#   python instance-states.py

count = 0
keyName = None
if len(sys.argv) == 2:
    keyName = sys.argv[1]

command = ['aws', 'ec2', 'describe-instances']
p = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
data = p.stdout.read()

instanceData = (json.loads(data))['Reservations']

tableFormat = '{0:10s}|{1:19s}|{2:15s}|{3:19s}|{4:10s}'
print tableFormat.format('KeyName', 'InstanceId', 'PublicIpAddress',
        'LaunchTime', 'State')

for instance in instanceData:
    detail = instance['Instances'][0]
    state = detail['State']
    datetime = dateutil.parser.parse(detail['LaunchTime'])
    datetimeStr = datetime.strftime("%Y-%m-%d %H:%M:%S")
    key = detail['KeyName']
    if not keyName or keyName == key:
        count += 1
        if 'PublicIpAddress' in detail:
            ip = detail['PublicIpAddress']
        else:
            ip = 'invalid'
        print tableFormat.format(key, detail['InstanceId'], ip,
                datetimeStr, state['Name'])

print 'Total {0} instances.'.format(count)
