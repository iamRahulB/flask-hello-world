from discordwebhook import Discord

class Disnotify:

	def __init__(self,content=None):
		self.content=content


	def notification(self,name):
		self.name=name
		discord = Discord(url="https://discord.com/api/webhooks/1105962198985080923/q6y3s1cGvpJHo-oNomPc-OlBzYCMin2cMOSNO8cRGEV8UXR13QkTLYaOeitUGjPQzvSv")
		discord.post(content=f"{name} has clicked on check here")
		