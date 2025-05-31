from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['POST'])
def webhook():
    req = request.get_json()
    print("Request received:", req)

    tag = req.get('fulfillmentInfo', {}).get('tag')

    # Customize response based on tag
    if tag == "custom-welcome":
        response_text = "Hello from Cloud Run webhook!"
    else:
        response_text = f"Webhook received tag: {tag}"

    return jsonify({
        "fulfillment_response": {
            "messages": [
                {
                    "text": {
                        "text": [response_text]
                    }
                }
            ]
        }
    })

if __name__ == '__main__':
    app.run(debug=True)
