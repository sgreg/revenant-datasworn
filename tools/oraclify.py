#!/usr/bin/env python3
#
# Create YAML oracle row text from extracted PDF text data
#
# Takes a .txt file created from extract.sh, parses it as oracle roll data,
# builds a dict from it, and dumps it as YAML data.
# The resulting text can be copied as-is to replace oracle rows entries.
#
# Accepts an optional i18n part_of_speech value.
#

import re
import sys
import yaml

if len(sys.argv) < 2:
    print(f"Usage: {sys.argv[0]} <input file>")
    sys.exit(1)
filename = sys.argv[1]

speech_type = None
if len(sys.argv) > 2:
    speech_type = {'_i18n': {'text': {'part_of_speech': sys.argv[2]}}}


with open(filename, "r", encoding="utf-8") as input_file:
    text = input_file.read()


# Define a custom dict type for `roll: { min: x, max: y }` entries, to tweak
# its dump output to use flow_style and have it with the curly braces, rather
# than having min and max on individual, indented lines.
class RollDict(dict):
    pass

# Do the output tweaking part
def roll_dict_representer(dumper, roll_dict):
    return dumper.represent_mapping('tag:yaml.org,2002:map', roll_dict.items(), flow_style=True)

yaml.add_representer(RollDict, roll_dict_representer, Dumper=yaml.SafeDumper)


roll_data = {}
for line in text.split("\n"):
    if match := re.search(r"^(\d+) (.*)$", line):
        roll_min = roll_max = int(match.group(1))
        text = match.group(2)
    elif match := re.search(r"^(\d{2})-(\d{2}) (.*)$", line):
        roll_min = int(match.group(1))
        roll_max = int(match.group(2))
        text = match.group(3)
    else:
        continue

    if roll_min == 0:
        roll_min = 100
    if roll_max == 0:
        roll_max = 100

    roll_data[roll_min] = [roll_min, roll_max, text]


roll_entries = []
for roll in sorted(roll_data.values()):

    data = {
        'roll': RollDict({
            'min': roll[0],
            'max': roll[1],
        }),
        'text': roll[2],
    }

    if speech_type is not None:
        data = speech_type | data

    roll_entries.append(data)


yaml.safe_dump(roll_entries, sys.stdout, default_flow_style=False, sort_keys=False)
