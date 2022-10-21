from flask import Flask, render_template
import os
import requests, json
app = Flask(__name__)


@app.route('/')
def login():
   api_host = os.environ.get('API_HOST')
   api_port = os.environ.get('API_PORT')
   api_endpoint = os.environ.get('API_ENDPOINT')
   # if(request.method == 'GET'):
   uri = f'http://{api_host}:{api_port}/{api_endpoint}'
   try:
      Jresponse = requests.get(uri)
   except requests.ConnectionError:
      return "Connection Error"  
   meal = Jresponse.json()

   return render_template('login.html', food=meal['meal'], price=meal['price'])
  
#putting the DB in volume 

if __name__ == '__main__':
   port = os.environ.get('CONSUMER_PORT')
   app.run(host="0.0.0.0",port=port)