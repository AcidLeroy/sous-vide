from flask import Flask
from flask import jsonify
from flask import request
from sous_videdb import SousVideDB


app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/stats', methods=['GET']) 
def stats(): 
    past_minutes = request.args.get('minutes') 
    print("past_minutes = ", past_minutes)
    with SousVideDB() as db: 
        stats = db.get_stats(int(past_minutes))

    return jsonify(stats)
	
if __name__ == '__main__': 
    app.run(debug=True)
