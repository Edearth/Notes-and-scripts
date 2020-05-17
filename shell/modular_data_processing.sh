#!/bin/sh

# This is a template for modular data-processing-oriented scripting.
#
# It can accept input in 3 different ways:
# * Single parameter: `./script "data"`
# * Reading from a file: `./script -f filepath`
# * Reading from stdin: `cat filepath | ./script -f -`
#
# Example: imagine you have a SQL database with "users" and "transactions" tables. You need to check if a user has any open transaction, and call an HTTP endpoint that closes that transcation. In order to achieve that, you could have these simple individual scripts:
# * Script that runs a SQL query to extract an ID given a username
# * Script that runs a SQL query to extract open transactions given a user ID
# * Script that sends an HTTP request to an endpoint that closes transactions. Or you could easily replace this with something that gets info about those transactions that you need (while keeping the other 2 scripts).
#
# In the end, you get something reusable and modular like this:
# `get_user_id "john" | get_open_transactions -f - | close_transaction -f -`
# And you can re-use them like:
# `get_user_id "john" | get_open_transactions -f - | get_transaction_data -f -`
# `get_user_id "john" | get_referred_users -f -`

function print_usage() {
	>&2 echo "script_name data [-f file]
  
This script does "something" with the input data.
  
Options:
  -f    Instead of using argument input data, you can pass a list of input datas inside a file
  -h    Display this help and exit"
}

function do_something() {
  # Processing goes here
  # Bear in mind, the output of this function will be the output of the script
  echo "> $1"
}


while getopts ":f:h" opt; do
  case ${opt} in
    f )
      input=`cat $OPTARG`
      ;;
    h )
      print_usage
      exit 0
      ;;
    \? )
      >&2 echo "Invalid option: $OPTARG" 1>&2
      ;;
    : )
      >&2 echo "Invalid option: $OPTARG requires an argument" 1>&2
      ;;
  esac
done
shift $((OPTIND -1))

if [ -z "$input" ] ; then
  if [ -z "$1" ] ; then
    >&2 echo "Error: received no parameters"
    print_usage
    exit 0
  fi
  input="$1"
fi


echo "${input}" | while read line
do
  do_something "$line"
done

exit 0
