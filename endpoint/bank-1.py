__author__ = 'Ajay'

from flask import Flask, jsonify, request
app = Flask(__name__)

login = {
        "username": "automation",
        "password": "strong123"
    }

@app.route('/bank/login', methods=['POST'])
def login_pass():
    return_code = '200'
    return_message = 'Invalid Login Credentials'
    if str(request.get_json()) == str(login):
        return_code = '200'
        return_message = 'Login Successful'
    print(request.headers)
    return return_message, return_code


@app.route('/bank/credit', methods=['GET'])
def waterfound():
    return_message = 'Balance, found!'
    return_code = 200
    return return_message, return_code



@app.route('/bank/payment', methods=['PUT'])
def putfound():
    return_message = 'Payment received!'
    return_code = 200
    if 'payment' in str(request.get_json()):
        return return_message, return_code
    else:
        return_message = 'payment not received!'
        return_code = 404
        return return_message, return_code


@app.route('/bank/credit', methods=['PUT'])
def diggold():
    return_message = 'credit found.'
    return_code = 200
    if 'payment' in str(request.get_json()):
        return return_message, return_code
    else:
        return "Incoorect type", 404


@app.route('/bank/changepwd', methods=['PUT'])
def changepwd():
    return_message = 'Password changed'
    return_code = 200
    if 'payment' in str(request.get_json()):
        return return_message, return_code
    else:
        return "Password change failed", "404"


@app.route('/bank/delete', methods=['DELETE'])
def deletebot():
    return_message = 'successfully deleted'
    return_code = 200
    if 'delete' in str(request.get_json()):
        return return_message, return_code
    else:
        return "delete failed", "404"


@app.route('/bank/passbook', methods=['GET'])
def viewpassbook():
    return_message = 'Passbook!'
    return_code = 200
    return return_message, return_code


@app.route('/bank/changeuser', methods=['PUT'])
def changeuser():
    return_message = 'User changed'
    return_code = 200
    if 'payment' in str(request.get_json()):
        return return_message, return_code
    else:
        return "Password change failed", "404"


@app.route('/bank/linkaccount', methods=['PUT'])
def linkaccount():
    return_message = 'Account linked'
    return_code = 200
    if 'payment' in str(request.get_json()):
        return return_message, return_code
    else:
        return "Password change failed", "404"



@app.route('/bank/paycreditbill', methods=['POST'])
def paycreditbill():
    return_message = 'Account linked'
    return_code = 200
    if 'payment' in str(request.get_json()):
        return return_message, return_code
    else:
        return "Password change failed", "404"



@app.route('/bank/payee', methods=['DELETE'])
def removepayee():
    return_message = 'successfully deleted'
    return_code = 200
    if 'delete' in str(request.get_json()):
        return return_message, return_code
    else:
        return "delete failed", "404"


@app.route('/bank/logout', methods=['POST'])
def logout():
    return_message = 'Logged out'
    return_code = 200
    if 'payment' in str(request.get_json()):
        return return_message, return_code
    else:
        return "Password change failed", "404"
