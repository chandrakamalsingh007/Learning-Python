my_name = "Chandra"
print(my_name[0]) #first letter
print(my_name[-1] ) #last letter

sentence = "This is a sentence."
print(sentence[:4])
print(sentence.split()) #delimeter -default is space

sentence_split=sentence.split()
sentence_join = ' '.join(sentence_split)

quote="He said, 'give me all your money'"
print(quote)
quote= "He said, \"give me all your money\""
print(quote)

too_much_space = "          hello     "
print(too_much_space.strip())
print("A" in "Apple") #True
print("a" in "Apple") #False
letter="A"
word = "Apple"

print(letter.lower() in word.lower()) #improved


movie = "The Hangover"
print("My favourite movie is {}.".format(movie))
print("My favorite movie is %s." %movie)
print(f"My favorite movie is {movie}.")