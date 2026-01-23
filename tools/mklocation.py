#!/usr/bin/env python3
#
# Create a YAML template for location oracles to be filled with oraclify.py roll data.
# Works for both territory and theme oracles, as they use the same tables.
#

import sys

if len(sys.argv) < 3:
    print(f"Usage: {sys.argv[0]} <oracle name> <page number>")
    sys.exit(1)
oracle = sys.argv[1]
page = int(sys.argv[2]) # fail hard if you don't give me number

print(f"""
          {oracle}:
            name: {oracle.title()}
            oracle_type: tables
            type: oracle_collection
            summary: |-
            _source:
              <<: *Source
              page: {page}
            contents:
              feature:
                <<: *Feature
                _source:
                  <<: *Source
                  page: {page}
                rows:
                  - roll: {{ min: 91, max: 95 }}
                    <<: *DescriptorFocus
                  - roll: {{ min: 96, max: 100 }}
                    <<: *RollTwice
              hazard:
                <<: *Hazard
                _source:
                  <<: *Source
                  page: {page + 1}
                rows:
                  - roll: {{ min: 89, max: 96 }}
                    <<: *ActionTheme
                  - roll: {{ min: 97, max: 100 }}
                    <<: *RollTwice
              opportunity:
                <<: *Opportunity
                _source:
                  <<: *Source
                  page: {page + 1}
                rows:
                  - roll: {{ min: 89, max: 96 }}
                    <<: *ActionTheme
                  - roll: {{ min: 97, max: 100 }}
                    <<: *RollTwice
""")