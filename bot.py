import discord                      # Importe la librairie discord.py
from discord.ext import commands
import random                       # Importe la librairie random
import config                       # Importe le fichier config.py
import sys                          # Importe la librairie sys

# Définit le préfixe des commandes et les intents
bot = commands.Bot(command_prefix=config.PREFIX, intents=discord.Intents.all())

# Variables
respond_feur = True                 # Variable permettant de savoir si le bot doit répondre à "feur" ou non

#############################################################
#               LORSQUE LE BOT SE CONNECTE                  #
#############################################################

@bot.event
async def on_ready():
    """
    Effectue des actions lorsque le bot se connecte
    """

    # Importe les commandes slash
    await bot.tree.sync()

    # Change le status du bot
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name="réparer le Sunny"))

    # Affiche des informations sur le bot dans la console
    print(
f"""------------------------------------------------------------------------------------------------------------------------
{config.INFO} | Bot connecté en tant que | {config.YELLOW}{bot.user}{config.RESET}
{config.INFO} | ID du bot                | {config.YELLOW}{bot.user.id}{config.RESET}
{config.INFO} | Ping du bot              | {config.YELLOW}{round(bot.latency * 1000)}{config.RESET}
{config.INFO} | Version de discord.py    | {config.YELLOW}{discord.__version__}{config.RESET}
{config.INFO} | Version de Python        | {config.YELLOW}{sys.version}{config.RESET}
------------------------------------------------------------------------------------------------------------------------""")

#############################################################
#               LORSQU'UN MESSAGE EST ECRIT                 #
#############################################################

@bot.event
async def on_message(message):
    """
    Effectue des actions lorsque le bot reçoit un message
    """

    # Vérifie si le message a été envoyé par le bot
    if message.author == bot.user:
        return
    
    # Création d'un tableau contenant les mots du message
    message_content = message.content.lower().split(' ')


    bot_permissions = message.channel.permissions_for(message.guild.me)

    # Vérifie si le bot a les permissions pour envoyer des messages
    if bot_permissions.send_messages:
        # Parcours le tableau des mots du message
        for word in message_content:
            if word in config.MOTS_FEUR:
                await message.reply(random.choice(config.GIF_FEUR), mention_author=False)
                return

            elif word in config.MOTS_SUPER:
                await message.reply(random.choice(config.GIF_SUPER), mention_author=False)
                return

            elif word in config.MOTS_OBSEDE:
                await message.reply("Hein ? On parle de moi ?", mention_author=False)
                return

#############################################################
#                       COMMANDES SLASH                     #
#############################################################

##########################
# Commandes Informatives #
##########################

# Commande help
@bot.tree.command(name="help", description="Affiche la liste des commandes")
async def help(interaction: discord.Interaction):
    """
    Affiche la liste des commandes disponibles du bot dans un embed
    """

    # Création d'un embed
    embed_message = discord.Embed(title="Aide", description="Liste des commandes disponibles", color=discord.Color.blue())

    # Récupère toutes les commandes slash
    commands = bot.tree._get_all_commands()
    command_dict = {command.name: command for command in commands}
    
    # Trie les commandes par catégorie
    for title, cmd in config.COMMANDS.items():
        content = ""
        for command_name in cmd:
            if command_name in command_dict:
                command = command_dict[command_name]
                content += f"**`/{command.name}`"
                # Ajoute les paramètres de la commande
                for param in command._params.keys():
                    if param != None:
                        content += f" _`<{param}>`_"
                content += f"** : {command.description}\n"
        if content:
            embed_message.add_field(name=title, value=content, inline=False)

    embed_message.set_thumbnail(url=bot.user.avatar)

    await interaction.response.send_message(embed=embed_message)

# Commande ping
@bot.tree.command(name='ping', description='Donne le ping du bot')
async def ping(interaction: discord.Interaction):
    """
    Affiche le ping du bot avec un embed temporaire
    """

    embed_message = discord.Embed(title="", description=f"Le ping du bot est de **{round(bot.latency * 1000)}** ms", color=discord.Color.green())
    await interaction.response.send_message(embed=embed_message, ephemeral=True)

# Commande jeux
@bot.tree.command(name='jeux', description='Donne des liens vers des jeux incroyables')
async def jeux(interaction: discord.Interaction):
    """
    Affiche des liens vers les jeux que j'ai créer avec un embed
    """

    embed_message = discord.Embed(title="Jeux", description="Liste des meilleurs jeux sur Terre", color=discord.Color.blue())
    embed_message.add_field(name="CubeRunner", value="[CubeRunner](https://washi-fr.itch.io/cubrunner) est un runner 2D dans lequel vous devez éviter les obstacles et faire le meilleur score.", inline=False)
    embed_message.add_field(name="Roguelike", value="[Roguelike](https://washi-fr.itch.io/roguelike-2d) est un jeu de type rogue-like dans lequel vous devez battre le dernier boss.", inline=False)
    await interaction.response.send_message(embed=embed_message)

