from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Estimate API Running"

@app.route("/estimate", methods=["POST"])
def estimate():

    data = request.json

    return jsonify({
        "status": "success",
        "received": data
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
