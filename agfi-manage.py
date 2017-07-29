#!/bin/env python

# Copyright 2017 Falcon Computing Solutions, Inc.
#  
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#  
#     http://www.apache.org/licenses/LICENSE-2.0
#  
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import json
import subprocess
from datetime import datetime, date, time
import dateutil.parser

class AGFIManager():
    version = 'v0.0.1'
    def showAFI(self): 
        command = ['aws', 'ec2', 'describe-fpga-images', '--owners', 'self']
        p = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        allAFIs = p.stdout.read()
        
        allAFIParse = json.loads(allAFIs)
        
        print 'Found {} AGFIs.'.format(len(allAFIParse['FpgaImages']))
        
        allAFISorted = sorted(allAFIParse['FpgaImages'], key=lambda dct: dct['UpdateTime'])
        AFITableFormat = '{:20s}|{:20s}|{:12s}|{:12s}|{:20s}'
        print AFITableFormat.format('AGFI', 'UpdateTime', 'ShellVersion', 'State', 'Name')
        
        for afi in allAFISorted:
             afiState = afi['State']
             afiDatetime = dateutil.parser.parse(afi['UpdateTime'])
             afiDatetimeStr = afiDatetime.strftime("%Y-%m-%d %H:%M:%S")
             if afiState['Code'] == 'pending':
                 print AFITableFormat.format(afi['FpgaImageGlobalId'], afiDatetimeStr, 'pending', afiState['Code'], afi['Name'])
             else:
                 print AFITableFormat.format(afi['FpgaImageGlobalId'], afiDatetimeStr, afi['ShellVersion'], afiState['Code'], afi['Name'])
        
        print '\nTotal AGFIs: {}'.format(len(allAFIParse['FpgaImages']))

#main function
def main():
    agfiManager = AGFIManager()
    print 'Falcon Computing AWS F1 FPGA AGFI Manager ' + agfiManager.version
    agfiManager.showAFI()

if __name__ == '__main__':
     main()
