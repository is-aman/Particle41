from flask import Flask, request, jsonify
from datetime import datetime
import os

app = Flask(__name__)

@app.route('/')
def get_time():
    return jsonify({
        "timestamp": datetime.utcnow().isoformat(),
        "ip": request.remote_addr
    })

if __name__ == '__main__':
    port = int(os.getenv("PORT", 3000))
    app.run(host='0.0.0.0', port=port)
