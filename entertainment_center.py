"""entertainment_center.py: 
   Using movie information to create a movie trailer page."""

import media
import fresh_tomatoes

mr_nobody = media.Movie('Mr. Nobody',
	                    'Multiple outcomes from multiple choices',
	                    'https://upload.wikimedia.org/wikipedia/en/thumb/3/32/Mr._Nobody_%28film_poster%29.jpg/220px-Mr._Nobody_%28film_poster%29.jpg',   # noqa
	                    'https://www.youtube.com/watch?v=mpi0qsp3v_w',
	                    7.9)

lego_movie = media.Movie('The Lego Movie',
	                     'Basically an AWESOME Lego Ad',
	                     'https://upload.wikimedia.org/wikipedia/en/thumb/1/10/The_Lego_Movie_poster.jpg/220px-The_Lego_Movie_poster.jpg',  # noqa
	                     'https://www.youtube.com/watch?v=fZ_JOBCLF-I',
	                     7.8)

notting_hill = media.Movie('Notting Hill',
	                       'Love story between superstar and bookstore owner',
	                       'https://upload.wikimedia.org/wikipedia/en/thumb/3/38/NottingHillRobertsGrant.jpg/220px-NottingHillRobertsGrant.jpg',    # noqa
	                       'https://www.youtube.com/watch?v=Ig_88q9M3SU',
	                       7.0)

fight_club = media.Movie('Fight Club',
	                     'A club in which everyone fights',
	                     'https://upload.wikimedia.org/wikipedia/en/thumb/f/fc/Fight_Club_poster.jpg/220px-Fight_Club_poster.jpg',    # noqa
	                     'https://www.youtube.com/watch?v=SUXWAEX2jlg',
	                     8.9)


movies = [mr_nobody, lego_movie, notting_hill, fight_club]
fresh_tomatoes.open_movies_page(movies)
