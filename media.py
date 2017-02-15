import webbrowser

#  class movie with all the necessary instance variables data


class Movie():

    # the __init__ function create space in memory for all the 'self.' data

    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube):

        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

#  the instance method that will open a webbrowser
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
        
  