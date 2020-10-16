import Descrypter
import socket
import GenAp
import os


texto= open("mensajeentrada.txt","r")
textoplano= texto.read()
texto.close()


#Servidor
respuestas = []
host = "LocalHost"
port = 5656
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host,port))
server.listen(1)
print("Server en espera de conexiones")

sb=int(input("Ingersar valor secreto: ")) #valor provado server

activeConection, addr = server.accept()
numeros = GenAp.AP()

p = numeros[0]
alpha = numeros [1]
respuestas.append(numeros)
num = (str(numeros[0])+"-"+str(numeros[1]))
print(num)
activeConection.send(str(num).encode(encoding = "ascii", errors="ignore"))

c =0
while True:

    recibido = activeConection.recv(1024)
    a = recibido.decode(encoding = "ascii", errors="ignore")
    respuestas.append(a)
    enviar= input("Continuar")
    print (respuestas)
    activeConection.send(enviar.encode(encoding = "ascii", errors="ignore"))
    if(c==0):
        x2 = pow(alpha,sb)%p
        respuestas.append(int(x2))
        activeConection.send(str(x2).encode(encoding = "ascii", errors="ignore"))
        c +=1

    elif(c==1):
        x1 = int(respuestas[1])
        xb = pow(x1,sb)%p
        xb = int(xb)
        activeConection.send(str(xb).encode(encoding = "ascii", errors="ignore"))
        respuestas.append(xb)
        c +=1

    else:
        if (int(respuestas[3]) == respuestas[4]):
            
            print ("Las claves coinciden, se procedera a encryptar el texto")



            MseguroDes = Descrypter.desC(textoplano)
            Msegurotri = Descrypter.tridesC(textoplano)

            ms = str(MseguroDes)
            mstri = str(Msegurotri)

            os.remove("mensajeentrada.txt")
            mensajec = open("mensajeentrada.txt", "w")
            mensajec.write(ms)
            mensajec.write("-")
            mensajec.write(mstri)
            mensajec.close()
            break
        else:
            print("Las claves no coinciden adios")
            objsocket.close()        

    
activeConection.close() 

    
    



