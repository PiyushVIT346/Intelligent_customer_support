from flask import Flask, request, jsonify, render_template
import pickle
from chatbot.nlp import process_user_message

# Load the chatbot model
with open('model/chatbot_model.pkl', 'rb') as file:
    chatbot_model = pickle.load(file)

# Create the Flask app
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.form.get('message', '')
    response = process_user_message(user_message, chatbot_model)
    return jsonify({'response': response})

@app.route('/admin')
def admin():
    return render_template('admin.html')

if __name__ == '__main__':
    app.run(debug=True)
