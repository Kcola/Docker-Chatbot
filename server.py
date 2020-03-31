#main.py
from flask import Flask
from flask import request, render_template, jsonify
from convobot import ConvoBot
from flask_cors import CORS
import json
app = Flask(__name__)
cb = ConvoBot()
CORS(app, support_credentials=True)
@app.route('/')
def hello_world():
    #cb.send('hi')
    #return cb.reply()
    pass
@app.route('/send', methods=['GET', 'POST'])
def send():
    if request.method == 'POST':
        user_in = json.loads(request.data)
        
        cb.send(user_in['chat'])
            
        bot_rep = cb.reply()
        bot_rep = {
        "bot_response":bot_rep
        }
        return bot_rep
        
        #return render_template('reply.html', user_in=user_in, bot_rep=bot_rep)
    
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)