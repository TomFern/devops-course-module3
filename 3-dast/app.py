from flask import Flask, request, jsonify

app = Flask(__name__)

# Vulnerable endpoint: does not sanitize user input
@app.route('/search')
def search():
    query = request.args.get('q', '')
    # In a real-world scenario, this query would be passed to a database without proper sanitization
    return f"Search results for: {query}"

if __name__ == '__main__':
    app.run(debug=True)
