import socketio
import eventlet

sio_server = socketio.Server()
# Web Server Gateway Interface
app = socketio.WSGIApp(sio_server)

@sio_server.event
def connect(sid, headers):
    print("Client connected: ", sid) # sid in lista

@sio_server.event
def my_message(sid, data):
    print(f"User {data['name']} send message: {data['msg']}")

eventlet.wsgi.server(eventlet.listen(('localhost', 5001)), app)

# def send_msg():
#     msg = input("Enter message: ")
#     sio_client.emit('my_message', {'msg': msg, 'name': username})
#     sio_client.sleep(1)

# trebuie retinuti clientii pe partea de server

# se creeaza server
# se pune in WSGI (modalitatea de distribuitie)
