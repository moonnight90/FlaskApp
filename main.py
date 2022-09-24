from flask import Flask,jsonify
from flask import request
import random
app = Flask(__name__)
usernames = open("usernames.txt", encoding="cp437", errors='ignore').read().splitlines()
@app.route('/username')
def username():    
    _ = random.choice(usernames).strip() + f"{random.randint(100,999)}"
    return jsonify({'username':_,'ip':request.remote_addr})

if __name__ == "__main__":
    app.run(debug=False,host="0.0.0.0")