print True and True # True
print False and True # False
print 1 == 1 and 2 == 1 # False
print "test" == "test" # True
print 1 == 1 or 2 != 1 # True
print True and 1==1 # True
print False and 0 != 0 # False
print True or 1 ==1 # True
print "test" == "testing" # F
print 1 != 0 and 2 ==1 # F
print "test" != "testing" # T
print "test" == 1 # F
print not (True and False) # T
print not (1 == 1 and 0 != 1) # F
print not (10 == 1 or 1000 == 1000) # F
print not (1 != 10 or 3 == 4 ) # F
print not ("testing" == "testing" and "Zed" == "Cool Guy") # T
print 1 == 1 and not ("testing" == 1 or 1 == 0) # T
print "chunky" == "bacon" and not (3 == 4 or 3 == 3) # F
print 3 != 4 and not ("testing" != "test" or "Python" == "Python") # F