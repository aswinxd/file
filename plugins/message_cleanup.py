import asyncio
from pyrogram import filters, Client
from datetime import datetime, timedelta

from bot import Bot

async def delete_bot_messages(client, chat_id, message_ids, delay):
    await asyncio.sleep(delay)
    try:
        await client.delete_messages(chat_id, message_ids)
    except Exception as e:
        print(f"Error deleting messages: {e}")

@Bot.on_message(filters.outgoing)
async def outgoing_message_handler(client, message):
    # Set the delay for message deletion (e.g., 5 minutes)
    delay = 5 * 60  # seconds

    # Schedule a task to delete the bot's messages after the specified delay
    asyncio.create_task(delete_bot_messages(client, message.chat.id, [message.message_id], delay))
