from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/submit', methods=['POST'])
def submit_data():
    data = request.get_json()
    name = data.get('name')
    age = data.get('age')
    mobile = data.get('mobile')
    email = data.get('email')

    print(f"Received DATA -> Name: {name}, Age: {age}, Mobile: {mobile}, Email: {email}")

    return jsonify({
        "status": "success",
        "message": f"Hello {name}! Received your profile: Age {age}, Mobile {mobile}, and Email {email}."
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)