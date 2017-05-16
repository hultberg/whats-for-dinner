# -*- coding: utf-8 -*-

import random, re, json, os, sys, getopt
from urllib.request import urlopen

# Keep track of chosen dinners.
debug = False
source = ''
weekdays = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thuesday",
    "Friday",
    "Saturday",
    "Sunday"
]


##
# Provides the dinners as JSON from source.
##
def get_dinners(source):
    # Fetches the dinner source. A source is a json file containing a string for each day.
    # Example: [ "Dinner #1", "Dinner #2" ] or objects: [ { name: "Dinner name" } ]
    content = ''

    # Test if we must download the source.
    # Only check some protocols, as files on the fs can be named "dinners.json"
    if re.match('(htt|ft)(p|ps):\/\/', source):
        if debug:
            print("> Downloading source " + source)

        # The source is a URL, must download it if I can.
        content = urlopen(source).read()
    else:
        if debug:
            print("> Reading source " + source)

        content = open(source, 'r').read()

    # Finally, parse the content as json.
    return json.loads(content)


def get_dinner_for_day(dinners, day):
    # Attempt to find a dinner randomly.
    # This might hang forever if no dinners are ever found.
    while True:
        try:
            return dinners[random.randint(1, len(dinners))]
        except IndexError:
            pass

    return None


def usage():
    print("Whats-for-dinner, determine whats for dinner from a json source.")
    print("Usage: whats-for-dinner.py -s [source]")


# Main script
if __name__ == '__main__':
    try:
        opts, args = getopt.getopt(sys.argv[1:], 's:d', ['source=', 'debug', 'help'])
    except getopt.GetoptError:
        usage()
        sys.exit(2)

    for opt, arg in opts:
        if opt in ('-h', '--help'):
            usage()
            sys.exit(2)

        # Debug flag.
        if opt in ('-d', '--debug'):
            debug = True

        if opt in ('-s', '--source'):
            source = arg

    if len(source) < 1:
        print("Missing source.")
        usage()
        sys.exit(1)

    dinners = get_dinners(source=source)

    print("")
    print("Dinners:")
    
    for number, weekday in enumerate(weekdays):
        print("> " + weekday + ": " + get_dinner_for_day(dinners=dinners, day=number))
