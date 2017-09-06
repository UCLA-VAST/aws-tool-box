#!/bin/bash
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

DIR=$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )

if [ $# -lt 4 ]; then
    echo "Usage: ${BASH_SOURCE[0]} instance-type instance-name ami-id key-name"
    exit 1
fi

instance_type=$1
instance_name=$2
image_id=$3
key_name=$4

username=centos

instance_json=`aws ec2 run-instances \
        --count 1 \
        --image-id $image_id \
        --instance-type $instance_type \
        --key-name $key_name \
        --security-groups default` 

if [ $? -ne 0 ]; then
    >&2 echo "Error: Failed to launch instance"
    exit 2
fi;

instance_id=`echo $instance_json > tmp.json && jq -r '.Instances[].InstanceId' tmp.json`;

if [ $? -ne 0 ]; then
    >&2 echo "Error: Failed to get instance ID."
    exit 3
fi;

ip=`aws ec2 describe-instances --instance-ids $instance_id \
    | jq -r .Reservations[].Instances[].PrivateIpAddress`;

aws ec2 create-tags --resources $instance_id --tags "Key=Name,Value=$instance_name"

# wait for instance to init
ping -c 1 $ip > /dev/null;
ret=$?;
while [ $ret -ne 0 ]; do
    echo "Waiting for the instance to initialize..."
    sleep 10
    ping -c 1 $ip > /dev/null
    ret=$?
done;

echo "$instance_type instance with AMI $instance_id has been created."
echo "Run the command below to ssh to the instance"
echo "ssh -i $key_name.pem centos@$ip"

