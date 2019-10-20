#!/usr/bin/env python

"""
This program takes a raw dump of the CDC's list of parasite names and parses
it. It then assigns a random type to each parasite (like pokemon) and
generates a pokedex style CSV file.
"""

import csv
import random

__filename__ = "parasites.py"
__author__ = "Trevor Michael Tomesh"
__copyright__ = "Copyright 2019, Trevor M. Tomesh"
__credits__ = "Trevor M. Tomesh"
__license__ = "GPL"
__version__ = "0.0.1"
__maintainer__ = "Trevor M. Tomesh"
__email__ = "tmtomesh@gmail.com"


def main():
    f = open("parasites.txt", "r")

    # The following list comprehension strips off new-lines
    # excludes category headers and 'Back To Top' string
    rawBugs = [bug.rstrip('\n') for bug in f.readlines()
               if len(bug) > 2 and "Back To Top" not in bug]
    f.close()

    writeBugs = getTypes(rawBugs)
    writeCSV(writeBugs)


def writeCSV(bugs):
    """Try to open new or existing CSV file and write bugs."""
    try:
        with open('parasites.csv', 'w') as writeFile:
            writer = csv.writer(writeFile)
            writer.writerows(bugs)
        print("Writing to " + str(writeFile.name) + " was successful!")
        writeFile.close()

    except Exception as exp:
        print("The following error occurred: " + str(exp))


def getTypes(parasites):
    """Take parasites and assign a type to them -- like in pokemon! Then
    return the list of parasites."""
    bugsOut = []
    for i in range(len(parasites)):
        bugsOut.append([i+1, parasites[i],
                        random.choice(["fire", "water", "grass"])])
    return bugsOut


main()
