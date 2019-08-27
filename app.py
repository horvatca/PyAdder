from flask import Flask, request
from datetime import datetime
#from redis import Redis, RedisError
import os
import socket

# Connect to Redis
#redis = Redis(host="redis", db=0, socket_connect_timeout=2, socket_timeout=2)

app = Flask(__name__)

@app.route("/")
def hello():
#    try:
#        visits = redis.incr("counter")
#    except RedisError:
#        visits = "<i>cannot connect to Redis, counter disabled</i>"

    html = "<h3>Hello {name}!</h3>" \
	   "<b>You have just accessed you containerized Python api.<br>" \
           "<b>The host container who served this up is:</b> {hostname}<br/>" \
           "<b>This reply was generated at: </b> {nowtime}<br/>"
    return html.format(name=os.getenv("whoBuilt"), hostname=socket.gethostname(), \
                nowtime=datetime.now())

@app.route("/xml")
def xml():
    html = "<h3>To do... Wish this was XML!</h3>"
    return html

@app.route("/add")
def add():
    return str(int(request.args.get('num1')) + int(request.args.get('num2')))

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
