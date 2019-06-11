name = "OSRS_Hiscores"

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
			info['level']      = self.data[1]
			info['experience'] = self.data[2]
			subset['total']         = info

			skills = [
				  'attack',
			          'defense',
			          'strength',
			          'hitpoints',
			          'ranged',
			          'prayer',
			          'magic',
			          'cooking',
			          'woodcutting',
			          'fletching',
			          'fishing',
			          'firemaking',
			          'crafting',
			          'smithing',
			          'mining',
			          'herblore',
			          'agility',
			          'thieving',
			          'slayer',
			          'farming',
			          'runecrafting',
			          'hunter',
			          'construction'
			           ]
			counter = 0
			for i in range(len(skills)):
				info = {}
				info['rank']       = self.data[counter+3]
				info['level']      = self.data[counter+4]
				info['experience'] = self.data[counter+5]
				subset[skills[i]] = info
				counter += 3
		except IndexError as IE:
			print("ERROR: issue with OSRS Hiscores API -- {}".format(IE))
			print("OSRS Hiscores currently only works with Normal type accounts.")

		# set stats dictionary
		self.stats = subset

	def skill(self,skill):
		try:
			return self.stats[skill.lower()]['level']
		except KeyError as KE:
			print("ERROR: skill {} does not exist".format(KE))
			exit(0)
