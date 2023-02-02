import spacy  # importing spacy
nlp = spacy.load('en_core_web_md') # specifying the model we want to use. 

# Movie class defined, takes in title and description - with get_title and get_description methods defined
class Movie:

    def __init__(self, title, description):
        self.title = title
        self.decription = description

    def get_title(self):
        return self.title

    def get_description(self):
        return self.decription

#==========Functions outside the class==============
# movie_list() function - try/except used for FileNotFoundEror
# With block opens the mpvies.txt file and readlines() saves it to movies
# for loop iterates over each line in movies - which is split at : and strip to remove ; into title and decription
# the index of each item is used to populate the parameters of the Movie class, creating a Movie object which is appended to the movie_list

movie_list = []
def list_movies():
    '''
    list_movies() function opens the file movies.txt
    reads the data from the file, split() at :, strip()
    and appends index 1 to the movies_description list
    '''
    try:
        with open("movies.txt", "r") as movie_file:
            movies = movie_file.readlines()
    except FileNotFoundError:
        print("The file you are trying to open does not exist")
    for line in movies:
        split_line = line.strip().split(":")
        movie_object = Movie(split_line[0], split_line[1])
        movie_list.append(movie_object)

# Function called to get the movie data into objects in the movie_list
list_movies()

# Movie description to compare assigned to the variable description_to_compare
description_to_compare = """Will he save their world or destroy it? When the Hulk becomes too dangerous 
for the Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the
Hulk can live in peace. Unfortunately, Hulk land on the planet Sakar where he is sold into slavery
and trained as a gladiator."""

# description_to_compare is nlp() and assigned to model_description variable
model_description = nlp(description_to_compare)

# Empty dictionary called
# For loop iterates over each movie object in the movie_list
# get_description() and get_title() methods called and assigned to variables description and title
# similarity between the model_description and the movie object description is found
# The movie title is added as a key and the similarity as a value to the empty similarity_dict dictionary
# The key for the maximum value in the dictionary is found and assidned to the variable max_tital and this is printed
similarity_dict = {}

for movie in movie_list:
    description = movie.get_description()
    title = movie.get_title()
    similarity = nlp(description).similarity(model_description)
    similarity_dict[title] = similarity

max_title = max(similarity_dict, key=similarity_dict.get)

print(f"The most similar movie to Planet Hulk is: {max_title}")
