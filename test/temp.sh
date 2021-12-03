#! /bin/sh

fail () {
    for var in "$@"; do
        echo "$var"
    done

    exit 1
}

check () {
    for var in "$@"; do
        which "$var" || fail_install
    done
}

fail "Please install jq:" "    sudo apt-get install jq"    # For example.

which fail
