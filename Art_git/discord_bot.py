import discord
import time

client = discord.Client()
Token = "Put your Bot token in here"
channel_code = "put your channel code here make sure its an int"


@client.event
# This sets up the bot and checks your file path for the screen shots
async def on_ready():
    print("Logged in")
    screenshots = 3
    while True:
        try:
            # put your channel code here
            channel = client.get_channel(channel_code)
            await channel.send(file=discord.File(r"C:/Desktop" + str(screenshots) + ".png"))
            print("succesfully uploaded")
            screenshots += 1
        except:
            time.sleep(10)
            print("Failed waiting 5 seconds for another")
        time.sleep(20)

client.run(Token)
