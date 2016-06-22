#A list of desserts i like
desserts = ["ice cream", "apple pie", "beef", "carbonara"]
favorite_dessert = "carbonara"

#print the desserts out, but let everyone know my favorite dessert
for dessert in desserts:
    if dessert == favorite_dessert:
        print ("%s is my favorite dessert!!!" % dessert.title())
    else:
        print ("I like %s" % dessert)

