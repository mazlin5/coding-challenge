# coding-challenge
YipitData recently acquired a dataset of Oscar-nominated movies from 1927 - 2014. The data is stored in an S3 bucket (s3://yipit-oscars-data). This repo explains how to extract, transform, and load the data as a csv.

### Prerequisites
- IDE Dev Environment (VSCode, atom, ect.)
- Create an AWS account (https://portal.aws.amazon.com/billing/signup#/start/email) & setup all account settings (billing, payment methods, ect.)
- Python version 3 or greater is required
- AWS CLI is required
- Access IAM keys and Secret keys & S3 bucket keys (s3://yipit-oscars-data) for AWS connection 

##### Set up AWS IAM credentials to access AWS resources (S3 data)
- Create an IAM users (deployment display name) in `Add user` and select `Programmatic access` as the AWS access type.
- Grant admin access to users by selecting `AdministratorAccess`
- Store the created user `Access key ID` and `Secret access key` into a safe location for configuring AWS CLI 

### Installation
- Go to https://www.python.org and find your respective OS download package file (Windows or Mac OS X).
  - verify install from machine terminal run `python` or `python3.6` to verify console pops up
- Confirm pip for Python using `pip3.6` vs `pip` for Python 2.7
- Install AWS CLI using homebrew (Mac OS) or reference https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html for your machines OS.
  - Linux `curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
unzip awscliv2.zip
sudo ./aws/install`
- Configure AWS CLI by typing `aws configure` in terminal and input your `region (us-east-1)` & `access keys` given from yipitdata
- Install Boto3 library in Python using command `pip3 install boto3` or `pip install boto3`

### Instructions for running the scripts
  - 


### Troubleshooting
  - Test aws-cli was installed correctly by typing `which aws`  or `aws --version` in your env terminal.
  - Ensure configure credentials are set properly by running command `aws configure`. If correct keys and region show correctly without input, then all is successful
