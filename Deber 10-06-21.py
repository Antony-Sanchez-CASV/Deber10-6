
def abrirT ():
    h=0
    c=0
    p=0
    archivo=open('Harry.txt',encoding='utf8')
    linea=archivo.readline()
    while linea!="":
        if("child" in linea or "Child" in linea or "Boy" in linea or "kid" in linea):
            c=c+1
        if("Harry" in linea or "harry" in linea):
            h=h+1
        if("Potter" in linea or "potter" in linea):
            p=p+1
        linea=archivo.readline()
    print("(Harry, ",h,")")
    print("(Potter, ", p,")")
    print("(Child, ", c,")")
    archivo.close()

abrirT()

