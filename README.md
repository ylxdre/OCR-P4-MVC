# Gestion des tournois

## Introduction

Ces instructions vous permettent de :
- récupérer le programme, 
- d'installer l'environnement nécessaire à son exécution, 
- de l'exécuter,
- de l'utiliser

### Pré-requis

```
paquets : python 3.11, python3.11-venv, git 
```

### Installation

Voici les étapes à suivre pour avoir un environnement d'exécution opérationnel :

créer l'environnement virtuel 

```
python3.11 -m venv env
source env/bin/activate
```
cloner le dépôt, aller dans le bon dossier
```
git clone https://mcstn.fr/gitea/Yann/Projet4.git
cd Projet4
```

## Exécution

exécuter la commande :
```
python3 main.py
```

## Utilisation  

Toutes les actions se font via le menu affiché.
Il y a deux menus : général et rapport.

Si vous souhaitez spécifier une liste de joueurs au format JSON, il vous faut la placer  
dans le répertoire `data`  
Sinon, vous pouvez créer des joueurs via le menu

Le répertoire, nom des fichiers joueurs et tournois sont des constantes de models.py  
Ils sont placés dans le dossier `data`

## Auteur

Yann  <yann@needsome.coffee>



## License

N/A
