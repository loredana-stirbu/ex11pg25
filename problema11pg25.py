n=int(input('Dati numarul de elemente din vector:'))
a=[]
print('Introduceti ',n,' elemente pentru vectorul creat')
if n<10:
    for i in range(0,n):
        x=int(input('Dati elementul='))
        a.extend([x])
    print(a)
else:
    print("Ati introdus o valoare incorecta.")

#a)  
print('a)  afişează pe ecran componentele tabloului la un interval de 5 poziţii:')
r=a[::5]
print(r)

#b)  
print('b)  afişează pe ecran numerele în ordinea inversă a introducerii în calculator:')
b=a[::-1]
print(b)

#c)  
print('c)  sortează componentele tabloului în ordine descrescătoare:')
c=sorted(a)
c.sort(reverse=True)
print(c)

#d)  
print('d)  afişează pe ecran doar componentele pare:')
d=[]
for i in range(0,len(a)):
    if a[i]%2==0:
        y=a[i]
        d.extend([y])
print(d)

#e)  
print('e)  afişează pe ecran media aritmetică a componentelor pare:')
e=sum(d)/len(d)
print(e)

#f) 
print('f)  afişează pe ecran doar componentele impare:')
f=[]
for i in range(0,len(a)):
    if a[i]%2!=0:
        y=a[i]
        f.extend([y])
print(f)

#g) 
print('g)  afişează pe ecran doar componentele care sunt mai mari ca x şi nu sunt divizibile cu y (valorile x şi y se citesc de la tastatură):')
x=int(input("Dati un numar:"))
y=int(input("Dati un numar:"))
g=[]
for i in range(0,len(a)):
    if (a[i]>x and a[i]%y!=0):
        z=a[i]
        g.extend([z])
if len(g)==0:
    print("lista nu are elemente")
else:
    print(g)

#h)
print('h)  afişează pe ecran doar componentele care sunt mai mari ca x şi mai mici decât y (valorile x şi y se citesc de la tastatură):')
x=int(input("Dati un numar:"))
y=int(input("Dati un numar:"))
h=[]
for i in range(0,len(a)):
    if (a[i]>x and a[i]<y):
        w=a[i]
        h.extend([w])
if len(h)==0:
    print("lista nu are elemente")
else:
    print(h)

#i)
print('i)  afişează pe ecran poziţiile (indicii) componentelor impare negative:')
ii=[]
for i in range(0,len(a)):
    if (a[i]%2!=0 and a[i]<0):
        ii.append(i)
print(ii)

#j)
print('j)  afişează pe ecran poziţiile (indicii) componentelor ce conţin doar două cifre semnificative:')
j=[]
for i in range(0,len(a)):
    if (a[i]>9 and a[i]<100)or(a[i]<-9 and a[i]>-100):
        j.append(i)
print(j)

#k)
print('k)  înlocuieşte prima componentă a tabloului cu componenta de valoare minimă din tabloul respectiv:')
k=a.copy()
k[0]=min(k)
print(k)

#l)
print('l)  înlocuieşte componenta de valoare minimă din tabloul respectiv cu prima componentă a acestuia:')
l=a.copy()
s=min(l)
l[l.index(s)]=l[0]
print(l)

#m)
print('m)  creează un tablou nou, format doar din componentele pare ale tabloului introdus de la tastatură:')
par=[]
for i in range(0,len(a)):
    if a[i]%2==0:
        y=a[i]
        par.extend([y])
m=par
print(m)

#n)
print('n)  creează un tablou nou, format doar din componentele divizibile cu 3 ale tabloului introdus de la tastatură:')
div=[]
for i in range(0,len(a)):
    if a[i]%3==0:
        y=a[i]
        div.extend([y])
n=div
print(n)

#o)
print('o)  creează un tablou nou, format doar din acele componente ale tabloului in-trodus de la tastatură care au cel mult patru divizori:')
o=[]
for i in a:
    if i>0:
        nr=0
        for x in range(1,i+1):
            if i%x==0:
                nr+=1
        if nr<=4:
            o.append(i)
if i<0:
    print("Numerele ce nu sunt naturale nu au divizori")
print(o)
