from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello World'

@app.route('/login', methods=['GET'])
def login():
    if not request.args.get('name') or not request.args.get('email'):
        return jsonify({
            'massage': 'Missing name or email',
            'status': 'error'
        })
    
    name = request.args.get('name','')
    email= request.args.get('email','')
    return jsonify({
        'massage': 'Login Succefully',
        'status': 'success',
        'data__info':{
            'name': name,
            'email': email
        }
    })
    
if __name__ == '__main__':
    app.run(debug=True,port=5000)
