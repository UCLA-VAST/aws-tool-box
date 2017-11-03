# fcs-tool-box for UCLA
- This repo was forked from Falcon Computing Solutions, Inc.
- The settings in this repo are customized for UCLA CDSC/VAST group.

# launch-ec2.sh
A shell script to launch an AWS EC2 instance with specified key and
instance type.

## Usage
```
launch-ec2.sh key-name [instance-type]
key-name: Key name you created for accessing EC2 instances on EC2 console. 
          You should have a file key-name.pem in the working directory.
instance-type (optional): EC2 instance type. Default is f1.2xlarge.
```

## Example
Launch an f1.2xlarge instance using key cdsc
```
./launch-ec2.sh cdsc
```
Launch an c4.4xlarge instance with key cdsc
```
./launch-ec2.sh cdsc c4.4xlarge
```

# terminate-ec2.sh
List all active instances and let user choose one to be terminated.

## Usage
```
terminate-ec2.sh
```

# instance-states.py
Check the states of all active instances.

## Usage
```
python instance-states.py [key-name]
key-name (optional): Same as launch-ec2.sh
```
