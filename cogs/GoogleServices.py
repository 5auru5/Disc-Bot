#internalcommands.py
import os
import time
import datetime
from discord.ext import commands

class GoogleServices(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='Calendar', help='Create and manage Google Calendar events')
    async def Calendar(self, ctx, string="options"):
        if string == "options":
            optionsScreen = "```Here are the commands you can use:\n +Calendar Create - Create a calendar\n +Calendar edit - Edit a calendar\n +Calendar delete - Delete a calendar event\n +Calendar invite - Invite a user to a calendar```"
            await ctx.send(optionsScreen)
        if string == "create":
            await ctx.send("Creating a calendar event!")
        if string == "edit":
            await ctx.send("Editing a calendar event!")
        if string == "delete":
            await ctx.send("Deleting a calendar event!")
        if string == "invite":
            await ctx.send("Please Select a calendar event")
        await ctx.send("NOTE: This command is being configured")
    
    @commands.command(name='Docs', help='Create and manage Google Docs')
    async def Docs(self, ctx, string="options"):
        if string == "options":
            optionsScreen = "```Here are the commands you can use:\n +Docs Create - Create a Google Doc\n +Docs invite - Invite a user to a Google Doc\n```"
            await ctx.send(optionsScreen)
        if string == "create":
            await ctx.send("Creating a new Google Doc!")
        if string == "invite":
            await ctx.send("Ivitation Sent!")   
        await ctx.send("NOTE: This command is being configured")

    @commands.command(name='Sheets', help='Create and manage Google Sheets')
    async def Sheets(self, ctx, string="options"):
        if string == "options":
            optionsScreen = "```Here are the commands you can use:\n +Sheets Create - Create a Google Sheet\n +Sheets invite - Invite a user to a Google Sheet\n```"
            await ctx.send(optionsScreen)
        if string == "create":
            await ctx.send("Creating a new Google Sheet!")
        if string == "invite":
            await ctx.send("Ivitation Sent!")
        await ctx.send("NOTE: This command is being configured")
    
    @commands.command(name='Slides', help='Create and manage Google Slides')
    async def Slides(self, ctx, string="options"):
        if string == "options":
            optionsScreen = "```Here are the commands you can use:\n +Slides Create - Create a Google Slide\n +Slides invite - Invite a user to a Google Slide\n```"
            await ctx.send(optionsScreen)
        if string == "create":
            await ctx.send("Creating a new Google Slide!")
        if string == "invite":
            await ctx.send("Ivitation Sent!")
        await ctx.send("NOTE: This command is being configured")
def setup(bot):
    bot.add_cog(GoogleServices(bot))




