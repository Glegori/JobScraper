from flask import Flask, render_template, request, jsonify

import httpx
import re

import json
import openai
from requests_html import HTMLSession

app = Flask(__name__)
f = open("OpenAiKey.txt","r")
apikey = f.read()
f.close

@app.route('/')
def index():
    return render_template('index.html')

def indeedScrape():
    indeedHeader = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    "Connection": "keep-alive",
    "Accept-Language": "en-US,en;q=0.9,lt;q=0.8,et;q=0.7,de;q=0.6",
}   
    search="Networking"
    location = "Burnaby"
    response = httpx.get(f"https://ca.indeed.com/jobs?q={search}&l={location}&sc=0kf%3Aexplvl(ENTRY_LEVEL)" , headers=indeedHeader)
    
    #return display

def linkedinScrape():
    print("incomplete")

@app.route('/scrape', methods=['POST, GET'])
def scrape():
    website = request.form['website']
    match website:
        case "":
            indeedScrape()
        case "":
            linkedinScrape()
#pass from the input/ move this query section up to the other page
""" 
@app.route('/process_chatgpt', methods=['POST'])
async def process_chatgpt():
    query = request.form['query']
    results_1 = request.form.getlist('results_1[]')

    if not results_1:
        return jsonify({'error': 'No results to process.'})

    try:
        openai.api_key = apikey  # Replace with your OpenAI API key
        #change model perhaps?
        apiquery = openai.ChatCompletion.create(
            model="gpt-3.5",
            messages=[
                {"role": "user", "content": f"Given the following data: {results_1}, please filter out jobs requiring greater than 3 years and {query}. return in the same format it was given"}
            ]
        )
        chatgpt_response = apiquery['choices'][0]['message']['content']
        return jsonify({'response': chatgpt_response})
    except Exception as e:
        return jsonify({'error': str(e)})
"""
if __name__ == '__main__':
    app.run(debug=True)