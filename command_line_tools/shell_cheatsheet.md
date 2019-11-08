
### Run multiple commands in one line

```
A; B    # Run A and then B, regardless of success of A
A && B  # Run B if and only if A succeeded
A || B  # Run B if and only if A failed
A &     # Run A in background.
```

### Getting named parameters value (-key val)

Putting a colon after the parameter allows you to signal that it requires a value after it. The colon before all others parameters disables error reporting (but you still have the last 2 cases to handle errors, invalid option and missing argument).

```sh
while getopts ":k:h" opt; do
  case ${opt} in
    k )
      input="$OPTARG"
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
``` 

It's important to shift the argument pointer at the end so that the $# doesn't show already read arguments. This way you can do something like ./script.sh -a 1 -b 2 "extra" "arguments", reading arguments "a" and "b" with getopts and the other 2 with $1 and $2.

Also, try to validate your input is correct and show appropiate error messages when possible:

```sh
if [ -z "$1" ] ; then
  >&2 echo "Error: received no parameters"
  print_usage
  exit 0
fi
```

