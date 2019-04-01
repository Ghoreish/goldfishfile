import _thread,socket,os
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
def send(file,s):
    x,b=s.accept()
    x.recv(1024)
    x.send(file.encode())
    res=x.recv(1024)
    while res!=b'OK':
        res=x.recv(1024)
    f=open(file,"rb")
    data=f.read(1000)
    while data:
        x.send(data)
        data = f.read(1000000)
    f.close()
def get(x):
    x.sendall(b'HELLO')
    filename=x.recv(1024)
    while filename==b'':
        filename=x.recv(1024)
    x.sendall(b'OK')
    file=str(filename)[2:-1]
    f=open(file,"wb")
    data=x.recv(10000000)
    while data:
        f.write(data)
        data=x.recv(10000000)
    f.close()
    print(file," DONE!")

while True:
    c=input("1) server\n2) client\n1 or 2?: ")
    if c=='1':
        file=input("please enter filename: ")
        if file not in os.listdir():
            print("File not Found!")
            continue
        try:
            s.bind(("0.0.0.0",int(input("port: "))))
            s.listen(10)
        except:
            print("ERROR!")
            continue
        send(file,s)
        print(file," DONE!")
    elif c=='2':
        try:
            ip=input("ip: ")
            port=int(input("port: "))
        except:
            print('ERROR!')
            continue
        s.connect((ip,port))
        get(s)
