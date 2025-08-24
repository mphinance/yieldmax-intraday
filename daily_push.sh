#!/bin/bash

# Add all new and modified files
git add .

# Get the current date in YYYY-MM-DD format
commit_date=$(date +%Y-%m-%d)

# Commit with a message that includes the date
git commit -m "Automated commit for $commit_date"

# Push the changes to the remote repository
git push
