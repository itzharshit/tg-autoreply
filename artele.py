import time
from telethon import TelegramClient, events

# this is secret, do not share with anyone
api_id = 14456079
api_hash = '51da94efc990b58e3db3c897fc24e8d6'
string =''
 #this is where your session data will persist. You can name the file anything you want.

message = '**AUTO REPLY** \n\nHey baby!!\n\nSorry Im not answering private msgs right now but I have everything you need. So if youre looking for a sexy fun time, I can provide it. Come & join me at my website, get my exclusive naughty content & lets chat 1-on-1 together.\n\nSee you there,\n-elly xoxo\n\n https://elly.onepage.me \n\n**AUTO REPLY**'

if __name__ == '__main__':
    #Create the client
    # use sequential_updates=True to respond to messages one at a time
    client  = TelegramClient(StringSession(string), api_id, api_hash)


    @client.on(events.NewMessage(incoming=True)) #handle only incoming messages
    async def handle_new_message(event):
        if event.is_private: #only reply to private chats
            from_ = await event.get_sender()
            print(from_)
            print(time.asctime(), '-',  event.message)
            time.sleep(30)
            me_ = await client.get_me()
            if isinstance(me_.status, telethon.tl.types.UserStatusOffline):
                await event.respond(message)
            else:
                print(passed)

    # Function to get all the open/current dialogs
    def setup():
        users = set()
        for dialog in client.iter_dialogs():
            if dialog.is_user:
                print(dialog)
                users.add(dialog.id)  
    
    
    print(time.asctime(), '-', 'Auto-replying turned on for you...')
    client.start(phone) # start client istance
    setup()
    client.run_until_disconnected() #run auto reply until disconnected 
    print(time.asctime(), '-', 'Stopped Auto-reply')
