#!/bin/bash
clear

# Creating new instance

python deploy.py
printf "Done!\n\n"

printf "Adding machine to known hosts...\n"

ssh-keygen -R ec2-18-211-236-148.compute-1.amazonaws.com
ssh-keygen -R 18.211.236.148
ssh-keyscan -H ec2-18-211-236-148.compute-1.amazonaws.com, 18.211.236.148 >> ~/.ssh/known_hosts
ssh-keyscan -H 18.211.236.148 >> ~/.ssh/known_hosts
ssh-keyscan -H ec2-18-211-236-148.compute-1.amazonaws.com >> ~/.ssh/known_hosts


printf "Done!\n\n"

printf "Copying required files over...\n"
scp -i DO_NOT_COMMIT/ec2-keypair.pem -r js -r json -r images -r style -r urls -r webpages -r current_instances.csv -r search.py -r main_page.py -r multicrawler.py -r pagerank.py -r performance_test.py -r database_access.py -r crawler.py -r dbFile.db ubuntu@18.211.236.148:~/ &&
printf "Done!\n\n"

printf "Installing necessary packages...\n"
ssh -i DO_NOT_COMMIT/ec2-keypair.pem ubuntu@18.211.236.148 < bash_scripts/package.sh &&
printf "Done!\n\n"

printf "Starting web server..."
ssh -t -i DO_NOT_COMMIT/ec2-keypair.pem ubuntu@18.211.236.148 'alias python=python3; sudo python main_page.py'


