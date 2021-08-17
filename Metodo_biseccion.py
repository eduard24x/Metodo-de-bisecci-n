from math import *
def f(x):
    return cos(x)-pow(x,3);
def biseccion(a,b,tol):
    m1=a;
    m=b;
    k=0;
    if(f(a)*f(b)>0):
        print("la funcion no cambia de signo");

    while (abs(m1-m)>tol):
        m1=m;
        m=(a+b)/2;
        if(f(a)*f(m)<0):
            b=m;
        if(f(m)*f(b)<0):
            a=m;
        print("el intervalo es[",a,",",b,"]")
        k=k+1;
    print("x",k,"=",m,"es una buena aproximacion")
biseccion(0,pi,10**(-6))
