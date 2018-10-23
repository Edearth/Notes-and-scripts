#!/bin/bash

#Instructions to use this script:
# 1. Install PostgreSQL (Mac: brew update && brew doctor && brew install postgresql)
# 2. Create pgpass file in user's folder (~/.pgpass). File should contain passwords using this format `hostname:port:database:username:password`
# 3. Disallow permissions for world and groups in pgpass file (chmod 0600 ~/.pgpass)

if  [[ "$1" == "-h" || "$1" == "--help" || "$2" != "" || "$1" == "" ]]
then
  echo "${0##*/} user_id

  This script runs another script for all the resulting rows of a DB query.

  Options:
  -h, --help    Display this help and exit"
  exit 0
fi

user_id=$1

psql -h host -d dbname -U dbuser \
  -q -A -t -c "select id from items where id_user='$user;" \
  | xargs -t -L 1 sh ~/path/to/script/script.sh

echo
exit 0