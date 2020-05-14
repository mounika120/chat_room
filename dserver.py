import select
import socket
import sys
import time
import re
class socket_server:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        try:
            self.server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            self.server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            print('socket has been created')
        except socket.error:
            print('Socket is not created')
            sys.exit()
        self.server.bind((self.host,self.port))
        self.server.listen(100)
        self.server.setblocking(1)
    def server_run(self):
        c_list = [self.server]
        a=[]
        n_list =[]
        new_=[]
        dict = {}
        while True:
            r_list,wr_list,err_list = select.select(c_list,[],[])
            if self.server in r_list:
                conn ,addr = self.server.accept()
                print('New_connection {} established',format(addr))
                n_name = conn.recv(1024)
                sys.stdout.flush()
                comm = 'Hello'
                comm = bytes(comm,'utf-8')
                conn.send(comm)
                conn.setblocking(0)
                n_list.append(n_name)
                c_list.append(conn)
                dict [conn] = 1
            for c in r_list:
                if c != self.server:
                    try:
                        connection_start = c.recv(1024)
                        sys.stdout.flush()
                        if dict[c] == 1:
                            connection_start = connection_start.decode('utf-8')
                            connection_start1 = connection_start[5:]
                            if connection_start[0:4] !='NICK':
                                comm1 = '*Error* type NICK and then give nickname '
                                comm1 = bytes(comm1,'utf-8')
                                c.send(comm1)
                            else:
                                if len(connection_start1)<=12 and len(connection_start1)>=0:
                                    list = ['!','@','#','$','%','^','&','*','(',')','{','}','[',']',':','/','>','<','~','.','|']
                                    count = 0
                                    for i in range(len(list)):
                                        if list[i] in connection_start1:
                                            count = count +1
                                    if count==0:
                                        comm2 = 'ok'
                                        comm2= bytes(comm2,'utf-8')
                                        c.send(comm2)
                                        dict[c] = 0
                                    else:
                                        comm3 = ('*nickname check*: only A-Z and a-z and 0-9 should be present in the nickname ')
                                        comm3 = bytes(comm3,'utf-8')
                                        c.send(comm3)
                                else:
                                    comm4 = 'length of the nickname should be below 12 characters'
                                    comm4= bytes(comm4,'utf-8')
                                    c.send(comm4)
                        else:
                            comm5 = connection_start.decode('utf-8')
                            comm6 = comm5.strip('MSG')
                            if comm5[0:3] != 'MSG':
                                comm7 = 'Format : MSG + text'
                                comm7 = bytes(comm7,'utf-8')
                                c.send(comm7)
                            else:
                                if len(comm5) <= 255:
                                    count =0
                                    for i in comm5[:-1]:
                                        if ord(i)<31:
                                            count = count +1
                                        else:
                                            pass
                                    if count != 0:
                                        comm8 = '*error* check the msg'
                                        comm8 = bytes(comm8,'utf-8')
                                        c.send(comm8)
                                    else:
                                        if comm6=='quit':
                                            comm11 = ('client' +' ' + connection_start1+ 'is Disconnected')
                                            comm11 = bytes(comm1,'utf-8')
                                        #client.send(data4)
                                        for i in c_list:
                                            if i!=self.server and i!=c:
                                                i.send(comm11)
                                            elif i == c:
                                                c_list.remove(i)
                                        else:
                                            for i in c_list:
                                                if i!=self.server and i!=c:
                                                    comm9 = ('MSG' +connection_start1+ " "+comm6)
                                                    comm9 = bytes(comm9,'utf-8')
                                                    i.send(comm9)
                                elif len(comm5) >256:
                                    comm10 = 'ERROR'
                                    comm10 = bytes(comm10,'utf-8')
                                    c.send(comm10)
                    except IOError:
                        continue
                    
        self.server.close()                
def main():
    ser = socket_server(sys.argv[1],int(sys.argv[2]))
    ser.server_run()
if __name__ == "__main__":
    main()



