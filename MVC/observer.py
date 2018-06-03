class Observer:
	def update(self, obj, *args, **kwargs):
		raise NotImplementedError

class Observable:
	def __init__(self):
		self._observers = []
	def addObserver (self, obs):
		self._observers.append(obs)
	def removeObserver(self,obs):
		self._observers.remove(obs)
	def notifyObserver(self, *args, **kwargs):
		for obs in self._observers:
			obs.update(self, *args, **kwargs)