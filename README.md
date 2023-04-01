# Bot Discord Franky

***

## Commandes disponibles

### /help

Affiche la liste des commandes disponibles du bot dans un embed.

### /ping

Affiche le ping du bot avec un embed temporaire.

### /jeux

Affiche des liens vers les jeux que j'ai créer avec un embed.

### /laser

Tire un Radical Beam sur l'utilisateur mentionné avec un gif dans un embed.

> Paramètres : 
>
> * `<user>` : membre discord
>   * L'utilisateur mentionné

### /punch

Donne un coup de poing à l'utilisateur mentionné avec un gif dans un embed.

> Paramètres : 
>
> * `<user>` : membre discord
>   * L'utilisateur mentionné

### /dance

Affiche un gif de danse aléatoire avec l'utilisateur mentionné dans l'embed.

> Paramètres : 
>
> * `<user>` : membre discord
>   * L'utilisateur mentionné (par défaut : Franky)

### /tableflip

Affiche un gif de Franky renversant une table.

### /quoi

Active ou désactive l'envoie d'un gif de `feur` lorsque un utilisateur écrit un message contenant `quoi`

> Paramètres : 
>
> * `<active>` : booléen 
>   * True pour activer, False pour désactiver

### /random

Génère un nombre aléatoire entre 0 et le nombre spécifié.

> Paramètres : 
>
> * `<number>` : int (nombre réel)
>   * Le nombre maximum du nombre aléatoire généré (par défaut 100)

### /dice

Lance le nombre de dé avec un nombre de faces et un bonus spécifié.

> Paramètres : 
>
> * `<face>` : int (nombre réel)
>   * Le nombre de faces du/des dé(s) lancé(s) (par défaut 6)
> * `<number>` : int (nombre réel)
>   * Le nombre de dé(s) lancé(s) (par défaut 1)
> * `<bonus>` : int (nombre réel / peux être négatif)
>   * Le bonus ajouté au résultat du/des dé(s) lancé(s) (par défaut 0)

### /maths

Calcule une expression mathématique donnée, renvoie une erreur si l'expression est invalide.

> Paramètres : 
>
> * `<expression>` : str (String, phrase)
>   * L'expression mathématique à calculer

### /clear

Supprime les messages d'un salon, le bot et l'utilisateur doivent avoir la permission de supprimer des messages.

> Paramètres : 
>
> * `<number>` : int (nombre réel)
>   * Le nombre de messages à supprimer (max 100)

***

## Autres fonctionnalités disponibles

Le bot réagit  lorsque certains mots sont écrits dans les messages par les utilisateurs, comme :

* `quoi` -> le bot enverra un gif `feur` aléatoire (peut être désactiver avec la commande `/quoi`).
* `super` -> le bot enverra un gif de Franky faisant sa célèbre pose.
* `obsédé` -> le bot demandera si on parle de lui, comme dans œuvre. 
