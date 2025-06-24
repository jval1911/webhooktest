from flask import Flask, request, jsonify
import os
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({
        "status": "running", 
        "message": "Webhook server is live",
        "endpoints": ["/webhook"]
    })

@app.route('/webhook', methods=['POST'])
def handle_webhook():
    print("=== WEBHOOK HIT ===", flush=True)
    try:
        data = request.json
        print(f"Full request data: {data}", flush=True)
        
        # Get epidescription directly (not nested in 'data')
        epidescription = data.get('epidescription')
        print(f"EPI Description: {epidescription}", flush=True)
        
        return jsonify({"status": "success", "received": True}), 200
    except Exception as e:
        print(f"ERROR: {e}", flush=True)
        return jsonify({"status": "error", "message": str(e)}), 400

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
