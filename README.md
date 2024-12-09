# MQTT with Flask in Docker

A simple MQTT client using Flask, Paho MQTT, and Dockerized for easy execution in any environment.

## Description

This is a basic MQTT client implemented using Flask and Paho MQTT. The client listens for MQTT messages from a broker and serves them to connected clients via WebSocket. The `/` endpoint serves an HTML page (`index.html`) where users can send and receive messages in real-time.

## Technologies Used

- Python
- Flask (Python web framework)
- Flask-SocketIO
- Paho MQTT (MQTT client library)
- Docker

## Prerequisites

To run this project, you need to have Docker installed on your machine. If you don't have it, you can download it from [here](https://www.docker.com/products/docker-desktop).

Additionally, you need a running MQTT broker (e.g., Mosquitto). You can either set up your own broker or use a public one like `test.mosquitto.org`.

## Instructions to Run the Project

1. **Clone this repository:**

   If you haven't cloned the repository yet, you can do so with the following command:

   ```bash
   git clone git clone git clone 

2. **Build the Docker image:**

   Before running the container, build the Docker image using the following command:

   ```bash
   docker build -t ksrobalino/mqtt:v1 .

3. **Push the image to Docker Hub (if needed):**

   If you'd like to upload the image to Docker Hub for others to use, you can do so with:

   ```bash
   docker push ksrobalino/mqtt:v1

4. **Run the Docker container:**

   After building the image, run the container with the following command:

   ```bash
   docker run -d -p 5000:5000 --name mqtt_client_container ksrobalino/mqtt:v1

5. **Access the WebSocket server:**

   Once the container is running, you can access the server at the following URL
   ```bash
   http://localhost:5000
   
   The server will serve a simple HTML page where you can send and receive MQTT messages.

6. **Test the connection:**

- **When you send a message from the HTML interface**, the server will emit the message to connected clients using WebSocket.
- **When the MQTT client receives a message from the broker**, it will emit the message to the WebSocket clients.

7. **Example of MQTT Communication:**

#### Client (Web Interface):
1. Enter a message and click "Send" on the page served at `http://localhost:5000`.
2. The message will be sent to the MQTT broker, and any subscribed clients will receive it.