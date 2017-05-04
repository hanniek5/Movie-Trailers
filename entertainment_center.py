# Movie-Trailers

import media        #importing the file "media.py"
import fresh_tomatoes       # importing the fresh_tomatoes file

# providing the movie title, storyline, poster image, and trailer URL
toy_story = media.Movie("Toy Story", "A story of a boy and his toys that come to life.",
                        "https://upload.wikimedia.org/wikipedia/commons/0/0a/Toy_Story_logo.svg"
                        ,"https://www.youtube.com/watch?v=KYz2wyBy3kc")
                        
# providing the movie title, storyline, poster image, and trailer URL
avatar = media.Movie("Avatar", "Marine on an alien planet"
                      , """http://t0.gstatic.com/images?q=tbn:ANd9GcQCfmvrE4fMo2cd8esc7mDZPtFSJThAujddMPkRtti1_ij6u-jp"""
                     , "https://www.youtube.com/watch?v=d1_JBMrrYw8")
                     
# providing the movie title, storyline, poster image, and trailer URL
wanted = media.Movie("Wanted", "Man who discoveres his skill as an assassin."
                     , "http://www.gstatic.com/tv/thumb/movieposters/172810/p172810_p_v8_an.jpg"
                     , "https://www.youtube.com/watch?v=edpEspHOeVU")

# providing the movie title, storyline, poster image, and trailer URL
ninja_assassin = media.Movie("Ninja Assassin", "Ninja Raised to Become an Assassin"
                             , """http://t2.gstatic.com/images?q=tbn:ANd9GcSZL3_zAx2ygtj
                             -kOs_EfeRK0f5cOaW0PigZklnCwPPXyh5QpWJ"""
                             , "https://www.youtube.com/watch?v=NhYH26KTNbQ")

# providing the movie title, storyline, poster image, and trailer URL
avengers = media.Movie("Avengers", "Teamwork of Superheroes"
                       , "http://t1.gstatic.com/images?q=tbn:ANd9GcTp0qlAoWcOOswIkL_qpjYzJqCCDmWXiBzCXiqbE43Obo8c0Z-s"
                       , "https://www.youtube.com/watch?v=eOrNdBpGMv8")

# providing the movie title, storyline, poster image, and trailer URL
happy_feet = media.Movie("Happy Feet", "One Dancing Penguin Spreading Happy Feet"
                         , """https://images-na.ssl-images-amazon.com/images/M/MV5BMTQyNTkxMjUwMV5BMl5BanBnXkFtZTcwMDQ2NTU0MQ@@._V1_UY1200_CR90,0,630,1200_AL_.jpg"""
                         , "https://www.youtube.com/watch?v=hFUC5adf8FE")
# Creating the list of our selected movies                          
movieslist = [toy_story, avatar, wanted, ninja_assassin, avengers, happy_feet]

# opening the fresh_tomatoes file and open_movies_page function to apply it with our movies list
fresh_tomatoes.open_movies_page(movieslist)
