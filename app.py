from flask import Flask

# Create an instance of the Flask class
app = Flask(__name__)

# Use the route() decorator to tell Flask what URL should trigger the function
@app.route("/")
def hello_world():
    return "<p>Hello, World!Webhook!!!</p>"

# Run the application on a specific port (e.g., 8000)
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8081, debug=False)
