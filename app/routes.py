from app import app
from flask import render_template, request, redirect
import os
import requests

@app.route('/')
def index():
    client_id = os.environ.get('CLIENT_ID')
    return render_template("index.jinja", client_id=client_id)

@app.route('/home')
def home():
    client_id = os.environ.get('CLIENT_ID')
    client_secret = os.environ.get('CLIENT_SECRET')
    redirect_url = "https://github.com/login/oauth/access_token?client_id=" + client_id \
        + "&client_secret=" + client_secret \
        + "&code=" + request.args.get('code')
    response1 = requests.get(redirect_url)

    print(response1.text)
    query_params = response1.text.split('&')
    access_token = ''
    for param in query_params:
        print(param)
        split = param.split('=')
        if len(split) == 2 and split[0] == 'access_token':
            access_token = split[1]
    
    print("found access token: ", access_token)
    
    request_header = {'Authorization': "token " + access_token}
    resp = requests.get('https://api.github.com/user', headers = request_header)
    
    print("final response: ", resp.text)

    return "finita"

@app.route('/callback')
def callback():
    access_token = request.args.get('access_token')
    print('access_token: ', access_token)
    request_header = {'Authorization': "token " + access_token}
    response = requests.get('https://api.github.com/user', headers = request_header)
    print('response.text: ', response.text)
    return render_template("callback.jinja")