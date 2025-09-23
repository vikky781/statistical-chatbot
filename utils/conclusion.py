import openai
import os

# Set your OpenAI API key
openai.api_key = os.environ.get('OPENAI_API_KEY')

def generate_conclusion(introduction, statistics):
    """
    Generate a conclusion paragraph based on the introduction and statistics.
    """
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant that provides concise conclusions based on given information."},
                {"role": "user", "content": f"Based on the following introduction and statistics, provide a brief conclusion:\n\nIntroduction: {introduction}\n\nStatistics: {statistics}"}
            ],
            max_tokens=100,
            temperature=0.7
        )
        
        return response.choices[0].message['content'].strip()
    except Exception as e:
        print(f"Error generating conclusion: {e}")
        return "In conclusion, the information provided offers valuable insights into the topic. Further research may reveal additional details and perspectives."