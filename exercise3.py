#slide 77: list comprehension

#multiplies of ten
print ("multiplies of ten")

#creates a list with list comprehension in which it multiplies those numers by 10
multlist = [i*10 for i in range (1,11)]
print (multlist)



#cubes
print ("lezzo cubes")

#creates a list with list comprehension in which it cubes those numbers
cubelist = [i**3 for i in range (1,11)]
print (cubelist)



#Awesomeness
print ("I am awesome!!!!!")
# I create a list of names
namelist = ["michele", "matteo", "alessia", "stefania", "leonardogaycapodegliebrei"]
# I loop through each name in the list and add the string "is awesome"
awesomelist = [name + " is awesome" for name in namelist]
print (awesomelist)


#Working Backwards
print ("backwards")
"""
I have to write as non list comprehension the following line of code
plus_thirteen = [number + 13 for number in range(1,11)] 
"""
numlist = range (1,11)
plus_thirteen = [number + 13 for number in numlist]
print (plus_thirteen)
