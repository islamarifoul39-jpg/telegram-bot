import asyncio
import random
from telethon import TelegramClient

API_ID = 36154784
API_HASH = 'a6fbcc32fb4da179d5736aae32efc382'
SHARE_LINK = "https://t.me/bridalvideogroup"

# গ্রুপগুলোর তালিকা এবং সঠিক সময়সূচী (সেকেন্ডে হিসাব)
GROUPS_CONFIG = [
    {"chat_id": "@NlRGI3anYY5kODFl", "base_interval": 3600},   # ১ ঘণ্টা পরপর
    {"chat_id": "@lC7i-XANtKZkNjc1", "base_interval": 3600},   # ১ ঘণ্টা পরপর
    {"chat_id": "@free_link_up", "base_interval": 900},       # ১৫ মিনিট পরপর
    {"chat_id": "@linksharefree65", "base_interval": 30},     # ৩০ সেকেন্ড পরপর
    {"chat_id": "@m1DOXGOhi6NkNTFk", "base_interval": 300},   # ৫ মিনিট পরপর
    {"chat_id": "@free_link_share_group_SS", "base_interval": 3600}, # ১ ঘণ্টা পরপর
    {"chat_id": "@FREE_LINK_SHARE_10_K", "base_interval": 30} # ৩০ সেকেন্ড পরপর
]

client = TelegramClient('my_session', API_ID, API_HASH)

async def send_to_group(chat_id, interval):
    while True:
        try:
            jitter = random.randint(2, 7)
            current_sleep = interval + jitter
            await asyncio.sleep(current_sleep)
            await client.send_message(chat_id, SHARE_LINK)
            print(f"Message sent to {chat_id}")
        except Exception as e:
            print(f"Error sending to {chat_id}: {e}")
            await asyncio.sleep(10)

async def main():
    print("Userbot is starting 24/7 automation...")
    await client.start()
    tasks = [send_to_group(item["chat_id"], item["base_interval"]) for item in GROUPS_CONFIG]
    await asyncio.gather(*tasks)

with client:
    client.loop.run_until_complete(main())
