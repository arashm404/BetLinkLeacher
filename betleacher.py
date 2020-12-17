from telethon.sync import TelegramClient # import modules
import re # import regex 
api_id = 1581224 #PUT YOUR API_ID HERE
api_hash = 'bd891fcb8726cfbd64abc9ddbba2c8ff'#PUT YOUR API_HASH HERE
client = TelegramClient('lcr',api_id,api_hash)#create client
client.start()#start client 
messages = [item.text for item in client.iter_messages('AmirTatalooOriginal')]#get messages
black_domain = ['youtu.be','deezer','instagram','spotify','youtube']#black list for leach link
domains = []#domains list
def search(text):
    w = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', text)[0]
    return w
def check(text):
    i = False
    for item in black_domain:
        if item in text:
            i = True
    return i
for item in messages:
    try:
        link = search(item)
        if check(link) == False:
            domains.append(link)
    except:
        continue
print(domains)

