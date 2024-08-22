a = int(input("Enter the number of rows :"))
b= int(input("Enter the number of columns :"))
X = []
val =[]
for i in range (0,a) :
    for j in range (0,b) :
        val.insert(j, int(input("Enter the %d * %d element" %(i,j))))
    X.insert(i,val)
    val = []
Y = []
val =[]
for i in range (0,a) :
    for j in range (0,b) :
        val.insert(j, int(input("Enter the %d * %d element" %(i,j))))
    Y.insert(i,val)
    val = []
sum = []
for i in range(0,a) :
    for j in range(0,b) :
        val.insert(b, X[i][j] + Y[i][j])
    sum.insert(i,val)
    val = []
print(sum)



