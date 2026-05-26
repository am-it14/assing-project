from flask import Flask, render_template, render_template_string, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    html_content = '''<!DOCTYPE html>
<html>
<head>
    <title>Hello Backend Page</title>
</head>
<body>
    <h1>Hello From Backend!</h1>
</body>
<style>
    body {
        background-color: #000000;
        color: #FFFF00;
    }
</style>
</html>
'''
    return render_template_string(html_content)

@app.route('/api/submit', methods=['POST'])
def submit_data():
    data = request.get_json()
    name = data.get('name')
    age = data.get('age')
    mobile = data.get('mobile')
    email = data.get('email')

    line = f"{name}, {age}, {mobile}, {email}\n"
    with open('data.txt', 'a') as far:
        far.write(line)

    return jsonify({
        "status": "success",
        "message": f"Hello {name}! Received your profile: Age {age}, Mobile {mobile}, and Email {email}."
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)