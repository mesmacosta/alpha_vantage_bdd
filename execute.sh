#!/bin/bash

echo "Beginning Entrypoint script execution."

cd src

output=$(behave ./features --tags=-wip)
status=$?

echo "Behave finished executing."

# Change this to your project
gcloud config set project YOUR_PROJECT

gcloud auth activate-service-account --key-file=/app/auth/batch-workload-log-writter.json

gcloud logging write batch-workload "[$hostname]Exit status from behave cmd: $status"
gcloud logging write batch-workload "[$(hostname)]Output from behave cmd: $output"

echo "Entrypoint script execution finished."
