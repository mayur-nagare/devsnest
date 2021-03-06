from flask import Flask, redirect, url_for, request

app = Flask(__name__)

app.config["DEBUG"] = True

serverData = []
@app.route('/', methods=['GET'])
def home():
    return '''<h1>Devsnest FLASK API</h1>
    <ul>
    <li>Add a string here: /add/string<br></li>
    <li>Concat all the submitted strings: <url>/get</li>
    <li>To get the all strings that we have click on below link:</li>
        <li><a href="http://127.0.0.1:5000/get">Click Here</a></li>
    <ul>
    '''
    # return '''<h1>Devsnest FLASK API</h1>
    #         To add string click on below link:
    #         <a href="http://127.0.0.1:5000/add">Click Here</a>

    #         To get the all strings that we have click on below link:
    #         <a href="http://127.0.0.1:5000/get">Click Here</a>
    #         '''

@app.route('/add', methods=['POST'])
@app.route('/add/<string:ip_str>', methods=['GET', 'POST'])
def addString(ip_str=None):
    if request.method == "GET":
        serverData.append(ip_str)
        return 'The string {} has been saved in the server!'.format(serverData[-1])    
    elif request.method == "POST":
        req_data = request.get_json(force=True)
        serverData.append(req_data['string'])
        return 'The string {} has been saved in the server!'.format(serverData[-1]) 

@app.route('/get/', methods=['GET'])
def getString():
    return ' '.join(serverData)

app.run()