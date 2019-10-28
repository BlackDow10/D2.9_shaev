import os
import logging  
from bottle import Bottle, request, HTTPError, run
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
  
  
if os.environ.get("APP_LOCATION") == "heroku":
    app.run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 5000)),
        server="gunicorn",
        workers=3,
    )
else:
    app.run(host="localhost", port=8080, debug=True)