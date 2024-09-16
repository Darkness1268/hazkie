#Hazkie
class colors:
    BIGreen = "[\033[1;92m\]"
    cyan = "\033[1;36m"

print(colors.BIGreen + """
╔═══╦══╗─╔═══╦═══╦═══╦═══╦═══╦════╗╔════╦═══╦═══╦╗
║╔══╣╔╗║─║╔═╗║╔══╣╔═╗║╔═╗║╔═╗║╔╗╔╗║║╔╗╔╗║╔═╗║╔═╗║║
║╚══╣╚╝╚╗║╚═╝║╚══╣╚═╝║║─║║╚═╝╠╝║║╚╝╚╝║║╚╣║─║║║─║║║
║╔══╣╔═╗║║╔╗╔╣╔══╣╔══╣║─║║╔╗╔╝─║║────║║─║║─║║║─║║║─╔╗
║║──║╚═╝║║║║╚╣╚══╣║──║╚═╝║║║╚╗─║║────║║─║╚═╝║╚═╝║╚═╝║
╚╝──╚═══╝╚╝╚═╩═══╩╝──╚═══╩╝╚═╝─╚╝────╚╝─╚═══╩═══╩═══╝""")
print(colors.cyan + u'\033[40m' + """
            ▄▄▄▄
          ▄██████     ▄▄▄█▄
        ▄██▀░░▀██▄    ████████▄
       ███░░░░░░██     █▀▀▀▀▀██▄▄
     ▄██▌░░░░░░░██    ▐▌       ▀█▄
     ███░░▐█░█▌░██    █▌         ▀▌
    ████░▐█▌░▐█▌██   ██
   ▐████░▐░░░░░▌██   █▌
    ████░░░▄█░░░██  ▐█
    ████░░░██░░██▌  █▌
    ████▌░▐█░░███   █
    ▐████░░▌░███   ██
     ████░░░███    █▌
   ██████▌░████   ██
 ▐████████████   ███
 █████████████▄████
██████████████████
██████████████████
█████████████████▀
█████████████████
████████████████
████████████████


 """)
print("[+]A FB AUTO-REPORT v1 Created By HAZKIE DEV[+]")

import requests  
import json  
  
# Constants  
ACCESS_TOKEN = 'your_access_token'  
PAGE_ID = 'your_page_id'  
REPORT_URL = f'https://graph.facebook.com/v12.0/{PAGE_ID}/insights'  
  
# Function to generate report  
def generate_report(since, until):  
   params = {  
      'access_token': ACCESS_TOKEN,  
      'metric': 'page_impressions,page_engaged_users',  
      'period': 'day',  
      'since': since,  
      'until': until  
   }  
  
   try:  
      response = requests.get(REPORT_URL, params=params)  
      response.raise_for_status()  # Raise an exception for 4xx or 5xx status codes  
   except requests.RequestException as e:  
      print(f"Failed to generate report: {e}")  
      return  
  
   try:  
      report_data = response.json()  
   except json.JSONDecodeError as e:  
      print(f"Failed to parse JSON response: {e}")  
      return  
  
   if 'data' in report_data and isinstance(report_data['data'], list):  
      try:  
        with open('facebook_report.json', 'w') as report_file:  
           json.dump(report_data, report_file, indent=4)  
        print("Report generated successfully.")  
      except IOError as e:  
        print(f"Failed to write report to file: {e}")  
   else:  
      print("Failed to generate report: Unexpected response data")  
  
# Execute the function  
if __name__ == "__main__":  
   since = '2023-01-01'  
   until = '2023-01-31'  
   generate_report(since, until)
