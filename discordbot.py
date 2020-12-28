import discord
from discord.ext import commands
# from pydub import AudioSegment
# from pydub.playback import play
import os
import time

bot = commands.Bot(command_prefix='$')
ACCESS_TOKEN = os.environ['DISCORD_BOT_TOKEN']

if not discord.opus.is_loaded():
    discord.opus.load_opus("heroku-buildpack-libopus")

@bot.command()
async def ign(ctx):
    voice_status = ctx.author.voice

    if not voice_status:
        return
    
    await voice_status.channel.connect()
    await ctx.send('ignition on')

@bot.command()
async def start(ctx):
    voice_status = ctx.author.voice

    if not voice_status:
        return
    
    await voice_status.channel.connect()
    await ctx.send('lamborghini start up...')
    time.sleep(2)
    voice_file = discord.FFmpegPCMAudio('./special/starter2.wav')
    await ctx.message.guild.voice_client.play(voice_file)

@bot.command()
async def amo(ctx, *args):
    voice_status = ctx.author.voice
    voice_client = ctx.message.guild.voice_client

    if not voice_status:
        await ctx.send('aaaaaaaaaaaaaaamoooooooooo')
        return

    if len(args) > 0:
        file_name = args[0]
    else:
        file_name = 'amo1'

    # if args[1:2]:
    #     pitch = float(int(args[1]) / 100)
    #     change(file_name, pitch)
    #     file_name = 'out'

    voice_file = discord.FFmpegPCMAudio('./wav/' + file_name + '.wav')
    await ctx.message.guild.voice_client.play(voice_file)

@bot.command()
async def disconnect(ctx):
    voice_client = ctx.message.guild.voice_client
    
    if not voice_client:
        return

    await voice_client.disconnect()

@bot.command()
async def bye(ctx):
    print('bye')
    await bot.close()
    sys.exit()

# def change(file_name, pitch):
#     sound = AudioSegment.from_file('./wav/' + file_name + '.wav', format="wav")
#     octaves = 0.5
#     new_sample_rate = int(sound.frame_rate * (pitch ** octaves))

#     hipitch_sound = sound._spawn(sound.raw_data, overrides={'frame_rate': new_sample_rate})
#     hipitch_sound = hipitch_sound.set_frame_rate(44100)
#     hipitch_sound.export("./wav/out.wav", format="wav")
    

bot.run(ACCESS_TOKEN)