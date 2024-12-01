#list-Have brackets (Data structures)
movies = ["When Harry Met Sally","The Hangover","The perks of being a Wallflower","The Exorcist"]

print(movies[0])
print(movies[1:3])
print(movies[1:])
print(movies[:1])
print(movies[-1]) #return last item in the list
print(len(movies)) #count items in the list
movies.append("JAWS")
print(movies) #appends to the end of the list

movies.insert(2,"Hustle")
print(movies)

movies.pop() #removes the last item
print(movies)

movies.pop(0)
print(movies)

amber_movies =['Just Go With It','50 First Dates']

our_favourite_movies = movies + amber_movies
print(our_favourite_movies)

grades = [["Bob",82],["Alice",90],["Jeff",73]]
bobs_grade = grades[0][1]
print(bobs_grade)
grades[0][1]=83
print(grades)