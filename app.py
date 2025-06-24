from flask import Flask, request, jsonify
import os
from datetime import datetime

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def handle_softr_webhook():
    try:
        data = request.json
        print(f"Received at {datetime.now()}: {data}")
        
        # Process your data here
        if data.get('type') == 'form_submission':
            name = data.get('data', {}).get('name')
            email = data.get('data', {}).get('email')
            print(f"New form submission: {name} - {email}")
        
        return jsonify({"status": "success", "received": True}), 200
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"status": "error"}), 400

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
