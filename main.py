#tetrio
import asyncio
from teto.client import RibbonClient

async def on_ready(data):
    print("on_ready handler called")
    global roomid
    await client.room.join_room(roomid.upper())

async def on_room_join(data):
    await client.room.switch_brackets(True)

async def main():
    #tetrio
    token = "tetr.io bot token"

    global client, roomid
    client = RibbonClient(token)

    roomid = input("Enter room ID to join: ")

    client.on("client.room.join", on_room_join)

    print("Registering client.ready handler")
    client.on("client.ready", on_ready)
    print("Handler registered, connecting...")
    await client.connect()

    try:
        while True:
            a = 1
    except KeyboardInterrupt:
        if client.room.current_room:
            await client.room.leave_room()
        await client.close()

asyncio.run(main())
