import time
from telethon import TelegramClient, events
import re
import sys
from os import getenv
from telethon.sessions import StringSession
# this is secret, do not share with anyone
api_id = 14456079
api_hash = '51da94efc990b58e3db3c897fc24e8d6'
string = getenv("STRING")
 #this is where your session data will persist. You can name the file anything you want.
phone = '+380944672240'
message = '**Hello sir, this is a auto replied message. I am currently offline.**\n\nIf you want to know the price of premium save restricted contents bot, you can check it below\n\n✓1 Week - 6$(USD)\n✓ 1 Month - $13(USD) \nPayment mode is any crypto (BTC __preferable__)\n\nIf you want to subscribe premium feature you can reply otherwise you are free from here.'

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
