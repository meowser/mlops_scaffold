#!/bin/bash

## Update the URL of origin remote using SSH
# git remote set-url origin git@github.com:username/repo.git
# git remote set-url origin git@github.com:prfrl/mlops_scaffold.git
# Test URL remote
# git remote show origin

dt=$(date "+ %Y-%m-%d %T")

git add .

git commit -m "$dt"

git push