from Homework7.Client import request

data = 'GET /messages/4 HTTP/1.0\r\n\r\n'
print(request(data, '127.0.0.1', 8080))