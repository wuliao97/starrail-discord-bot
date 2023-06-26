from config import RESOURCES, USERS
from utils.functions import getUser, getClient, getDefaultInfo, quote


import discord
from discord.commands import Option
from discord.ext import commands



class Commands(commands.Cog):
    def __init__(self, bot:commands.Bot):
        self.bot = bot
        
    star_rail = discord.SlashCommandGroup(
        "star-rail", "Various Star rail Command"
    )
    
    
    @commands.Cog.listener()
    async def on_ready(self):
        print("[ COG ] Commands on set")
        
    
    @star_rail.command(name="profile")
    async def star_rail_profile(
        self, inter:discord.Interaction, user_id:Option(str, default=None)
    ):
        await inter.response.defer()
        data = await getDefaultInfo(user_id)
        
        
        e = discord.Embed(title=data.player.name + "'s info", description=quote(data.player.signature, "**"))
        e.set_thumbnail(url=getClient().get_icon_url(data.player.icon))
        
        e.add_field(name="Level", value=quote(data.player.level, "**"))
        
        e.add_field(name="UID", value=quote(data.player.uid, "**"))
        e.add_field(name="Characters", value=quote(data.player_details.characters, "**"))
        e.add_field(name="Achievements", value=quote(data.player_details.achievements, "**"))
        e.add_field(name="Simulated Universes", value=quote(data.player_details.simulated_universes, "**"))
        e.add_field(name="Forgotten Hall", value=quote(data.player_details.forgotten_hall, "**"))
        
        
        
        [print(i) for i in dir(data)]
        print("-----------------------------------")
        [print(i) for i in dir(data.player)]
        print("-----------------------------------")
        [print(i) for i in dir(data.player_details)]

        
        await inter.followup.send(embeds=[e])
    

def setup(bot:commands.Bot):
    return bot.add_cog(Commands(bot))
