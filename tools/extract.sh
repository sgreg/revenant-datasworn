#!/bin/bash
#
# Convert individual page(s) from the Revenant PDF to text using pdftotext.
# 
# Usages:
#   ./extract.sh 277 action.txt
#   ./extract.sh 283-288 names.txt
#
# Writes all debug and error information to stderr.
# Writes the output file's absolute path to stdour.
# This allows to pipe the file name to e.g. the clipboard or wherever.
# e.g.
#   ./extract.sh 277 action.txt |xsel -ib
#

#PDF="/home/sven/dump/ttrpg/Ironsworn Supplements/Revenant/Revenant_-_Digital_(pages)_without_background.pdf"
PDF="/tmp/revenant/revenant.pdf"

if [ ! -f "$PDF" ] ; then
    echo "Error: source file $PDF not found" >&2
    exit 1
fi

if [ $# != 2 ] ; then
    echo "Usage: $0 <first page[-<last page>]> <output file>" >&2
    exit 1
fi

pages="$1"
outfile="$2"

# Match "<digits>" and "<digits>-<digits>"
#
# Example: "123" and "123-456"
# Match groups:
#  in: "123"    "123-456"
#   1: "123"    "123"
#   2: ""       "-456"
#   3: ""       "456"
re='^([0-9]+)(-([0-9]+))?$'

if ! [[ $pages =~ $re ]] ; then
    echo "Error: invalid page selection parameter" >&2
    exit 1
fi

first="${BASH_REMATCH[1]}"
last="${BASH_REMATCH[3]:-$first}"

if [ -e "$outfile" ] ; then
    read -p "Warning: output file $outfile exists. Overwrite? [y|N] " overwrite
    if [ "${overwrite,,}" != "y" ] ; then
        echo "Aborting" >&2
        exit 2
    fi
fi

echo "Extracting p$pages from $PDF to $outfile" >&2
pdftotext -f $first -l $last "$PDF" "$outfile" && (echo "" ; ls -l $outfile) >&2
readlink -f $outfile

