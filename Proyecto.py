num = []
totalS = 0
totalE = 0
totalO = 0 
can = int(input("Cantidad de Numeros:  "))

for i in range(can):
     num.append(int( input("Digite sus Numeros: ") ))
     
print("Sus numeros elegidos Son: ", num)
    
for i in range(len(num)):
    totalS = num[i] + totalS
    
print("La sumatoria de los numeros es: ", totalS)

for i in range(0 ,len(num), 2):
    totalE = num[i] + totalE
    
print("La sumatoria de los numeros pares son: ", totalE)

for i in range(1, len(num), 2):
    totalO = num[i] + totalO
    
print("La sumatoria de los numeros Odd son: ", totalO)
for i in range(0, len(num), 2):
    totalO = num[i] + totalO
