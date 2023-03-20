import discord
from discord import app_commands

id_do_servidor =  #seu id

class client(discord.Client):
    def __init__(self):
        super().__init__(intents=discord.Intents.default())
        self.synced = False 

    async def on_ready(self):
        await self.wait_until_ready()
        if not self.synced: 
            await tree.sync(guild = discord.Object(id=id_do_servidor)) 
            self.synced = True
        print(f"Entramos como {self.user}.")

aclient = client()
tree = app_commands.CommandTree(aclient)

@tree.command(guild = discord.Object(id=id_do_servidor), name = 'teste', description='Testando') #comando teste 01
async def slash2(interaction: discord.Interaction):
    await interaction.response.send_message(f"CONGRATZ", ephemeral = True) 

@tree.command(guild = discord.Object(id=id_do_servidor), name = 'vagas', description='Mostrar vagas de emprego de acordo com o que o usuário deseja')
async def slash(interaction: discord.Interaction):
    await interaction.response.send_message('Digite a vaga que deseja procurar no formato: /vagas <cargo> <localidade> (Ex. /vagas desenvolvedor python junior São Paulo)')
    resposta = await interaction.wait_for_message()
    cargo, localidade = resposta.text[7:].split(' ', 1) #separando o cargo e a localidade
    #buscando nos sites
    await interaction.response.send_message(f'Procurando {cargo} em {localidade}...')
    #Filtrando os resultados e criando os links
    links = {'NerdIn': 'https://nerdin.com.br/vagas/'+cargo+'/'+localidade,
            'Linkedin': 'https://www.linkedin.com/jobs/search/?geoId=101940982&keywords='+cargo+'&location='+localidade
            }
    #Enviando resposta
    await interaction.response.send_message(f'Você pode procurar as vagas nesses sites: \n{links["NerdIn"]} \n{links["Linkedin"]}')

aclient.run('SEU TOKEN')