##################
# Commandes Funs #
##################

# Commande radical beam
@bot.tree.command(name='laser', description="Vous tirez un radical beam sur l'utilisateur mentionné")
async def radical_beam(interaction: discord.Interaction, user: discord.Member):
    """
    Tire un radical beam sur l'utilisateur mentionné avec un gif dans un embed

    Parameters
    ----------
    user : discord.Member
        L'utilisateur mentionné
    """

    # Vérifie si l'utilisateur mentionné est le même que l'utilisateur qui a lancé la commande
    user_command = interaction.guild.get_member(interaction.user.id)
    if user_command == user:
        embed_message = discord.Embed(title="", description="Attends mais, tu ne peux pas te frapper toi même !", color=discord.Color.green())
        embed_message.set_image(url="https://media.tenor.com/1sJs2Np6YvYAAAAd/one-piece-one-piece-franky.gif")
        await interaction.response.send_message(embed=embed_message, ephemeral=True)
        return
    

    embed_message = discord.Embed(title="", description=f"**{user.name}** a reçu un Radical Beam de la part de **{interaction.user.name}**", color=discord.Color.blue())
    embed_message.set_image(url="https://media.tenor.com/h5Z_swrQIicAAAAC/franky.gif")
    await interaction.response.send_message(user.mention, embed=embed_message)

# Commande punch
@bot.tree.command(name='punch', description="Vous donnez un coup de poing à l'utilisateur mentionné")
async def punch(interaction: discord.Interaction, user: discord.Member):
    """
    Donne un coup de poing à l'utilisateur mentionné avec un gif dans un embed

    Parameters
    ----------
    user : discord.Member
        L'utilisateur mentionné
    """

    # Vérifie si l'utilisateur mentionné est le même que l'utilisateur qui a lancé la commande
    user_command = interaction.guild.get_member(interaction.user.id)
    if user_command == user:
        embed_message = discord.Embed(title="", description="Attends mais, tu ne peux pas te frapper toi même !", color=discord.Color.green())
        embed_message.set_image(url="https://media.tenor.com/1sJs2Np6YvYAAAAd/one-piece-one-piece-franky.gif")
        await interaction.response.send_message(embed=embed_message, ephemeral=True)
        return
    
    embed_message = discord.Embed(title="", description=f"**{user.name}** a reçu un coup de poing de la part de **{interaction.user.name}**", color=discord.Color.blue())
    embed_message.set_image(url=random.choice(config.GIF_PUNCH))
    await interaction.response.send_message(user.mention, embed=embed_message)

# Commande dance
@bot.tree.command(name='dance', description="Vous dansez avec Franky ou avec un autre utilisateur")
async def dance(interaction: discord.Interaction, user: discord.Member = None):
    """
    Affiche un gif de danse aléatoire avec l'utilisateur mentionné dans l'embed

    Parameters
    ----------
    user : discord.Member
        L'utilisateur mentionné (par défaut : Franky)
    """

    if user == interaction.user or user == None or user == bot.user:
        user = bot.user

    embed_message = discord.Embed(title="", description=f"**{interaction.user.name}** danse avec **{user.name}**", color=discord.Color.blue())
    embed_message.set_image(url=random.choice(config.GIF_DANCE))

    await interaction.response.send_message(user.mention, embed=embed_message)

# Commande tableflip
@bot.tree.command(name='tableflip', description="Franky renverse une table")
async def tableflip(interaction: discord.Interaction):
    """
    Affiche un gif de Franky renversant une table
    """

    await interaction.response.send_message("https://tenor.com/view/franky-gif-26081422")

# Commande d'activation de la réponse à quoi
@bot.tree.command(name='quoi', description="Active ou désactive la réponse 'feur' à 'quoi'")
async def activate_feur(interaction: discord.Interaction, active: bool):
    """
    Active ou désactive l'envoie d'un gif de feur lorsque un utilisateur écrit un message contenant 'quoi'

    Parameters
    ----------
    active : bool
        True pour activer, False pour désactiver
    """

    respond_str = "activé" if active else "désactivé"
    global respond_feur

    # Vérifie si la valeur de active est déjà celle de respond_feur
    if active == respond_feur:
        embed_message = discord.Embed(title="", description=f"Répondre à quoi est déjà **{respond_str}**", color=discord.Color.green())
        await interaction.response.send_message(embed=embed_message, ephemeral=True)
        return
    
    respond_feur = active
    embed_message = discord.Embed(title="", description=f"Répondre à quoi **{respond_str}**", color=discord.Color.green())
    await interaction.response.send_message(embed=embed_message, ephemeral=True)

