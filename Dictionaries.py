#Dictionaries-key/value pairs {}

drinks = {"White Russian":7, "Old Fashioned":10, "Lemon Drop":8} #drink is the key, price is the key value
print(drinks)

employees= {"Finance": ["Bob","Linda","Linda","Tina"],"IT":["Gene","Louise"],"HR":["Jimmy sir","Mort"]}
print(employees)

employees['legal']= ["Mr.Fond"] #adds new key:value pair
print(employees)

employees.update({"sales":["Andie","ollie"]})
print(employees)

drinks["White Russian"] = 8
print(drinks)


print(drinks.get("white Russian"))