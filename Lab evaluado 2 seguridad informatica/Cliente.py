import socket
import Descrypter
import binascii
#Javiera Ruiz
#Manuel Fuentes

#Cliente
host = "LocalHost"
port = 5656
objsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
objsocket.connect((host, port))
print ("Iniciando cliente")
respuestas = []
sa=int(input("Ingersar valor secreto: "))#valor provado cliente
c=0
while True:
        

        recibido = objsocket.recv(1024)
        a = (recibido.decode(encoding ="ascii",errors ="ignore"))
        respuestas.append(a)
        enviar= input("Continuar")
        objsocket.send(enviar.encode(encoding ="ascii", errors = "ignore"))
        
        print (respuestas) #separacion alpha p
        ap = respuestas[0]
        ap = ap.split("-")
        p = ap[0]
        alpha = ap[1]
        alpha = int(alpha)
        p = int(p)

        if(c==0):
            x1= pow(alpha,sa)%p
            respuestas.append(x1)
            objsocket.send(str(x1).encode(encoding ="ascii", errors = "ignore"))
            c += 1

        elif(c==1):      
            x1 = int(respuestas[2])
            xa = pow(x1,sa)%p
            objsocket.send(str(xa).encode(encoding = "ascii", errors="ignore"))
            respuestas.append(xa)
            c +=1

        else:
            if (respuestas[3] == int(respuestas[4])):
                print ("Las claves coinciden, se procedera a desencriptar el texto")
                break
            else:
                print("Las claves no coinciden adios")
                objsocket.close()

objsocket.close()
            
mensajec = open("mensajeentrada.txt", "r")      
textoplano= mensajec.read()
mensajec.close()

mensaje =textoplano.split("-")

des = (mensaje[0])


Mdes =Descrypter.desD(binascii.unhexlify(des))
print(Mdes)

Msalida = open("mensajerecibido.txt", "w")
Msalida.write(Mdes)
Msalida.close()


