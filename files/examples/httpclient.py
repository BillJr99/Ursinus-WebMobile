import socket

def read_response(conn):
    data = ""
    while True:
        chunk = conn.recv(1024)
        print(chunk)
        if not chunk: 
            break
        data += chunk.decode("utf-8")
        
    return data
	
def connect(host, port, url):
    conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # SOCK_STREAM is a TCP connection over AF_INET, which is IP: TCP/IP
    conn.connect((host, port))
    connstr = "GET " + url + " HTTP/1.1\r\n"
    conn.send(connstr.encode())
    hoststr = "Host: " + host + "\r\n"
    conn.send(hoststr.encode())
    conn.send("\r\n".encode()) # blank line
	
    return read_response(conn)
	
resp = connect("www.ctralie.com", 80, "/")
print(resp)