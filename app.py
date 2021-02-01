from flask import Flask,request
import pandas as pd
app = Flask(__name__)

@app.route('/hello/')
def hello():
    return "Hello World!"
print("40")

@app.route('/computemean/',methods=["POST"])
def bye():
    data = request.json
    data = pd.read_json(data,orient="index")
    return data.mean().to_json()

if __name__ == '__main__':
    print("72")
    app.run(debug = True)

