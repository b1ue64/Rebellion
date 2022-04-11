import voltage
import requests
import random
from voltage.ext.commands import Cog


async def get_prefix(message, client):
    if message.server is None:
        return ['r!', client.user.mention+' ', client.user.mention]
    with open ("prefixes.json", "r") as f:
        prefixes = json.load(f)
    return [prefixes.get(str(message.server.id), "-"), client.user.mention+' ', client.user.mention]

def setup(client: voltage.Client) -> Cog:
    fun = Cog("Fun", "Random and fun stuff.")

    @fun.command()
    async def cat(ctx):
        request = requests.get("https://cataas.com/cat?json=true")
        fact_request = requests.get("https://catfact.ninja/fact")
        cat = request.json()
        fact = fact_request.json()
        embed = voltage.SendableEmbed(
            title="Meow!",
            description=fact["fact"],
            media=f"https://cataas.com{cat['url']}"
        )

        await ctx.send(content="#", embed=embed)
    
    @fun.command()
    async def dog(ctx):
        request = requests.get("https://dog.ceo/api/breeds/image/random")
        fact_request = requests.get("https://dog-api.kinduff.com/api/facts")
        dog = request.json()
        fact = fact_request.json()
        embed = voltage.SendableEmbed(
            title="Woof!",
            description=fact["facts"][0],
            media=dog["message"]
        )

        await ctx.send(content="#", embed=embed)
    
    @fun.command()
    async def fox(ctx):
        request = requests.get("https://randomfox.ca/floof/")
        fox = request.json()
        embed = voltage.SendableEmbed(
            title="What does the fox say?",
            description="Here's your fox!",
            media=fox["image"]
        )

        await ctx.send(content="#", embed=embed)
    
    @fun.command()
    async def duck(ctx):
        request = requests.get("https://random-d.uk/api/v2/random")
        duck = request.json()
        embed = voltage.SendableEmbed(
            title="Quack!",
            description="Here's your duck!",
            media=duck["url"]
        )

        await ctx.send(content="#", embed=embed)
    
    @fun.command()
    async def roll(ctx, sides: int=6) -> None:
        await ctx.send(f"You rolled a **{random.randint(1, sides)}**")

    @fun.command()
    async def coin_flip(ctx) -> None:
        await ctx.send(f"Your coin landed on **{random.choice(['heads', 'tails'])}**")
    
    @fun.command()
    async def say(ctx, *, message: str=None) -> None:
        prefix = await ctx.client.get_prefix(ctx.message, ctx.client.prefix)
        if message == None:
            return await ctx.send("provide something for me to say you idiot")
        elif message.startswith(prefix):
            return await ctx.send("stop ratelimiting me lmfao")
        await ctx.send(message)
    
    
    return fun