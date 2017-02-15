import fresh_tomatoes
import media

"""
  below are all the instances of the class movie for 9 movie objects
  all of this data below will be initialize in the __init__ funtion in the
  media file

"""

michael_clayton = media.Movie("Michael Clayton",
                              "A law firm brings in its 'fixer' to remedy the \
                              situation after a lawyer has a breakdown",
                              "https://upload.wikimedia.org/wikipedia/en/a/a8/Michael_clayton.jpg",  # noqa
                              "https://www.youtube.com/watch?v=5kJRYBhG43Q")

rogue_one = media.Movie("Rogue One",
                        "A mission to steal the plans to the Death Star ",
                        "https://upload.wikimedia.org/wikipedia/en/d/d4/Rogue_One%2C_A_Star_Wars_Story_poster.png",  # noqa
                        "https://www.youtube.com/watch?v=DbwTcXRPyPw")

the_firm = media.Movie("The Firm",
                       "A young lawyer joins a small but prestigious law firm \
                       only to find out that most of their clients are on the \
                       wrong side of the law.",
                       "https://upload.wikimedia.org/wikipedia/en/f/ff/Firm_ver2.jpg",  # noqa
                       "https://www.youtube.com/watch?v=pZdCpriLea8")

the_game = media.Movie("The Game",
                       "There are no rules in 'The Game'. And that will make \
                       life very difficult for Nicholas Van Orton, a successful\
                       businessman who is always in control.",
                       "https://upload.wikimedia.org/wikipedia/en/5/53/TheGame_poster323.jpg",  # noqa
                       "https://www.youtube.com/watch?v=9HTJh4lzAjk")

spectre = media.Movie("Spectre",
                      "A cryptic message from the past leads James Bond \
                      (Daniel Craig) to Mexico City and Rome...",
                      "http://vignette2.wikia.nocookie.net/jamesbond/images/9/95/SPECTRE_poster_1.jpg/revision/latest?cb=20150916083032",  # noqa
                      "https://www.youtube.com/watch?v=7GqClqvlObY")

hero = media.Movie("Hero",
                   "With supernatural skill, a nameless soldier embarks on a \
                   mission of revenge against the fearsome army that massacred \
                   his people.",
                   "https://upload.wikimedia.org/wikipedia/en/0/08/Hero_poster.jpg",  # noqa
                   "https://www.youtube.com/watch?v=MgsddFEe9Oc")

the_dark_knight = media.Movie("The Dark Knight",
                              "When the menace known as the Joker wreaks havoc \
                              and chaos on the people of Gotham.",
                              "https://upload.wikimedia.org/wikipedia/en/8/8a/Dark_Knight.jpg",  # noqa
                              "https://www.youtube.com/watch?v=EXeTwQWrcwY")

jupiter_ascending = media.Movie("Jupiter Ascending",
                                "A young woman discovers her destiny as an\
                                heiress of intergalactic nobility.",
                                "https://upload.wikimedia.org/wikipedia/en/7/76/%27Jupiter_Ascending%27_Theatrical_Poster.jpg",  # noqa
                                "https://www.youtube.com/watch?v=t4ZzMkDLjWI")

batman_v_superman = media.Movie("Batman v Superman",
                                "Fearing that the actions of Superman are left\
                                unchecked, Batman takes on the Man of Steel.",
                                "https://upload.wikimedia.org/wikipedia/en/2/20/Batman_v_Superman_poster.jpg",  # noqa
                                "https://www.youtube.com/watch?v=fis-9Zqu2Ro")

movies = [michael_clayton, rogue_one, the_firm, the_game, spectre,
          hero,the_dark_knight, jupiter_ascending, batman_v_superman]

"""
fresh_tomatoes file contains the all the necessary code to create a movie
website, which includes a open_movies_page function which will takes in the list
from the array and open a website with all the coding movie data from
entertainment_center file.

"""

fresh_tomatoes.open_movies_page(movies)