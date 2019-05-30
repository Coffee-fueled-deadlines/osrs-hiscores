# OSRS Hiscores

## Purpose
  The purpose of this library is to interface with Old School Runescape (OSRS)'s Hiscores page and allow developers to access stat levels, ranks, and experience levels in a more intuitive way (via dictionary).  This library accesses this information via a `http.client` request and parses the information accordingly.
	

## Installation
```
python -m pip install OSRS_HISCORE_WRAPPER
```

## Example Usage
```Python
from OSRS_Hiscores import Hiscores

# User to lookup
username = 'Zezima'

# Initialize user object
user = Hiscores(username)

# Get the entire stat dictionary
user.stats

# Get a specific skill's ranking, level, and experience
user.stats['runecrafting']

# Get skill's level, ranking, and experience separately
user.stats['runecrafting']['level']
user.stats['runecrafting']['rank']
user.stats['runecrafting']['experience']

# A simpler way to just get a skill's level
user.skill('attack')
```
