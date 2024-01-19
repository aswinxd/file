import asyncio
from pyrogram import filters
from bot import Bot

async def delete_bot_messages(client, chat_id, message_ids, delay):
    await asyncio.sleep(delay)
    try:
        await client.delete_messages(chat_id, message_ids)
    except Exception as e:
        print(f"Error deleting messages: {e}")

@Bot.on_message(filters.command("start"))
async def start_command_handler(client, message):
    pass  # You can add the logic for the start command if needed

@Bot.on_message(filters.private)
async def private_message_handler(client, message):
    bot_me = await Bot().get_me()
    if message.from_user.id == bot_me.id and not message.text.startswith("/start"):
        # Set the delay for message deletion (e.g., 10 seconds for testing)
        delay = 10  # seconds

        # Schedule a task to delete the bot's messages after the specified delay
        asyncio.create_task(delete_bot_messages(client, message.chat.id, [message.message_id], delay))
