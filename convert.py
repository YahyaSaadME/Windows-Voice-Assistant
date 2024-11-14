# Use this prompts in llm api like google vortex, gemini,open ai, etc. to generate the above code snippet. 

{
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
            ]}