import csv
import telethon
from telethon.sync import TelegramClient
from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.types import InputPeerEmpty

phone = '***'
api_id = ***
api_hash = "***"

client = TelegramClient('test')

client.start()

