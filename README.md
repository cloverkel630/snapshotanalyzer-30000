# snapshotanalyzer-30000

Demo project to manage AWS EC2 instance snapshots

## About

This project is a demo, and uses boto3 to manage AWS EC2 instance snapshots.

## Configuring

shotty uses the configuration file created by the AWS Cli. e.g.

`aws confirgure --profile shotty`

## Running

`pipevn run python shotty/shotty.py <command> <--project=PROJECT`

*command* is a list, start, or stop_instances
*project* is optional
