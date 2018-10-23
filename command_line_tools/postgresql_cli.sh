#!/bin/bash

#Instructions to use this script:
# 1. Install PostgreSQL (Mac: brew update && brew doctor && brew install postgresql)
# 2. Create pgpass file in user's folder (~/.pgpass). File should contain passwords using this format `hostname:port:database:username:password`
# 3. Disallow permissions for world and groups in pgpass file (chmod 0600 ~/.pgpass)

psql -h host -d database -U user \
  -q -A -t -c "SELECT id FROM users WHERE username='patata';"
