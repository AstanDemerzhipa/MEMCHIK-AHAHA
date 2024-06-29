import discord
import random
from discord.ext import commands
import os




intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Привет! Я бот {bot.user}!')

@bot.command()
async def mem(ctx):
    with open('images/mem1.jpg', 'rb') as f:
        # В переменную кладем файл, который преобразуется в файл библиотеки Discord!
        picture = discord.File(f)
   # Можем передавать файл как параметр!
    await ctx.send(file=picture)

@bot.command()
async def raremem(ctx):
    with open('images/rare.jpg', 'rb') as f:
        # В переменную кладем файл, который преобразуется в файл библиотеки Discord!
        picture = discord.File(f)
   # Можем передавать файл как параметр!
    await ctx.send(file=picture)


@bot.command()
async def memr(ctx):
    img_name = random.choice(os.listdir('images'))
    with open(f'images/{img_name}', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)



@bot.command()
async def list_commands(ctx):
    embed = discord.Embed(title="Список команд", description="Список доступных команд бота", color=0x00ff00)

    embed.add_field(name="$hello", value="Приветствие от бота", inline=False)
    embed.add_field(name="$bye", value="Прощание", inline=False)
    embed.add_field(name="$sangulia", value="Отправляет сообщение 'САНГУЛИЯ ДВА!'", inline=False)
    embed.add_field(name="$add [число1] [число2]", value="Складывает два числа", inline=False)
    embed.add_field(name="$joined [упоминание_пользователя]", value="Показывает, когда пользователь присоединился к серверу", inline=False)
    embed.add_field(name="$choose [вариант1] [вариант2] ...", value="Выбирает один из предложенных вариантов", inline=False)
    embed.add_field(name="$heh [количество]", value="Отправляет 'he' заданное количество раз", inline=False)

    await ctx.send(embed=embed)

@bot.command()
async def bye(ctx):
    await ctx.send(f'Пока')

@bot.command()
async def sangulia(ctx):
    await ctx.send(f'САНГУЛИЯ ДВА!')

@bot.command()
async def add(ctx, left: int, right: int):
    await ctx.send(left + right)

@bot.command()
async def joined(ctx, member: discord.Member):
    """Says when a member joined."""
    await ctx.send(f'{member.name} joined {discord.utils.format_dt(member.joined_at)}')

@bot.command(description='For when you wanna settle the score some other way')
async def choose(ctx, *choices: str):
    """Chooses between multiple choices."""
    await ctx.send(random.choice(choices))

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)







bot.run("token")
