
import requests
import json
import re
import time

class Groq:
    """This is a class that lets us use Groq AI with ease"""
    """
    Inputs :-
    groq.chat("press enter")
    groq.chat("How to make a water boat")
    
    Outputs:-
    ```{'gui':[['enter']]}```
    ```{'audio':'To make a water boat, you can use materials like plas....'}```
    """
    def __init__(self, api_key):
        self.api_url = "https://api.groq.com/openai/v1/chat/completions"
        self.session = requests.Session()
        self.api_key = api_key
        self.session.headers.update({
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        })
        
    def remove(self, input_string):
        # Define the pattern to match $@$ and the text between them
        try:
            result = re.sub(r'\$\@.*?\$\@\$', '', input_string)
            result = re.findall(r'```(.*?)```', result, re.DOTALL)[0]
            return result
        except:
            return input_string
    
    def chat(self, message):
        if ('time' in message or 'date' in message):
            message += ' '+str(time.localtime())
        
        # Structure the request for Groq's API
        request_body = {
            "model": "llama3-70b-8192",  # Llama 3.2 70B model
            "messages": [
                {"role": "system", "content": "You are an automation assistant that generates precise control commands based on natural language requests. Follow these output formats exactly:\n\n1. For GUI automation commands, return: ```[{'gui':[['key1','key2'], ['action','target']]}]```\n2. For information queries, return: ```[{'audio':'Your detailed answer here'}]```\n3. For visual recognition tasks, return: ```[{'ocr':'text to find on screen'}]```\n\nAlways wrap your response in triple backticks with the appropriate JSON structure. Do not include explanations outside the code block."},
                {"role": "user", "content": "open explorer"},
                {"role": "assistant", "content": "```[{'gui':[['win','e']]}]```"},
                {"role": "user", "content": "open notepad and paste text"},
                {"role": "assistant", "content": "```[{'gui':[['win','r'],['write','notepad'],['enter'],['ctrl','v']]}]```"},
                {"role": "user", "content": "what is raspberry pi"},
                {"role": "assistant", "content": "```[{'audio':'Raspberry Pi is a single board computer'}]```"},
                {"role": "user", "content": "Click on blank document"},
                {"role": "assistant", "content": "```[{'ocr':'blank document'}]```"},
                {"role": "user", "content": """
                 ** *open explorer* ```[{'gui':[['win','e']]}]``` **
                 ** *open whatsapp* ```[{'gui':[['win'],['write','whatsapp'],['enter']]}]``` **
                 ** *open spotify* ```[{'gui':[['win'],['write','spotify'],['enter']]}]``` **
                 ** *type this is a big content* ```[{'gui':[['write','this is a big content']]}]```**
                 ** *search python basics on youtube* ```[{'gui':[['win','r'],['write','chrome'],['enter'],['write','https://www.youtube.com/results?search_query=python+basics'],['enter']]}]```**
                 ** *play pal on spotify* ```[{'gui':[['win'],['write','spotify'],['enter'],['ctrl','k'],['write','pal'],['enter']]}]```**
                 ** *turn off wifi* ```[{'gui':[['win'],['write','WIFI settings'],['enter']]},{'ocr':'off'}]```**
                 """},
                {"role": "user", "content": "How to code in python"},
                {"role": "assistant", "content": "```[{'audio':'Open VS code or any editor start typing print(\\'hello world!\\') then save the file and run python file_name.py in terminal'}]```"},
                {"role": "user", "content": message}
            ],
            "temperature": 0.2,
            "max_tokens": 1024,
            "top_p": 0.9
        }

        # Make POST request to Groq API
        try:
            resp = self.session.post(self.api_url, json=request_body)
            resp_json = resp.json()
            
            if 'choices' in resp_json and len(resp_json['choices']) > 0:
                content = resp_json['choices'][0]['message']['content']
                try:
                    # Extract the content from code blocks and evaluate it
                    extracted = self.remove(content)
                    return eval(extracted)
                except Exception as e:
                    # If evaluation fails, return the raw content
                    return content
            else:
                return resp.text
        except Exception as e:
            return f"Error: {str(e)}"

groq = Groq("Your API Key")