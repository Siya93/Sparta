from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

from pymongo import MongoClient           
client = MongoClient('localhost', 27017)  
db = client.dbsparta                      

## HTML을 주는 부분
@app.route('/')
def home():
    return render_template('00_Order_Page_v3.html')

## API 역할을 하는 부분
@app.route('/order_info', methods=['POST'])
def write_info():
    name_receive = request.form['name_give']
    address_receive = request.form['address_give']
    num1_receive = request.form['num1_give']
    size_receive = request.form['size_give']
    amount_receive = request.form['amount_give']

    information = {
        'name' : name_receive,
        'address' : address_receive,
        'num1' : num1_receive,
        'size' : size_receive,
        'amount' : amount_receive
    }

    db.informations.insert_one(information)
    return jsonify({'result':'success', 'msg': '이 요청은 POST!'})

@app.route('/order_info', methods=['GET'])
def read_info():
    informations = list(db.informations.find({}, {'_id': False}))
    return jsonify({'result': 'success', 'informations': informations})
    #return jsonify({'result':'success', 'msg': '이 요청은 GET!'})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)