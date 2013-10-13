import sfml as sf


class Entity(sf.Drawable):
	def __init__(self):
		sf.Drawable.__init__(self)
		self._transformable = sf.Transformable()
		self.shape = sf.RectangleShape()
	
	def draw(self, target, states):
		states.transform.combine(self._transformable.transform)

		target.draw(body)
		target.draw(clothes)

	def getposition(self):
		return self._transfomable.position

	def setposition(self, position):
		self._transformable.position = position

	def setsize(self,size):
		self._transfolrmable.size = size

	
window = sf.Window(sf.VideoMode(800, 600),'Game')
window.framerate_limit = 60
ground = Entity()
ground.setposition((0,750))
while window.is_open:
	for event in window.events:
		if type(event) is sf.CloseEvent:
				window.close()
		window.active=True

		window.display()
