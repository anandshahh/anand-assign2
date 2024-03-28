from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Welcome to Wild Rydes! Developer: Anand Shah ID: 1008886031'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
