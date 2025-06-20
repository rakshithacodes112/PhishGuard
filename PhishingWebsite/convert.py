import requests
import re
import csv
def convertion(url,prediction):
    name = []
    
    # found_url = find_url_in_csv('Datafiles/phishurls.csv', url)
    '''if "https://" in url:
        urlz = url.replace("https://","")
    if "http://" in url:
        urlz = url.replace("http://","")
    url_found = find_url_in_csv('Datafiles/legitimateurls.csv', urlz)'''
    
    if(shortlink(url)==-1):
        return [url,"Not Safe","redirect it to that website"]
    elif(prediction==1):
        return [url,"Safe","you can continue","1"]
    else:
        return [url,"Not Safe","redirect it to that website"]
def shortlink(url):
        

        match = re.search(r'bit\.ly|goo\.gl|shorte\.st|go2l\.ink|x\.co|ow\.ly|t\.co|tinyurl|tr\.im|is\.gd|cli\.gs|'
                          r'yfrog\.com|migre\.me|ff\.im|tiny\.cc|url4\.eu|twit\.ac|su\.pr|twurl\.nl|snipurl\.com|'
                          r'short\.to|BudURL\.com|ping\.fm|post\.ly|Just\.as|bkite\.com|snipr\.com|fic\.kr|loopt\.us|'
                          r'doiop\.com|short\.ie|kl\.am|wp\.me|rubyurl\.com|om\.ly|to\.ly|bit\.do|t\.co|lnkd\.in|'
                          r'db\.tt|qr\.ae|adf\.ly|goo\.gl|bitly\.com|cur\.lv|tinyurl\.com|ow\.ly|bit\.ly|ity\.im|'
                          r'q\.gs|is\.gd|po\.st|bc\.vc|twitthis\.com|u\.to|j\.mp|buzurl\.com|cutt\.us|u\.bb|yourls\.org|'
                          r'x\.co|prettylinkpro\.com|scrnch\.me|filoops\.info|vzturl\.com|qr\.net|1url\.com|tweez\.me|v\.gd|tr\.im|link\.zip\.net',
                          url)

        if match:
            return -1
        return 1
def find_url_in_csv(csv_file, target_url):
    with open(csv_file, 'r', newline='', encoding='utf-8') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            url = row [0].strip() 
            if url == target_url:
                return url
    return None
