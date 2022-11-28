
n = int(input("Plz enter number of time you: "))
a = 0
b = 1
print( b ,", " , end="" )
for i in range( n - 1 ):
   c = a + b
   a = b
   b = c
   if i != n - 2:
      print( c ,", " , end="")
   if i == n - 2:
      print(c , end="")
