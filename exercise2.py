
#creates a dictionary with some people and their characteristics and then prints them through a for loop
petinfo = {"lezzo": "puzza", "pulito": "profuma", "no": "rompe le palle"}

#for pet in petinfo:
#    print (pet + " " + petinfo[pet])
for pet, characteristic in petinfo.items():
    print (pet + " " + characteristic)


people = {"roberto": "Io sono il più bello del mondo", "gianni": "Io sono il più bravo del mondo!!", "Alfredo": "Io sono il più forte del mondo!", "ritardato": "Ciao"}

for person in people:
    print ("Come valuti la tua persona?")
    print (person + ": " + people[person])
