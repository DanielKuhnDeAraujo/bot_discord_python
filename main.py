import discord
from discord import app_commands
import random2
from random2 import randint

class MeuPrimeiroBot(discord.Client):
    def __init__(self):
        intents = discord.Intents.all()
        super().__init__(
            command_prefix = "!_!",
            intents= intents
        )
        self.tree = app_commands.CommandTree(self)

    async def setup_hook(self):
        await self.tree.sync()
        # guild=discord.object(id=0) colocar isso dentro da aspas pra sincronizar com um só servidor. substituir 0 pelo id do servidor
    
    async def on_ready(self) :
        print(f"O bot {self.user} foi iniciado.")
botin = MeuPrimeiroBot()

#interaction.user.mention é o nome do usuário
# ao colocar ephemeral=True para q a msg seja secreta
@botin.tree.command(name="pdi" , description="Ponto de interrogação")
async def pdi(interaction:discord.Interaction) :
    await interaction.response.send_message("?")

@botin.tree.command(name="d" , description="Dado com X lados")
@app_commands.describe(
    num="Número máximo do dado."
)
async def pdi(interaction:discord.Interaction,num:int) :
    msg=""
    msg= ("O resultado do d"+str(num)+" foi: "+str(randint(1,num)))
    await interaction.response.send_message(msg)

@botin.tree.command(name="ad" , description="X dados com X lados com X bônus")
@app_commands.describe(  
    num="Número máximo do dado."
)
@app_commands.describe(  
    bns="Bônus"
)
@app_commands.describe(  
    qtd="Quantidade de dados"
)
async def pdi(interaction:discord.Interaction,qtd:int,num:int,bns:int) :
    msg=""
    for i in range(0,qtd) :
        msg += ("O resultado do d"+str(num)+"com bônus de "+str(bns)+" foi: "+str((randint(1,num))+bns)+"\n")
    await interaction.response.send_message(msg)



botin.run("colocar aqui o id do bot)
