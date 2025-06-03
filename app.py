from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "🚀 Hello from Flask App deployed via DevOps Hello World! This is the sample dev"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
