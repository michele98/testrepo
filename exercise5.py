#slide 99 and 100
#dictionaries
#haha it's the same  as exercise 2 but I do it anyways

#Pet names
petinfo = {"god": "dog", "idiot": "mouse", "scemo": "cat", "leonardo": "coglione"}
for name, animal in petinfo.items():
    print ("%s is a %s" %(name, animal))
print ("\n")

#Polling friends
dictionary = {"leonardo": "sono un pelato", "matteo": "la famigghia!!", "michele": "I miei occhiali nooooo", "che nome metto": "che risposta metto"}

for name, answer in dictionary.items():
    print (name + ":\t" + answer)
print ("\n")

#mountain heights
mountaininfo = {"Everest": 8848, "K2": 8611, "Kangchenjunga": 8586, "Lhtose": 8516, "Makalu": 8485}

for name in mountaininfo:
    print (name)
for height in mountaininfo.values():
    print (height)
for name, height in sorted(mountaininfo.items()):
    print ("%s is %d m tall" %(name, height))