#########################
# Commandes Utilitaires #
#########################

# Commande random
@bot.tree.command(name='random', description='Génère un nombre aléatoire entre 0 et le nombre spécifié')
async def random_number(interaction: discord.Interaction, number: int = 100):
    """
    Génère un nombre aléatoire entre 0 et le nombre spécifié

    Parameters
    ----------
    number : int
        Le nombre maximum du nombre aléatoire généré (par défaut 100)
    """

    await interaction.response.send_message(random.randint(0, number))

# Commande jet de dé
@bot.tree.command(name='dice', description='Lance le nombre de dé avec un nombre de faces et un bonus spécifié')
async def dice(interaction: discord.Interaction, faces: int = 6, number: int = 1, bonus: int = 0):
    """
    Lance le nombre de dé avec un nombre de faces et un bonus spécifié

    Parameters
    ----------
    faces : int
        Le nombre de faces du/des dé(s) lancé(s) (par défaut 6)
    number : int
        Le nombre de dé(s) lancé(s) (par défaut 1)
    bonus : int
        Le bonus ajouté au résultat du/des dé(s) lancé(s) (par défaut 0)
    """

    embed_message = discord.Embed(title="Jet de dé", description=f"**{number}** dé(s) de **{faces}** face(s) lancé(s) avec un bonus de **{bonus}**", color=discord.Color.blue())
    total = 0
    res = "/ "
    for i in range(number):
        num = random.randint(1, faces)
        res += f"**{num}** ({bonus})/ "
        total += num + bonus
    embed_message.add_field(name="", value=f"{res}", inline=False)
    embed_message.add_field(name="Total", value=f"> Le total est : **`{total}`**", inline=False)
    await interaction.response.send_message(embed=embed_message)

# Commande calculate
@bot.tree.command(name='maths', description='Calcule une expression mathématique donnée')
async def maths(interaction: discord.Interaction, expression: str):
    """
    Calcule une expression mathématique donnée, renvoie une erreur si l'expression est invalide

    Parameters
    ----------
    expression : str
        L'expression mathématique à calculer
    """

    try:
        exp = expression
        res = eval(f'{expression}')
        embed_message = discord.Embed(title="Calculatrice", description=f"L'opération : `{exp}` = `{res}`", color=discord.Color.blue())
        await interaction.response.send_message(embed=embed_message)
    except:
        embed_message = discord.Embed(title="Calculatrice", description=f"L'opération : `{exp}` est invalide", color=discord.Color.red())
        await interaction.response.send_message(embed=embed_message)

# Commande clear
@bot.tree.command(name='clear', description="Supprime les messages d'un salon")
async def clear_message(interaction: discord.Interaction, number: int):
    """
    Supprime les messages d'un salon, le bot et l'utilisateur doivent avoir la permission de supprimer des messages
    
    Parameters
    ----------
    number : int
        Le nombre de messages à supprimer (max 100)
    """

    if number > 100:
        await interaction.response.send_message("Vous ne pouvez pas supprimer plus de 100 messages à la fois.")
        return

    member = interaction.guild.get_member(interaction.user.id)
    author_permissions = interaction.channel.permissions_for(member)
    bot_permissions = interaction.channel.permissions_for(interaction.guild.me)

    # Empêche d'avoir une erreur
    await interaction.response.defer(ephemeral=True)

    # Vérifie les permissions de l'utilisateur
    if not author_permissions.manage_messages:
        embed_message = discord.Embed(title="", description=f"Vous n'êtes pas autorisé à supprimer des messages dans ce salon.", color=discord.Color.green())
        embed_message.set_image(url="https://media.tenor.com/QcKXPogUPoEAAAAd/franky-franky-one-piece.gif")
        await interaction.followup.send(embed=embed_message)
    # Vérifie les permissions du bot
    elif not bot_permissions.manage_messages:
        embed_message = discord.Embed(title="", description=f"Je n'ai pas les autorisations nécessaires pour supprimer des messages dans ce salon.", color=discord.Color.green())
        embed_message.set_image(url="https://media.tenor.com/QcKXPogUPoEAAAAd/franky-franky-one-piece.gif")
        await interaction.followup.send(embed=embed_message)
    else:
        await interaction.channel.purge(limit=number)
        embed_message = discord.Embed(title="", description=f"**{number}** message(s) supprimé(s)", color=discord.Color.green())
        await interaction.followup.send(embed=embed_message)

#############################################################
#                   MISE EN LIGNE DU BOT                    #
#############################################################

# Lance le bot en utilisant le token généré précédemment
bot.run(config.TOKEN)