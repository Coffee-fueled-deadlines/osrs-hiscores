import http.client

class hiscore(object):

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
		self.parseData

	def parseData(self):
		self.data = self.data.replace('\n',',')
		self.data = self.data.split(',')
		container = {}
		subset = {}

		# Totals
		info = {}
		info['rank']             = self.data[0]
		info['total_level']      = self.data[1]
		info['total_experience'] = self.data[2]
		subset['totals']         = info

		# Attack
		info = {}
		info['rank']       = self.data[3]
		info['level']      = self.data[4]
		info['experience'] = self.data[5]
		subset['attack']   = info
		self.attackLevel   = info['level']

		# Defense
		info = {}
		info['rank']       = self.data[6]
		info['level']      = self.data[7]
		info['experience'] = self.data[8]
		subset['defense']  = info
		self.defenseLevel  = info['level']

		# Strength
		info = {}
		info['rank']       = self.data[9]
		info['level']      = self.data[10]
		info['experience'] = self.data[11]
		subset['strength'] = info
		self.strengthLevel = info['level']

		# Hitpoints
		info = {}
		info['rank']        = self.data[12]
		info['level']       = self.data[13]
		info['experience']  = self.data[14]
		subset['hitpoints'] = info
		self.hitpointsLevel = info['level']

		# Ranged
		info = {}
		info['rank']        = self.data[15]
		info['level']       = self.data[16]
		info['experience']  = self.data[17]
		subset['ranged']    = info
		self.rangedLevel    = info['level']

		# Prayer
		info = {}
		info['rank']        = self.data[18]
		info['level']       = self.data[19]
		info['experience']  = self.data[20]
		subset['prayer']    = info
		self.prayerLevel    = info['level']

		# Magic
		info = {}
		info['rank']       = self.data[21]
		info['level']      = self.data[22]
		info['experience'] = self.data[23]
		subset['magic']    = info
		self.magicLevel    = info['level']






