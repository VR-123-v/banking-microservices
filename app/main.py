from flask import Flask, jsonify

app = Flask(__name__)


@app.get("/health")
def health():
    return jsonify({
        "status": "healthy",
        "service": "account-service"
    }), 200


@app.get("/accounts")
def accounts():
    return jsonify({
        "accounts": [
            {
                "id": "ACC001",
                "type": "checking"
            },
            {
                "id": "ACC002",
                "type": "savings"
            }
        ]
    }), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)