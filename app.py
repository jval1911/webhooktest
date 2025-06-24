@app.route('/webhook', methods=['POST'])
def handle_webhook():
    print("=== WEBHOOK HIT ===", flush=True)
    try:
        data = request.json
        print(f"Full request data: {data}", flush=True)
        
        # Get epidescription from body
        epidescription = data.get('epidescription')
        print(f"EPI Description: {epidescription}", flush=True)
        
        # Get Individual Certificate Number from header ← HERE
        cert_number = request.headers.get('Individual-Certificate-Number')  ← THIS LINE
        print(f"Individual Certificate Number: {cert_number}", flush=True)  ← AND THIS LINE
        
        # Process both pieces of data
        if epidescription and cert_number:
            print(f"Processing certificate {cert_number} with description: {epidescription}", flush=True)
        else:
            print("Missing required data - epidescription or certificate number", flush=True)
        
        return jsonify({"status": "success", "received": True}), 200
    except Exception as e:
        print(f"ERROR: {e}", flush=True)
        return jsonify({"status": "error", "message": str(e)}), 400
