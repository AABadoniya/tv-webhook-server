from flask import Flask, request
import datetime
import os

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    try:
        data = request.get_json()
        timestamp = datetime.datetime.now().strftime('%d-%m-%Y %H:%M:%S')
        print(f"\n🚨 ALERT RECEIVED at {timestamp} 🚨")
        print(data)

        # Optional system action (Linux users only)
        # os.system("notify-send 'TradingView Alert' 'Signal Received!'")

        return "✅ Alert Received", 200
    except Exception as e:
        print("❌ Error:", e)
        return "❌ Error", 500

@app.route('/', methods=['GET'])
def index():
    return "TradingView Webhook Listener is running!"

if __name__ == '__main__':
    app.run(port=5000)
