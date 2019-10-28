import logging  
from bottle import Bottle, request, HTTPError
import sentry_sdk
from sentry_sdk.integrations.bottle import BottleIntegration
sentry_sdk.init("https://513b50091e11430c9426a6e29d98f6f9@sentry.io/1797787",  integrations=[BottleIntegration()])


app = Bottle()

@app.route('/success')  
def index():  
   
    return  

@app.route('/fail')  
def fail():  
   
    return HTTPError(500) 
  
  
app.run(host='localhost', port=8080)