from flask import Flask, request, jsonify
from exprogram import calculate
app = Flask(__name__)

@app.route('/')
def home():
  return "Home Page."

@app.route('/test')
def test_route():
  return "Test Route 3: Even more extra testing"

@app.route('/calculate', methods=['POST'])
def calculate_scholarship_route():
    try:
        data = request.get_json()
        avg_score = data['avg_score']
        max_score = data['max_score']
        base = data['base']
        scholarship = calculate(avg_score, max_score, base)
        result = {
            'scholarship': scholarship
        }
        return jsonify(result), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')