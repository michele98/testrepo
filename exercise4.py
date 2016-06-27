#slide 84

#three is a crowd

namelist = ["dio", "gesu", "maria", "giuseppe"]

def crowd_test ():
    if len(namelist)>3:
        print ("AAAAAAAAAAAHHH!")
        namelist.pop()
        namelist.pop()
    else:
        print ("bravo")

crowd_test()
crowd_test()

namelist.extend (["salve", "idiota", "eh la miseria", "maccheccazzo"])

if len(namelist) > 5:
    print ("AAAAAAAAAAAAAAAAAAAUAAOOOAAAAHHHAAAAAOOOOAAAAA!")
elif len (namelist) > 3 and len(namelist) < 5:
    print ("AAAAAAAAAAAHHH!")
elif len (namelist) >=1 and len(namelist) <= 2:
    print ("it's ok!")
else:
    print ("Ah so boring!")
