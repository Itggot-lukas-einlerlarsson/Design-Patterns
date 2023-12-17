class Subscriber():
	"""Subsriber is a class subsribing on a thing the publisher owns advertises."""
	def __init__(self, name):
		self.name = name
		self.sublist = []

	def update(self, message):
		print(f"{self.name} got the update! tha message:{message}")


class Publisher():
	"""Publisher publishes and updates to subscribers."""
	def __init__(self, name):
		self.name = name
		self.subscribers = []

	def add_subscriber(self, subscriber):
		self.subscribers.append(subscriber)
		subscriber.sublist.append(self.name)

	def remove_subscriber(self, subscriber):
		self.subscribers.pop(subscriber)
		subscriber.sublist.pop(self.name)

	def _notify_subscriber(self, message):
		for subscriber in self.subscribers:
			subscriber.update(message)

def main():
	mac = Subscriber("Mac")
	dac = Subscriber("Dac")
	sac = Subscriber("Sac")
	cac = Subscriber("Cac")
	
	artie = Publisher("Artie")
	artie.add_subscriber(mac)
	artie.add_subscriber(dac)
	artie.add_subscriber(sac)
	artie.add_subscriber(cac)

	artie._notify_subscriber("Mellandagsrea, upp till 50% rabatt!!!* | *detta är ett skämt. Sax 10% rabatt. Sry!")


if __name__ == '__main__':
	main()