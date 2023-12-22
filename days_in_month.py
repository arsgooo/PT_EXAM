from flask import Flask, jsonify

app = Flask(__name__)

def days_in_month(month):
    months = {
        "January": 31,
        "February": 28,
        "March": 31,
        "April": 30,
        "May": 31,
        "June": 30,
        "July": 31,
        "August": 31,
        "September": 30,
        "October": 31,
        "November": 30,
        "December": 31,
    }

    if month in months:
        return months[month]
    else:
        raise ValueError("Invalid month name")

@app.route('/', methods=['GET'])
def get_days_in_month():
    month = "January"
    try:
        result = days_in_month(month)
        return f"{month} has {result} days."
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=3000)
