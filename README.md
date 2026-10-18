> [!NOTE]
> The Revenant ruleset is now part of the [Datasworn community content repository](https://github.com/datasworn-community/community-content) and this repository is no longer active.

---

# Revenant Datasworn

[Datasworn](https://github.com/rsek/datasworn/tree/v0.1.0) source data for [Revenant](https://www.drivethrurpg.com/en/product/457762/revenant), a [Starforged](https://tomkinpress.com/pages/ironsworn-starforged)-based post-apocalyptic solo TTRPG created by Killian Gillespie.

This repository is mainly used while creating the YAML source data, but the goal is to eventually merge it into the actual Datasworn repository.

For [Iron Vault](https://ironvault.quest/) users, both the YAML files and JSON release can be used as-is as a [Homebrew ruleset](https://ironvault.quest/other-features/rulesets-and-homebrew.html).

## Content

- [`source_data`](source_data) - all the YAML files defining the Revenant ruleset for Datasworn. This is most likely what you're here for.
- [`tools`](tools) - a few scripts that were used to get the book content extracted and processed. This is likely of little interest to anyone else.

## Data

Some details about the [`source_data`](source_data) content itself.

Most of it is straightforward and in the same fashion and layout as all other Datasworn source data:

- [`rules.yaml`](source_data/rules.yaml) - defines the basic ruleset and anything that would end up on the character sheet (stats, tracks, meters, impacts).
- [`moves.yaml`](source_data/moves.yaml) - defines all the moves.
- [`npcs.yaml`](source_data/npcs.yaml) - defines all the NPCs mentioned in the book, along with pack and group variants.
- [`oracles/`](source_data/oracles) - define all the oracles the book has.

Some are worth a few extra words, though:

- `truths.yaml` - does **not** exist as Revenant doesn't define a set of truths to build the world from like Starforged etc.
- [`assets.yaml`](source_data/assets.yaml) - defines asset cards to add to a character, except Revenant itself doesn't really have assets. The only asset-like things in it are a _vehicle_ and a _companion_, all else is defined by custom _talents_.
  It does, however, have a few optional rules (_immunity_, _vectors_, _carriers_) that affect some of the moves, so I decided to add those in the style of assets as well.

## License
This work is based on [Revenant](https://www.drivethrurpg.com/en/product/457762/revenant) by Killian Gillespie licensed under the [Creative Commons Attribution-ShareAlike 4.0 International license](https://creativecommons.org/licenses/by-sa/4.0/).

All YAML content and JSON release files are licensed under the [Creative Commons Attribution-ShareAlike 4.0 International license](https://creativecommons.org/licenses/by-sa/4.0/).
See [`LICENSE`](LICENSE) for the full text.

Source code found in [`tools/`](tools) is released under the MIT license.
