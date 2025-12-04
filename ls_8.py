from random import randint
massiv = [randint(0,1000) for i in range(10)]
# g =0
for i in range(len(massiv)-1):
   for j in range (len(massiv)-1-i):
    if massiv[j] > massiv[j+1]:
        massiv[j], massiv[j+1] = massiv[j+1], massiv[j]
        #print (massiv)
print (massiv)