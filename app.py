from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/")
def home():
    return jsonify({
        "status": "online",
        "app": "MarketFlow AI",
        "message": "AI WhatsApp backend is running"
    })


@app.route("/health")
def health():
    return jsonify({
        "status": "healthy"
    })


@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.get_json(silent=True)

    print("Incoming WhatsApp data:")
    print(data)

    return jsonify({
        "success": True,
        "message": "Webhook received"
    })


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000
    )
