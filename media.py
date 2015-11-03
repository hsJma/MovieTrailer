import webbrowser


class Movie():
	""" Base class to store movie information. 

	Attributes:
		title: A string
		storyline: A string description of movie
		poster_image_url: A string 
		trailer_youtube_url: A string
		imdb_rating: A float rating from 1.0 to 10.0
	"""
	def __init__(self, movie_title, movie_storyline, poster_image, 
		         trailer_youtube, imdb_score):
		self.title = movie_title
		self.storyline = movie_storyline
		self.poster_image_url = poster_image
		self.trailer_youtube_url = trailer_youtube
		self.imdb_rating = imdb_score

	def show_trailer(self):
		webbrowser.open(self.trailer_youtube_url)
