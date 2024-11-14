import requests
import json
import re
import time
class BlackBox:
    """This is a class that lets us use Blackbox AI with ease"""
    """
    Inputs :-
    blackbox.chat("press enter")
    blackbox.chat("How to make a water boat")
    
    Outputs:-
    ```{'gui':[['enter']]}```
    ```{'audio':'To make a water boat, you can use materials like plas....'}```
    """
    def __init__(self, secId):
        self.base_url = "https://www.blackbox.ai"
        self.api = "https://www.blackbox.ai/api"
        self.chat_endpoint = f"{self.api}/chat"
        self.check_endpoint = f"{self.api}/check"
        self.session = requests.Session()
        self.secId = secId
        self.session.headers.update({
            "Accept": "*/*",
            "Accept-Encoding": "gzip, deflate, br, zstd",
            "Accept-Language": "en-US,en;q=0.9",
            "Content-Type": "application/json",
            "Cookie": (f"sessionId={secId}; __Host-authjs.csrf-token=d117d51bd880156f730b4da771f42489c6d0227f64919e702ac9366ec574c92f%7C489bc0a5beb645693d6f090a0e3f25e86ca18621d88ad8a5ba34d030dd783936; __Secure-authjs.callback-url=https%3A%2F%2Fwww.blackbox.ai; intercom-id-jlmqxicb=68a1cc65-49d6-4058-bc77-178be67348f3; intercom-session-jlmqxicb=; intercom-device-id-jlmqxicb=c10ddb73-19d7-4a36-9664-7f3cdee421b3"),
            "Origin": "https://www.blackbox.ai",
            "Priority": "u=1, i",
            "Referer": "https://www.blackbox.ai/chat/CATHvRo",
            "Sec-CH-UA": '"Chromium";v="130", "Microsoft Edge";v="130", "Not?A_Brand";v="99"',
            "Sec-CH-UA-Mobile": "?0",
            "Sec-CH-UA-Platform": '"Windows"',
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-origin",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36 Edg/130.0.0.0"
        })
        self.session.get(self.base_url)  # Initial GET request to the base URL
        
    def remove(self, input_string):
        # Define the pattern to match $@$ and the text between them
        result = re.sub(r'\$\@.*?\$\@\$', '', input_string)
        result = re.findall(r'```(.*?)```', result, re.DOTALL)[0]
        return result

    def get(self, message):
        request_body = {
            "query": message,
            "messages": [{"role": "user", "content": message, "id": "BLRH0Ly"}],
            "index": None
        }
        resp = self.session.post(self.check_endpoint, json=request_body)
        return resp
    
    def chat(self, message):
        if ( 'time' or 'date')  in message:
            message += ' '+str(time.localtime())
        request_body = {
            "messages": [
                {"role": "user", "content": "Generate using message to pyatogui commands like this *open explorer ```[{'gui':[['win','e']]}]```* or *open notepad and paste text ```[{'gui':[['win','r'],['write','notepad'],['enter'],['ctrl','v']]}]```* just give me that python list on output if If you're ask some random question or simple question not like an assistant like this some normal questions *what is raspberry pi```[{'audio':'Raspberry pi is a single board computer'}]```* or *What is Lenovo's latest laptop ```[{'audio':'IdeaPad Slim 5x Gen 9 - Snapdragon was the latsest Lenovo's laptop'}]```* just give me that dict on output now finally if the message to click some where go some where in pc just like this *Click on blank document ```[{'ocr':'blank document'}]```* use this only if this process is not possible in pyautogui just give a dict of ocr like this.", "id": "V3awdet"},
                {"role": "user", "content": "open vs code", "id": "V3awdet"},
                {"role": "assistant", "content": '''```[{'gui':[['win','r'],['write','code'],['enter']]}]```''', "id": "V3awdet"},
                {"role": "user", "content": """
                 ** *open explorer* ```[{'gui':[['win','e']]}]``` **
                 ** *open whatsapp* ```[{'gui':[['win'],['write','whatsapp'],['enter]]}]``` **
                 ** *open spotify* ```[{'gui':[['win'],['write','spotify']]}]``` **
                 ** *type this is a big content* ```[{'gui':[['write','this is a big content']]}]```**
                 ** *search python basics on youtube* ```[{'gui':[['win','r']],['write','chrome'],['enter'],['write','https://www.youtube.com/results?search_query=python+basics'],['enter]]}]```**
                 ** *play pal on spotify* ```[{'gui':[['win'],['write','spotify'],['enter'],['ctrl','k'],['write','pal'],['enter]]}]```**
                 ** *turn off wifi* ```[{'gui':[['win'],['WIFI settings']]},{'ocr':'off'}]```**
                 """, "id": "V3awdet"},
                {"role": "user", "content": "How to code in python", "id": "V3awdet"},
                {"role": "assistant", "content": '''```[{'audio':'Open VS code or any editor start tying print('hellow world!') then save the file and run python file_name.py in terminal'}]```''', "id": "V3awdet"},
                {"role": "user", "content": message, "id": "V3awdet"}
            ],
            "id": "OyoOKrY",
            "previewToken": None,
            "userId": None,
            "codeModelMode": True,
            "agentMode": {},
            "trendingAgentMode": {},
            "isMicMode": False,
            "userSystemPrompt": None,
            "maxTokens": 1024,
            "playgroundTopP": 0.9,
            "playgroundTemperature": 0.8,
            "isChromeExt": False,
            "githubToken": None,
            "clickedAnswer2": False,
            "clickedAnswer3": False,
            "clickedForceWebSearch": False,
            "visitFromDelta": False,
            "mobileClient": False,
            "userSelectedModel": None,
            "validated": self.secId
        }

        # Make POST request using requests session
        resp = self.session.post(self.chat_endpoint, json=request_body)
        try:
            return eval(self.remove(resp.text))
        except:
            return resp.text

# Usage example
blackbox = BlackBox("4aa22a15-a9b9-44db-8133-c0ed2657ab2e")
