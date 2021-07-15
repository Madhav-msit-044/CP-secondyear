# trianglearea(s1, s2, s3)[5pts]
# Write the function trianglearea(s1, s2, s3) that takes 3 floats/ints and returns the area of the
# triangle that has those lengths of its side. If no such triangle exists, return 0. Hint: you
# will probably wish to use Heron's Formula.


def trianglearea(s1, s2, s3):
    x = (input(s1))
    y = (input(s2))
    z = (input(s3))
    
    # calculating semiperimeter
    s = (x+y+z)/2
    
    # calculating areaoftriangle
    area = ((s*(s-x)*(s-y)*(s-z))**0.5)
    print (area)
	# your code goes here
	
