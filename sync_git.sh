#!/bin/bash

dt=$(date +"%Y-%m-%d %T")

git add .

git commit -m "$dt"

git push