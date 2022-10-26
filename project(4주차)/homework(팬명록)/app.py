from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('mongodb+srv://test:sparta@cluster0.rp2thdg.mongodb.net/Cluster0?retryWrites=true&w=majority')
db = client.dbsparta


@app.route('/')
def home():
    return render_template('index.html')

@app.route("/homework", methods=["POST"])
def homework_post():
    name_receive = request.form['name_give']
    cheer_receive = request.form['cheer_give']

    doc = {
        'name': name_receive,
        'cheer': cheer_receive
    }

    db.fans_cheer.insert_one(doc)
    return jsonify({'msg':'댓글 저장 완료.'})

@app.route("/homework", methods=["GET"])
def homework_get():
    fans_cheer_list = list(db.fans_cheer.find({},{'_id':False}))
    return jsonify({'fans_cheers':fans_cheer_list})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)