class Subscriber():
	"""Subsriber is a class subsribing on a thing the publisher owns advertises."""
	def __init__(self, name):
		self.name = name

	def subscribe(self):
		pass

	def update(self):
		pass


class Publisher():
	"""Publisher publishes """
	def __init__(self, name):
		self.name = name
		self.subscribers = []

	def add_subscriber(self, subsciber_name):
		pass

	def remove_subscriber(self, subsciber_name):
		pass

	def notify_subscriber(self, message):
		for subscriber in self.subscribers:
			subscriber.update()

def main():
	pass

if __name__ == '__main__':
	main()