import voltage
import requests
import random
from voltage.ext.commands import Cog


def setup(client: voltage.Client) -> Cog:
    fun = Cog("Fun", "Random and fun stuff.")

    @fun.command(description="Gives you a random cat image and fact.", aliases=["catto", "meow", "kitty", "kitten", "cat"])
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

    @fun.command(description="Gives you a random dog image and fact.", aliases=["doggo", "bark", "puppy", "pupper", "pup", "dog"])
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

    @fun.command(description="Gives you a random fox image.", aliases=["foxy", "floof", "fox"])
    async def fox(ctx):
        request = requests.get("https://randomfox.ca/floof/")
        fox = request.json()
        embed = voltage.SendableEmbed(
            title="What does the fox say?",
            description="Here's your fox!",
            media=fox["image"]
        )

        await ctx.send(content="#", embed=embed)

    @fun.command(description="Gives you a random duck image.", aliases=["ducky", "quack", "duck"])
    async def duck(ctx):
        request = requests.get("https://random-d.uk/api/v2/random")
        duck = request.json()
        embed = voltage.SendableEmbed(
            title="Quack!",
            description="Here's your duck!",
            media=duck["url"]
        )

        await ctx.send(content="#", embed=embed)

    @fun.command(description="Rolls a die for you.", aliases=["die", "dice", "diceroll", "random", "roll"])
    async def roll(ctx, sides: int=6) -> None:
        await ctx.send(f"You rolled a **{random.randint(1, sides)}**")

    @fun.command(description="Flips a coin for you", aliases=["coin", "flip", "coin_flip"])
    async def coin_flip(ctx) -> None:
        await ctx.send(f"Your coin landed on **{random.choice(['heads', 'tails'])}**")

    @fun.command(description="Sends a user-provided message. Pretty useless, but it's there.")
    async def say(ctx, *, message: str=None) -> None:
        prefix = await ctx.client.get_prefix(ctx.message, ctx.client.prefix)
        if message == None:
            return await ctx.send("provide something for me to say you idiot")
        elif message.startswith(prefix):
            return await ctx.send("stop ratelimiting me lmfao")
        await ctx.send(message)


    return fun
