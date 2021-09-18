from requests import post as url_post
from bs4 import BeautifulSoup
from json import loads

class engine():
    ''' The core of the program to send and receive messages '''
    
    def sender_message(text: str,bot_token: str,chat_id: str):
        ''' Send message in bot '''
        
        ## api urls
        send_url = f"https://api.telegram.org/bot{bot_token}/SendMessage?chat_id={chat_id}&text={text}"
        site_sender = "https://www.httpdebugger.com/Tools/ViewHttpHeaders.aspx"
        
        ## payload for send a post request
        payload = {"UrlBox": send_url,
                    "AgentList": "Mozilla Firefox",
                    "VersionsList": "HTTP/1.1",
                    "MethodList": "POST"
                    }
    
        try:
            
            ## send post request for send message
            url_post(url=site_sender,data=payload)
            
        except Exception as ex:
            print(f"ERROR [sneder message] {ex}")
            return False
        else:

            return True

    def receive_message(bot_token: str) -> dict:
        ''' receive message from bot '''
        ## api urls
        receve_url = f"https://api.telegram.org/bot{bot_token}/Getupdates"
        site_sender = "https://www.httpdebugger.com/Tools/ViewHttpHeaders.aspx"
        
        ## payload for send a post request
        payload = {"UrlBox": receve_url,
                    "AgentList": "Mozilla Firefox",
                    "VersionsList": "HTTP/1.1",
                    "MethodList": "POST"
                    }
        
        try:
            ## send request in receive message api
            response = url_post(url=site_sender,data=payload)
            
            ## Extraction data from response
            response = response.text
            response = BeautifulSoup(response, "html.parser")
            response = response.find("div", id="ResultData").text.replace("Response Content",'')
            
        except Exception as ex:
            print(f"ERROR [sneder message] {ex}")
            return False
        else:
            ## return json data as dict
            return  loads(response)