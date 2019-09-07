#!/bin/bash

echo "Beginning Entrypoint script execution."

cd src

output=$(behave ./features --tags=-wip)
status=$?

echo "Behave finished executing."

# Change this to your project
gcloud config set project YOUR_PROJECT

# Add this service account to the root of your source repo dir. It's a SA with the Log writter and Custom VM delete Role.
gcloud auth activate-service-account --key-file=/app/auth/batch-workload-log-writter.json

gcloud logging write batch-workload "[$(hostname)]Exit status from behave cmd: $status"
gcloud logging write batch-workload "[$(hostname)]Output from behave cmd: $output"

echo "Entrypoint script execution finished."

# Delete the VM
gcloud compute instances delete $(hostname) --zone ${gcp_zone}
