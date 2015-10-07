

#Efficient method for computing the greatest common divisor (GCD) of two numbers
def gcd(a,b):

    while a % b != 0 :

        den = a % b
        a = b
        b = den

    return b

print(gcd(125,55))
print(gcd(46,78))

