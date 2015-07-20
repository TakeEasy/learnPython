__author__ = 'Easy_Zhou'

# import socket lib
import socket
# creat a socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# connect
s.connect(('www.sina.com.cn', 80))
# send message
s.send('GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')
# recv
buffer = []
while True:
    d = s.recv(1024)
    if d:
        buffer.append(d)
    else:
        break
data = ''.join(buffer)
s.close()
header, html = data.split('\r\n\r\n', 1)
print header
with open('''C:\Users\ZhouY129\Desktop\sina.html''', 'wb') as f:
    f.write(html)


