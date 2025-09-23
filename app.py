from flask import Flask, render_template, request, jsonify
from utils.ai_generator import generate_introduction
from utils.data_fetcher import get_statistical_data
from utils.conclusion import generate_conclusion

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/generate', methods=['POST'])
def generate_response():
    data = request.json
    prompt = data.get('prompt', '')
    
    if not prompt:
        return jsonify({'error': 'No prompt provided'}), 400
    
    try:
        # Generate the three paragraphs
        paragraph1 = generate_introduction(prompt)
        paragraph2 = get_statistical_data(prompt)
        paragraph3 = generate_conclusion(paragraph1, paragraph2)
        
        return jsonify({
            'paragraph1': paragraph1,
            'paragraph2': paragraph2,
            'paragraph3': paragraph3
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# In app.py
import sys
import os

# Get the absolute path to the project root
project_root = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, project_root)

# Now import using absolute paths
from utils.ai_generator import generate_introduction
if __name__ == '__main__':
    app.run(debug=True)
    