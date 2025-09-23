import openai
import sys
import os

# Set your OpenAI API key
openai.api_key = os.environ.get('OPENAI_API_KEY')

def generate_introduction(prompt):
    """
    Generate an introduction paragraph using OpenAI's GPT model.
    """
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant that provides clear, informative introductions to various topics."},
                {"role": "user", "content": f"Provide a brief introduction about: {prompt}"}
            ],
            max_tokens=150,
            temperature=0.7
        )
        
        return response.choices[0].message['content'].strip()
    except Exception as e:
        print(f"Error generating introduction: {e}")
        return "I couldn't generate an introduction at this time. Please try again later."