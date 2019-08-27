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

@app.route("/PyAdder", methods=['GET', 'POST'])
def PyAdder():
    if request.method == 'POST':
        num1 = request.form.get('num1')
        num2 = request.form.get('num2')
        theanswer = str(int(num1)+int(num2))
        hostname = socket.gethostname()
        nowtime = datetime.now()
        html = '''<form method == "GET">
            {printanswer}<br>
            <input type="submit" value="Reset"><br><br><br>
            The host container who served this up is:</b> {hostname}<br>
            This reply was generated at: </b> {nowtime}<br/>
        </form>'''
        return html.format(printanswer=theanswer, nowtime=nowtime, hostname=hostname)

    return '''<form method="POST">
        Welcome to PyAdder.<br>
        Enter two numbers that you want to add together.<br>
        First_Number: <input type="text" name="num1"><br>
        Second_Number: <input type="text" name="num2"><br>
        <input type="submit" value="Submit"><br><br><br>
        
        This application maintained by chase.horvath@ibm.com<br>
        Git repo: https://github.com/chase-horvath-ibm/PyAdder<br>
   </form> '''

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
