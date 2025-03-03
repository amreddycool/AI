from flask import Flask
from flask_cors import CORS
from flask import request

app = Flask(__name__)
CORS(app)

exchageRates = {
    "GBPUSD": 1.1111,
    "GBPEUR": 1.2222,
    "GBPAUD": 1.3333
}



@app.route("/exchangeRate", methods=["GET", "POST"])
def exchangeRate():
    print("Getting exchange rate")
    rate = exchageRates.get( request.json["fromCurrency"]+request.json["toCurrency"])
    print("Got Rate: ", rate)
    return rate    

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)