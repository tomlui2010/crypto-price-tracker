from flask import Flask, request, render_template   
import os, requests, json, base64

from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)

@app.route('/', methods = ['GET'])
def getindex():
    return render_template('index.html')

@app.route('/', methods = ['POST'])
def getcurrentrate():
    # get the crypto currency symbol
    crypto_symbol = request.form.get("symbol")
    apikey = os.environ.get("API_KEY")
    secret = os.environ.get("SECRET_VALUE")
    auth_string = f"{apikey}:{secret}"
    auth_string = auth_string.encode("ascii")
    auth_string = base64.b64encode(auth_string)
    headers = {
       'Accept': 'application/json',
       'Authorization' : f"Basic {auth_string.decode('ascii')}"
        }
    crypto_price = requests.request('GET', 'https://api.binance.com/api/v3/ticker/price?symbol={}'.format(crypto_symbol),headers=headers, auth=None)
        
    return render_template('pricetracker.html',price=crypto_price.json())

if __name__ == "__main__":
    # app.run(host="0.0.0.0", port=8000, debug=True)
    app.run(debug=True)