from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
import os

from crew.crew_manager import CrewManager
from utils.formatter import format_test_case_output

# Load environment variables
load_dotenv()

app = Flask(__name__)
crew_manager = CrewManager()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    user_requirement = request.json['requirement']
    result = crew_manager.run(user_requirement)
    formatted_result = format_test_case_output(str(result))
    return jsonify({"result": formatted_result})

if __name__ == '__main__':
    app.run(debug=True)
