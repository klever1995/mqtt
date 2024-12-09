import paho.mqtt.client as mqtt
from flask import Flask, render_template
from flask_socketio import SocketIO


app = Flask(__name__)
socketio = SocketIO(app)


def on_connect(client, userdata, flags, rc):
    print(f"Conectado al broker con código {rc}")
    client.subscribe("test/topic")  


def on_message(client, userdata, msg):
    print(f"Mensaje recibido en el tema {msg.topic}: {msg.payload.decode()}")
    
    socketio.emit('mqtt_message', {'message': msg.payload.decode()})


mqtt_client = mqtt.Client()


mqtt_client.on_connect = on_connect
mqtt_client.on_message = on_message


mqtt_client.connect("test.mosquitto.org", 1883, 60)


mqtt_client.loop_start()


@app.route('/')
def index():
    return render_template('index.html')  


if __name__ == '__main__':
    print("Iniciando el servidor Flask...")
    socketio.run(app, host='0.0.0.0', port=5000)  
