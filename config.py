# Importe un module pour fixer l'ordre des dictionnaires
from collections import OrderedDict

# Token du bot
TOKEN = "MTA4OTk4MTkwOTQyNzMwNjUzNg.GDFi0D.yXsvTy5fkF_Z--OfGs6Sh2JY7cS92edhHb9Pyk"

# Prefix du bot
PREFIX = "!"

# Couleurs
BLUE = '\033[1;34m'
YELLOW = '\033[1;33m'
RESET = '\033[0;0m'

# Messages
INFO = f"{BLUE}[INFO]{RESET}"

###################
# Tableaux de Gif #
###################

# Tableau contenant les liens des gifs de super
GIF_SUPER = [
    "https://tenor.com/view/franky-one-piece-franky-super-super-water7-gif-24670817",
    "https://tenor.com/view/franky-super-gif-7298920",
    "https://tenor.com/view/mine-funny-gif-23593802",
    "https://tenor.com/view/franky-super-one-piece-anime-funny-gif-17807980",
    "https://tenor.com/view/one-piece-luffy-monkey-d-luffy-franky-franky-super-gif-24670944",
    "https://tenor.com/view/franky-super-gif-25665747",
    "https://tenor.com/view/franky-suuuuper-gif-18135924",
    "https://giphy.com/gifs/one-piece-op-opgraphics-13znec2FaeHTna"
]

# Tableau contenant les liens des gifs de feur
GIF_FEUR = [
    "https://tenor.com/view/feur-theobabac-quoi-gif-24294658",
    "https://tenor.com/view/feur-meme-gif-24407942",
    "https://tenor.com/view/feur-th%C3%A9obabac-not-funny-gif-22130648",
    "https://tenor.com/view/feur-theobabac-gif-25381023"
]

# Tableau contenant les liens des gifs de dance
GIF_DANCE = [
    "https://media.tenor.com/aoCjwQpwfJUAAAAC/dance-franky.gif",
    "https://media.tenor.com/3pOBMvjlxwsAAAAC/super-franky.gif",
    "https://media.tenor.com/tml6AsTrPa8AAAAd/usopp-franky.gif"
]

# Tableau contenant les liens des gifs de punch
GIF_PUNCH = [
    "https://media.tenor.com/DBwUdL4XkPEAAAAC/franky.gif",
    "https://media.tenor.com/yJWRCs5JzlUAAAAC/franky-punch-uppercut-franky.gif",
    "https://media.tenor.com/ZQjFQjIUP5EAAAAd/franky.gif",
    "https://media.tenor.com/tqGxsaeRM7cAAAAC/one-piece-punch.gif",
    "https://media.tenor.com/DHFA3KRpOeMAAAAd/franky.gif",
    "https://media.tenor.com/VhhYZW8xun8AAAAC/fukuro-one-piece-fukuro.gif",
    "https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExNmMyMjBmNzZjY2IyNjk4MzQwZTJlNTlkMzE1MDEyYzU2OWRmYzE5MyZjdD1n/CUfY9iiyxyx56/giphy.gif",
    "https://media.tenor.com/uHWpaorGXVgAAAAC/one-piece-nero.gif"
]

# Tableau contenant les liens des gifs de defaite de Franky
GIF_DEFAITE = [
    "https://media.tenor.com/QcKXPogUPoEAAAAd/franky-franky-one-piece.gif",
    "https://media.tenor.com/2q__HPr5VY0AAAAC/one-piece-franky.gif"

]

# Tableau contenant les liens des gifs de victoire de Franky
GIF_VICTOIRE = [
    "https://media.tenor.com/ugf48cxfO5wAAAAC/one-piece-franky.gif",
    "https://media.tenor.com/0Y_xLi0iSTwAAAAC/one-piece-franky.gif",
    "https://media.tenor.com/HQ77zC07v6QAAAAC/one-piece-franky.gif"
]

##############################
# Tableaux des mots réaction #
##############################

# Tableau contenant les mots qui font réagir le bot en lui disant "super"
MOTS_SUPER = [
    "super"
]

# Tableau contenant les mots qui font réagir le bot en lui disant "feur"
MOTS_FEUR = [
    "quoi"
]

# Tableau contenant les mots qui font réagir le bot en lui disant "obsédé"
MOTS_OBSEDE = [
    "obsédé",
    "obsédés",
    "obsede",
    "obsedes",
]

##############################
# Dictionnaire des Commandes #
##############################

# Tableau contenant les noms des commandes triées par catégories
COMMANDS = OrderedDict({

    "Informatives": [
        'help',
        'ping',
        'jeux'
    ],

    'Marrantes': [
        'laser',
        'punch',
        'dance',
        'tableflip',
        'quoi'
    ],

    'Utilitaires': [
        'random',
        'dice',
        'maths',
        'clear'
    ]

})