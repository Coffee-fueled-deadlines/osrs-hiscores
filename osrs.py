import http.client
from sys import exit

class Hiscores(object):

	def __init__(self, username):
		self.username = username
		self.getHTTPResponse()

	def getHTTPResponse(self):
		conn = http.client.HTTPSConnection('secure.runescape.com')
		conn.request("GET", "/m=hiscore_oldschool/index_lite.ws?player={}".format(self.username))
		self.response = conn.getresponse()
		self.processResponse()

	def processResponse(self):
		self.data = self.response.read().decode('ascii')
		self.parseData()

	def parseData(self):
		try:
			self.data = self.data.replace('\n',',')
			self.data = self.data.split(',')
			subset = {}

			# Totals
			info = {}
			info['rank']             = self.data[0]
			info['total_level']      = self.data[1]
			info['total_experience'] = self.data[2]
			subset['totals']         = info

			# Attack
			info = {}
			info['rank']          = self.data[3]
			info['level']         = self.data[4]
			info['experience']    = self.data[5]
			subset['attack']      = info
			self.attackLevel      = info['level']

			# Defense
			info = {}
			info['rank']          = self.data[6]
			info['level']         = self.data[7]
			info['experience']    = self.data[8]
			subset['defense']     = info
			self.defenseLevel     = info['level']

			# Strength
			info = {}
			info['rank']          = self.data[9]
			info['level']         = self.data[10]
			info['experience']    = self.data[11]
			subset['strength']    = info
			self.strengthLevel    = info['level']

			# Hitpoints
			info = {}
			info['rank']          = self.data[12]
			info['level']         = self.data[13]
			info['experience']    = self.data[14]
			subset['hitpoints']   = info
			self.hitpointsLevel   = info['level']

			# Ranged
			info = {}
			info['rank']          = self.data[15]
			info['level']         = self.data[16]
			info['experience']    = self.data[17]
			subset['ranged']      = info
			self.rangedLevel      = info['level']

			# Prayer
			info = {}
			info['rank']          = self.data[18]
			info['level']         = self.data[19]
			info['experience']    = self.data[20]
			subset['prayer']      = info
			self.prayerLevel      = info['level']

			# Magic
			info = {}
			info['rank']          = self.data[21]
			info['level']         = self.data[22]
			info['experience']    = self.data[23]
			subset['magic']       = info
			self.magicLevel       = info['level']

			# Cooking
			info = {}
			info['rank']          = self.data[24]
			info['level']         = self.data[25]
			info['experience']    = self.data[26]
			subset['cooking']     = info
			self.cookingLevel     = info['level']

			# Woodcutting
			info = {}
			info['rank']          = self.data[27]
			info['level']         = self.data[28]
			info['experience']    = self.data[29]
			subset['woodcutting'] = info
			self.woodcuttingLevel = info['level']

			# Fletching
			info = {}
			info['rank']          = self.data[30]
			info['level']         = self.data[31]
			info['experience']    = self.data[32]
			subset['fletching']   = info
			self.fletchingLevel   = info['level']

			# Fishing
			info = {}
			info['rank']          = self.data[33]
			info['level']         = self.data[34]
			info['experience']    = self.data[35]
			subset['fishing']     = info
			self.fishingLevel     = info['level']

			# Firemaking
			info = {}
			info['rank']          = self.data[36]
			info['level']         = self.data[37]
			info['experience']    = self.data[38]
			subset['firemaking']  = info
			self.firemakingLevel  = info['level']

			# Crafting
			info = {}
			info['rank']          = self.data[39]
			info['level']         = self.data[40]
			info['experience']    = self.data[41]
			subset['crafting']    = info
			self.craftingLevel    = info['level']

			# Smithing
			info = {}
			info['rank']          = self.data[42]
			info['level']         = self.data[43]
			info['experience']    = self.data[44]
			subset['smithing']    = info
			self.smithingLevel    = info['level']

			# Mining
			info = {}
			info['rank']          = self.data[45]
			info['level']         = self.data[46]
			info['experience']    = self.data[47]
			subset['mining']      = info
			self.miningLevel      = info['level']

			# Herblore
			info = {}
			info['rank']          = self.data[48]
			info['level']         = self.data[49]
			info['experience']    = self.data[50]
			subset['herblore']    = info
			self.herbloreLevel    = info['level']

			# Agility
			info = {}
			info['rank']          = self.data[51]
			info['level']         = self.data[52]
			info['experience']    = self.data[53]
			subset['agility']     = info
			self.agilityLevel     = info['level']

			# Thieving
			info = {}
			info['rank']          = self.data[54]
			info['level']         = self.data[55]
			info['experience']    = self.data[56]
			subset['thieving']    = info
			self.thievingLevel    = info['level']

			# Slayer
			info = {}
			info['rank']          = self.data[57]
			info['level']         = self.data[58]
			info['experience']    = self.data[59]
			subset['slayer']      = info
			self.slayerLevel      = info['level']

			# Farming
			info = {}
			info['rank']          = self.data[60]
			info['level']         = self.data[61]
			info['experience']    = self.data[62]
			subset['farming']     = info
			self.farmingLevel     = info['level']

			# Runecrafting
			info = {}
			info['rank']          = self.data[63]
			info['level']         = self.data[64]
			info['experience']    = self.data[65]
			subset['runecrafting']= info
			self.runecraftingLevel= info['level']

			# Hunter
			info = {}
			info['rank']          = self.data[66]
			info['level']         = self.data[67]
			info['experience']    = self.data[68]
			subset['hunter']      = info
			self.hunterLevel      = info['level']

			# Construction
			info = {}
			info['rank']          = self.data[69]
			info['level']         = self.data[70]
			info['experience']    = self.data[71]
			subset['construction']= info
			self.constructionLevel= info['level']

		except Exception as e:
			print('User may be new, may not be a "normal" type account, or may not exist and stats cannot be displayed')
			exit(0)

		# set stats dictionary
		self.stats = subset

	def skill(self,skill):
		try:
			return self.stats[skill.lower()]['level']
		except Exception as e:
			print("ERROR: skill {} does not exist".format(e))
			exit(0)
