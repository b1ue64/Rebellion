import voltage
import random
from voltage.ext.commands import Cog

def setup(client: voltage.Client) -> Cog:
    misc = Cog("Misc", "Stuff that wouldn't fit anywhere else.")

    @misc.command()
    async def ping(ctx) -> None:
        await ctx.send("pong")
    
    return misc