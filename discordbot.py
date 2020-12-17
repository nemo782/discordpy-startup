from discord.ext import commands
import os
import traceback

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
    
    if message.author.bot:
        return
    # 「/もりちゃん」と発言したら「ﾃﾞｭﾌﾌ」が返る処理
    if message.content == '/もりちゃん':
        await message.channel.send('???(ﾃﾞｭﾌﾌ)')

    # 「/やおさん」と発言したら「以下の文章」が返る処理
    if message.content == '/やおさん':
        await message.channel.send('ﾝﾝ紫アーマーで殴ってくんのは違うじゃん！！')

    # 「/apex character」と発言したら「キャラガチャ」が始まる処理
    if message.content == '/apex character':
        character = ["ブラハ","ジブ","ライフラ","パスファ","レイス","バンガ","ミラージュ","コースティック","オクタン","ワットソン","クリプト","レヴナント","ローバー","ランパート","ホライゾン" ]
        character_number = random.randint(0,14)
        await message.channel.send("今回は" + character[character_number] + "に決定！")
bot.run(token)
