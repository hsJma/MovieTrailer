import webbrowser

class Movie():
	""" Base class to store movie information. 

	Attributes:
		title: A string
		storyline: A string description of movie
		poster_image_url: A string 
		trailer_youtube_url: A string
	"""
	def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
		self.title = movie_title
		self.storyline = movie_storyline
		self.poster_image_url = poster_image
		self.trailer_youtube_url = trailer_youtube

	def show_trailer(self):
		webbrowser.open(self.trailer_youtube_url)