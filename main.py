import win32com.client as wincom
import speech_recognition as sr
import webbrowser
import os
import datetime 
import openai
from config import apikey


chatStr = ""

def chat(query):
    global chatStr
    print(chatStr)
    openai.api_key = apikey
    chatStr += f"Addy: {query}\n Tom: "
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt= chatStr,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    # todo: Wrap this inside of a  try catch block
    say(response["choices"][0]["text"])
    chatStr += f"{response['choices'][0]['text']}\n"
    return response["choices"][0]["text"]


def ai(prompt):
  openai.api_key = apikey
  text=f"OpenAI response for Prompt: {prompt}  \n********************\n\n"
  response = openai.Completion.create(
  model="text-davinci-003",
  prompt=prompt,
  temperature=1,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
  )
  
  text+= response["choices"][0]["text"]
  if not os.path.exists("Openai"):
      os.mkdir("Openai")
  with open(f"Openai/{''.join(prompt.split('intelligence')[1:]) }.txt","w") as f:
     f.write(text)


def say(text):
  speak=wincom.Dispatch("SAPI.SPVOICE")
  speak.Speak(f"{text}")
def takecommand():
   r=sr.Recognizer()
   with sr.Microphone() as source:
      r.pause_threshold=0.8 #By default it is 0.8 , so you can change it manually also
      audio=r.listen(source)
      try:
           query=r.recognize_google(audio,language="en-in")
           print(f"User said:{query}")
           return query
      except Exception as e:
         return "Some error Occured..."

if __name__=="__main__":
   print("Vscode")
   say("Hello Iam Tom ")
   while(True):
    print("Listening...")
    query=takecommand()
    #To add sites 
    sites=[["Wikipedia","https://www.wikipedia.org"],["Google","https://google.com"],["youtube","https://www.youtube.com"]]
    for site in sites:
       if f"Open {site[0]}".lower() in query.lower():
          say(f"Opening {site[0]} sir..")
          webbrowser.open(site[1])
          break
    if  "play music".lower() in query.lower(): # To add music
          musicpath= "# PASTE the Path"
          say("playing music..")
          os.startfile (musicpath)
          break
    elif "the time".lower() in query.lower(): #TO add time
       strfTime= datetime.datetime.now().strftime("%H:%M:%S")
       say(f"Sir the time is {strfTime}")
       print(f"The Time is {strfTime}")
    elif "using artificial intelligence".lower()in query.lower(): #To search and save it in a file
       ai(prompt=query)
    elif "see you later".lower() in query.lower():
      say(" Good Bye see you later....")
      exit()
    elif "reset chat".lower() in query.lower():
            chatStr = ""
    else:
       print("Chatting...")
       chat(query)

        

   
    















