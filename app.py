from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('mongodb+srv://tests:sparta@cluster0.jpvee.mongodb.net/Cluster0?retryWrites=true&w=majority')
db = client.dbsparta

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/add', methods=["GET"])
def add_page():
    return render_template('add.html')

@app.route('/update', methods=["GET"])
def add_page():
    return render_template('update.html')


@app.route("/add", methods=["POST"])
def addPost():
    title_receive = request.form.get("title", type=str)
    author_receive = request.form.get("author", type=str)
    url_receive = request.form.get("url", type=str)
    food_receive = request.form.get("food", type=str)
    content_receive = request.form.get("content", type=str)
    print(title_receive,author_receive,url_receive,food_receive,content_receive)
    doc={
        'title':title_receive,
        'author':author_receive,
        'url': url_receive,
        'food':food_receive,
        'content':content_receive
    }
    db.testDB.insert_one(doc)

    return jsonify({'msg': '주문완료'})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)