
import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(("localhost", 4000))

# 开始监听
server.listen()

server.setblocking(True)


while True:
    # 在服务器端生成连接实例
    conn, addr = server.accept()
    while True:
        data = conn.recv(1024)
        print("receive data :", data)
        conn.send(data.upper())





