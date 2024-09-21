from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello, World! Let's go!"

if __name__ == '__main__':
    # '0.0.0.0' tells Flask to listen to all network interfaces, not just
    # traffic from the hosting machine. Required for access from a Docker
    # container, or to make this server publicly accessible to the internet.
    app.run(host='0.0.0.0', port=5000)
