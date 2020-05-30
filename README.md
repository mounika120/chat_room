# chat-server-client
Bothe the server and client files should be in the same folder to execute chat_room. 

Run the server file using "python chatserver.py hostname port" in the command prompt.
For the hostname use the command "ipconfig"which shows the ip4 address of your device .
You can give the default port number as 8888.

Simultaneously run the client file using "python chatclient.py hostname port NICKNAME"
The hostname and the port number should be same in both server and client.

After running it successfully server sends Hello message to all the clients connected.
The client should display messages from the server, without user input. 
The client will be able to send msg at any point in time.
No limit in the number of clients that can use it simultaneously. 
As with the client, the server will work without any user input. 

Nick name of the clients should be given in the form "NICK nickname" and the message in "MSG message" also the client can broadcast its messages in "MSG nickname message".
You can exit from chat-server-client using "MSG quit" in client .

