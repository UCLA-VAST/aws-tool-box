#!/bin/bash

# Show states of all instances
python instance-states.py

# Read instance ID from user
read -p "Enter the instance ID: " id

# Terminate
echo `aws ec2 terminate-instances --instance-ids $id` > tmp.json
jq -r '.TerminatingInstances[].CurrentState.Name' tmp.json
rm tmp.json

