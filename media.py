# Class that will be imported by entertainment_center.py file

import webbrowser   # importing the webbrowser function 

# creating our Movie class
class Movie():

# document of the class if needed 
    """ This class provides a way to store movie related information"""

# A constant function that will display the valid ratings for the movies.
    VALID_RATINGS = ["G", "PG", "PG-13", "R"]   # good to capitalize constant. Value of the variable probably isn't going to change in awhile 

# initializing information that we want to display to the user
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

# opens the webbrowser showing the trailer for a movie
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)

