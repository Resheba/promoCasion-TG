from telethon import TelegramClient, events
from config import api_hash, api_id
from parserCas import startSiteWork
from datetime import datetime
from pytess import get_cods
import os


BASE_DIR = os.path.dirname(os.path.dirname(__file__))


client = TelegramClient('anon', api_id, api_hash)
client.start()
startSiteWork()

@client.on(events.NewMessage(chats = ('kleinebock'))) # здесь указываем все каналы для просмотра. В данном случае это будет ('burmalkreed','burmalduster')
async def pars_hendler_burmalduster(event):
    photoId = event.message.to_dict()['id']
    print('Get new message!')
    if event.message.to_dict().get('media'):
        time = str(datetime.now().date())
        time = time.replace('-', '_').replace(' ', '_').replace('.', '_')
        await client.download_media(event.message,file=f'Photo/{photoId}_{time}.jpg')
        nameDuster = f'{photoId}_{time}.jpg'

        cods = await get_cods(name=nameDuster)
        print(cods)
        startSiteWork(cods)


# @client.on(events.NewMessage(chats = ('burmalkreed')))
# async def pars_hendler_burmalkreed(event):
#     photoId = event.message.to_dict()['id']
#     time = str(datetime.now().date())
#     time = time.replace('-', '_').replace(' ', '_').replace('.', '_')
#     file = f'Photo_Burmalkreed/{photoId}_{time}.jpg'
#     await client.download_media(event.message,file=file)
#     nameKreed = f'{photoId}_{time}.jpg'
#     await get_cods(name=nameKreed)


client.run_until_disconnected()
