#programa que calcula la suma de los primeros "n" numeros pares

N=input("Ingresa un numero: ")
N=int(N)
lista=list(range(1,N+1))
lista2=[i*2 for i in lista]
suma=sum(lista2)
print(suma)
