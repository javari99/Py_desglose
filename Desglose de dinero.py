n = float(input("Introduce la cantidad de dinero a desglosar: "))
#Billetes de 500
a = 0
#Billetes de 200
b = 0
#Billetes de 100
c = 0
#Billetes de 50
d = 0
#Billetes de 20
e = 0
#Billetes de 10
f = 0
#BIllete de 5
g = 0
#Moneda de 2
r = 0
#Moneda de 1
h = 0
#Moneda de 0.50
i = 0
#Moneda de 0.20
j = 0
#Moneda de 0.10
k = 0
#Moneda de 0.05
l = 0
#Moneda de 0.02
m = 0
#Moneda de 0.01
p = 0

if n//500 > 0:
    a = n // 500
    n = n - (a*500)
if n//200 > 0:
    b = n // 200
    n = n - (b*200)
if n//100 > 0:
    c = n // 100
    n = n - (c*100)
if n//50 > 0:
    d = n // 50
    n = n - (d*50)
if n//20 > 0:
    e = n // 20
    n = n - (e*20)
if n//10 > 0:
    f = n // 10
    n = n - (f*10)
if n//5 > 0:
    g = n // 5
    n = n - (g*5)
if n//2 > 0:
    r = n // 2
    n = n - (r*2)
if n//1 > 0:
    h = n // 1
    n = n - (h*1)
if n//0.5 > 0:
    i = n // 0.5
    n = n - (i*0.5)
if n//0.2 > 0:
    j = n // 0.2
    n = n - (j*0.2)
if n//0.1 > 0:
    k = n // 0.1
    n = n - (k*0.1)
if n//0.05 > 0:
    l = n // 0.05
    n = n - (l*0.05)
if n//0.02 > 0:
    m = n // 0.02
    n = n - (m*0.02)
if n//0.01 > 0:
    p = n // 0.01
    n = n - (p*0.01)
print("Esta cantidad contiene:",a,"Billetes de 500,",b,"Billetes de 200,",c,"Billetes de 100,",d,"Billetes de 50,",e,"Billetes de 20,",f,"Billetes de 10,",g,"Billetes de 5,",r,"monedas de 2,",h,"Monedas de 1,",i,"Monedas de 0.50,",j,"Monedas de 0.20,",k,"Monedas de 0.10,",l,"Monedas de 0.05,",m,"Monedas de 0.02,",p,"Monedas de 0.01")