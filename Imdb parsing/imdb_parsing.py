
# Read the genres.list file and parse the movie data into the dictionary
def readGenre():
	p = 0
	with open("genres.list",'r') as file:
		for line in file:
			line = line.strip(" ")
			line = line.split(")")
			movie_genre = line[-1].split("\t")
			movie_genre = movie_genre[-1].strip(" ").strip("\n")
			line = line[0].split("(")
			movie_name = line[0]
			movie_year = line[1]
			movie[movie_name]={"Genre": movie_genre, "Year": movie_year}
			p = p + 1	
			if (p > 50):
				break

# Read the ratings.list file and parse the movie data into the dictionary
def readRatings():
	p = 0
	with open("ratings.list",'r') as file:
		for line in file:
			line = line.strip()
			line = line.split("\t")[0].split("   ")
			line = line[1].split("  ")
			movie_name = line[1]
			movie_name = movie_name[:movie_name.index("(")].strip(" ")
			movie_rank = line[0]
			movie[movie_name] = {"Rank": movie_rank}
			p = p + 1
			if (p > 50):
				break

def main():
	readGenre()
	readRatings()

# The dictionary to store the movie data
movie = {}
main()
print(movie)