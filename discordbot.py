from discord.ext import commands
import os
import traceback
import random

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']


@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)


@bot.command()
async def ping(ctx):
    await ctx.send('pong')

@bot.command()
async def neko(ctx):
    await ctx.send('にゃーん')
    
@bot.command()
async def もりちゃん(ctx):
    await ctx.send('???(ﾃﾞｭﾌﾌ)')
    
@bot.command()
async def やおさん(ctx):
    await ctx.send('なるほどね(理解していない)')

@bot.comannd() 
async def apex character(ctx):
        character = ["ブラハ","ジブ","ライフラ","パスファ","レイス","バンガ","ミラージュ","コースティック","オクタン","ワットソン","クリプト","レヴナント","ローバー","ランパート","ホライゾン" ]
        character_number = random.randint(0,14)
        await ctx.send("今回は" + character[character_number] + "に決定！")
bot.run(token)
