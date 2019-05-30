# OSRS Hiscores Wrapper

## Purpose
  The purpose of this Wrapper is to allow for developers to easily access user stats that are recorded and displayed on secure.runescape.com's 'Hiscores' page.  This wrapper neatly packages the skills into an easy to use dictionary.  In addition, additional functionality is added for simple level lookups.
	
	
## Example Usage
```Python
import osrs-hiscores-wrapper

# User to lookup
username = 'Zezima'

# Initialize user object
user = Hiscores(username)

# Get the entire stat dictionary
user.stats

# Get a specific skill's ranking, level, and experience
user.stats['runecrafting']

# Get skill's level, ranking, and experience separately
user.stats['runcrafting']['level']
user.stats['runcrafting']['rank']
user.stats['runcrafting']['experience']

# A simpler way to just get a skill's level
user.skill('attack')
```