import math
from discord.ext import commands
import discord
intents = discord.Intents.all()
intents.presences = False
client = commands.Bot(command_prefix='!', intents=intents)

@client.command()
async def gs(ctx, stat1, stat2, stat3, stat4):
    first, second, third, fourth = 0.0, 0.0, 0.0, 0.0
    #if this is a speed, crit chance, or crit damage stat convert
    if stat1[0:3] == 'spd' or stat1[0:2] == 'cc' or stat1[0:2] == 'cd' or stat1[0:3] == 'att' or stat1[0:3] == 'def' or stat1[0:2] == 'hp':
        if stat1[0:3] == 'spd':
            first = float(stat1[3:])*2
        elif stat1[0:2] == 'cc':
            first = float(stat1[2:])*1.6
        elif stat1[0:2] == 'cd':
            first = float(stat1[2:])*1.14
        elif stat1[0:3] == 'att':
            first = float(stat1[3:])/10
        elif stat1[0:3] == 'def':
            first = float(stat1[3:])/6
        elif stat1[0:2] == 'hp':
            first = float(stat1[2:])/50
    else:
        first = float(stat1)

    if stat2[0:3] == 'spd' or stat2[0:2] == 'cc' or stat2[0:2] == 'cd' or stat2[0:3] == 'att' or stat2[0:3] == 'def' or stat2[0:2] == 'hp':
        if stat2[0:3] == 'spd':
            second = float(stat2[3:])*2
        elif stat2[0:2] == 'cc':
            second = float(stat2[2:])*1.6
        elif stat2[0:2] == 'cd':
            second = float(stat2[2:])*1.14
        elif stat2[0:3] == 'att':
            first = float(stat2[3:])/10
        elif stat2[0:3] == 'def':
            first = float(stat2[3:])/6
        elif stat2[0:2] == 'hp':
            first = float(stat2[2:])/50
    else:
        second = float(stat2)

    if stat3[0:3] == 'spd' or stat3[0:2] == 'cc' or stat3[0:2] == 'cd' or stat3[0:3] == 'att' or stat3[0:3] == 'def' or stat3[0:2] == 'hp':
        if stat3[0:3] == 'spd':
            third = float(stat3[3:])*2
        elif stat3[0:2] == 'cc':
            third = float(stat3[2:])*1.6
        elif stat3[0:2] == 'cd':
            third = float(stat3[2:])*1.14
        elif stat3[0:3] == 'att':
            first = float(stat3[3:])/10
        elif stat3[0:3] == 'def':
            first = float(stat3[3:])/6
        elif stat3[0:2] == 'hp':
            first = float(stat3[2:])/50
    else:
        third = float(stat3)

    if stat4[0:3] == 'spd' or stat4[0:2] == 'cc' or stat4[0:2] == 'cd' or stat4[0:3] == 'att' or stat4[0:3] == 'def' or stat4[0:2] == 'hp':
        if stat4[0:3] == 'spd':
            fourth = float(stat4[3:])*2
        elif stat4[0:2] == 'cc':
            fourth = float(stat4[2:])*1.6
        elif stat4[0:2] == 'cd':
            fourth = float(stat4[2:])*1.14
        elif stat4[0:3] == 'att':
            first = float(stat4[3:])/10
        elif stat4[0:3] == 'def':
            first = float(stat4[3:])/6
        elif stat4[0:2] == 'hp':
            first = float(stat4[2:])/50
    else:
        fourth = float(stat4)

    await ctx.reply(first + second + third + fourth)


class MyHelp(commands.MinimalHelpCommand):
    async def send_bot_help(self, mapping):
        embed = discord.Embed(title="GS Bot Help",
                                 description="Type in !gs and then your 4 stats. "
                                             "For speed, crit chance, and crit damage, "
                                             "include spd, cc, cd in front of those numbers. "
                                             "For flat stats, make sure to include att, def, hp in front of those numbers. Enjoy!\n"
                                             "\n Ex: !gs 5cc 10spd 15 20")
        destination = self.get_destination()
        await destination.send(embed=embed)


client.help_command = MyHelp()

@client.event
async def on_ready():
    print(f'{client.user.name} is ready to use')

client.run('MTA0ODQ5MzAzNjIxODM2ODA3Mw.GlqDpn.XbE4B5SONW94LiWQ-bLUdhBB86c2tMbz6xp4Dk')