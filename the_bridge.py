class Client():
	"""Client that uses the device"""
	def __init__(self, name):
		self.name = name

class Remote():
	"""Abstraction for all Remote devices"""
	def __init__(self, color, device):
		self.color = color
		self.device = device

	def toggle_power(self):
		pass
		
	def volume_up(self):
		pass

	def volume_down(self):
		pass

	def channel_up():
		pass

	def channel_down(self):
		pass

class Device():
	"""Abstraction for devices"""
	def __init__(self, article_nr):
		self.article_nr = article_nr

	def is_enabled(self):
		pass

	def enable(self):
		pass

	def disable(self):
		pass

	def get_volume(self):
		pass

	def set_volume(self, percentage):
		pass

	def get_channel(self):
		pass

	def set_channel(self):
		pass

	def mute(self):
		pass

class Radio(Device):
	"""Remote device for controlling a radio"""
	def __init__(self, name, article_nr):
		super(Radio, self).__init__(article_nr)
		self.name = name

class TV(Device):
	"""Remote device for controlling a tv"""
	def __init__(self, name, article_nr):
		super(TV, self).__init__(article_nr)
		self.name = name
		

def main():
	lasse = Client("Lasse")
	tv_remote = TV("lemmo", 101321)
	radio_remote = TV("remmo", 102321)
	lemmo = Remote("Blue", tv_remote)
	remmo = Remote("Black", radio_remote)
	lemmo.device.mute()
	print(remmo.device.name)

if __name__ == '__main__':
	main()