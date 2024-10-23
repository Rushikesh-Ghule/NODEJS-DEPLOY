from flask import Flask, jsonify
 
app = Flask(__name__)
 
# Sample data
data = {
    "message": "Hello, World!",
    "status": "success"
    
}
 
@app.route('/api/v1/hello', methods=['GET'])
def get_hello():
    return jsonify(data)
 
if __name__ == '__main__':
    port = 5000
    print(f"Running on port {port}")
    app.run(debug=True, host='0.0.0.0', port=port)