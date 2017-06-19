pi=4
x=4
z=3
y=1

while y<10000:
    y=y+1
    pi=pi-(x/z)
    print (pi)
    z=z+2
    pi=pi+(x/z)
    z=z+2
    print (pi)
