# fcs-tool-box
Useful utilities for accelerator development

# 

# launch-ec2.sh
A shell script to launch an AWS EC2 instance with specified instance type,
AMI ID  
## Usage
```
launch-ec2.sh instance-type instance-name ami-id key-name  
instance-type: EC2 instance type. e.g. t2.micro, f1.2xlarge  
instance-name: Any meaningfule name for you to identify the instance on EC2 console  
ami-id: Amazon Machine Image ID
key-name: Key name you created for accessing EC2 instances on EC2 console. 
          You should have a file key-name.pem in the working directory.
```
## Example
Launch an f1.2xlarge instance with F1 Development AMI 1.3.0a
```
./launch-ec2.sh f1.2xlarge f1demo ami-df3e6da4 mykey
```
Launch an f1.2xlarge instance with Merlin Compiler 1.0.0 AMI
```
./launch-ec2.sh f1.2xlarge f1demo ami-f2d0ec89 mykey
```



