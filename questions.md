# Partie 1

1. Pourquoi voudrait-on diviser un gros service web en plusieurs morceaux plus petits ?
Cela permet de faire évoluer l'application plus facilement, il suffit de modifier uniquement la partie concernée.

2. Imaginez que vous travaillez sur un gros projet. Que se passe-t-il si vous devez modifier une seule fonctionnalité ? Est-ce facile ? Risqué ?
Si le service n'est pas bien découpé cela sera sûrement compliqué, on peut casser d'autres fonctionnalités pendant les modifications. Si les services sont bien découpés, cela n'aura d'impact que sur les services qui utilisent celui qui est modifié.

3. Peut-on confier un petit service à une autre équipe ou un autre développeur sans qu’il ait besoin de connaître tout le reste ?
Oui

4. Que se passe-t-il si une partie tombe en panne ? Peut-on réparer sans tout redémarrer ?
Oui si tout les services sont bien découpés. Cela dépend aussi du service. Si c'est un service critique dont tous les autres dépendent, on ne pourra pas faire grand chose.

5. Avez-vous déjà vu ou utilisé un site ou une appli qui semblait “modulaire” ?

6. Sur quels critères peut-on séparer un gros service en plusieurs petits ?
On peut se baser sur les fonctionnalités : un service réalise une seule fonctionnalité bien précise ou plusieurs fonctionnalités qui vont ensemble.

7. Faut-il découper par fonctionnalité (ex : blague, météo, cantine…) ? Par type de donnée ? Par public cible ?

8. À partir de combien de lignes de code ou de routes HTTP faut-il envisager un découpage ?
Quand on s'apperçoit que le code commencer à être ingérable, qu'on a du mal à s'y retrouver.

9. Le découpage doit-il être figé ou peut-il évoluer ?
Il évolue en même temps que l'application.

# Partie 2

1. Pourquoi ne pas appeler directement open-meteo depuis le navigateur ?
Ce n'est pas très pratique d'obtenir un gros fichier JSON dans le navigateur.
Ce n'est pas vraiment utilisable, surtout pour les utilisateurs qui ne font pas de l'informatique.

2. Quel est l’avantage de passer par un microservice intermédiaire ?
Le microservice traite les données pour nous et ne renvoie que ce qui nous intéresse vraiment.

3. Si le format de réponse de open-meteo change, que se passe-t-il ?
On devra modifier la partie de notre code qui traite les données reçues.

4. Que pourrait-on ajouter pour rendre ce service plus complet ou plus robuste ?

# Partie 3

## Questions 3

1. Pourquoi ajouter une base de données à un service météo aussi simple ? Est-ce justifié ?
Dans ce cas, c'est surtout utile si on veut soulager l'API.

2. Est-ce que chaque microservice devrait avoir sa propre base, ou peut-on les partager ?
Si la base de données contient des données communes à plusieurs services, il vaut mieux en garder une seule.

3. Que gagne-t-on (et que perd-on) en utilisant une base relationnelle plutôt qu’un fichier ou un dictionnaire Python ?
On gagne la stabilité et la gestion de la concurrence. Par contre, selon la base de données choisie, cela peut devenir assez lourd. Dans notre cas, utliser sqlite suffit clairement.

4. Que permet une base comme MySQL que ne permet pas un fichier JSON ?
Voir ci-dessus.

5. Si on voulait partager cette météo avec d’autres services, la base est-elle une bonne interface ?
Si les autres services n'ont pas besoin de modifier les données, ils n'ont pas forcément besoin d'accéder à la base de données. Il faut décider ensuite si on fait une API alternative pour ces services ou si on leur limite juste l'accès à la base de données.

6. Peut-on facilement sauvegarder/exporter les données ? Et les restaurer ?
Avec une base de données, oui.

7. Est-ce que l’ajout d’une BDD rend le service plus rapide ? Plus lent ?
Le service sera plus rapide puisqu'on n'a pas à attendre les résultats de l'API.

8. Que se passe-t-il si plusieurs clients envoient des requêtes simultanément ?
Normalement, ils n'auront pas de problèmes de lenteur puisque chaque client ne devra pas attendre que l'API leur renvoit les résultats.

9. Peut-on mettre à jour une donnée météo sans recontacter l’API externe ?
Oui, on la modifie directement dans la base de données.

10. Est-ce qu’on peut interroger la météo d’hier ou de demain avec cette architecture ?
Oui, on peut stocker la météo et y associer une date.

## Questions 6

1. Pourquoi voudrait-on éviter d’écrire directement des requêtes SQL à la main ?
Cela évite d'alourdir le code avec beaucoup de strings plus ou moins longues.

2. Que gagne-t-on en utilisant un ORM comme SQLAlchemy ?
On n'a plus besoin de s'occuper du SQL et utiliser la programmation objet pour manipuler la base de données rend le code plus compréhensible.

3. Est-ce que l’ORM vous empêche complètement d’accéder au SQL si besoin ?
Non, SQLAlchemy permet d'exécuter des requêtes SQL directement.

4. Est-ce que le code Python devient plus clair ou plus opaque avec un ORM ?
Pour des requêtes simples il devient plus clair mais il peut devenir complexe si on enchaîne les filtres et autres appels de méthodes.

5. À quel moment l’ORM peut devenir un inconvénient ? (performances, complexité, etc.)
Dans le cas où on doit faire une requête complexe. Il serait plus rapide d'écrire la requête SQL plutôt que de parcourir toute la documentation pour trouver comment on fait.

# Partie 4

## Questions 2

1. Ce service fait deux appels HTTP internes. Est-ce efficace ? Pourquoi ?

2. Que se passe-t-il si l’un des deux services répond avec une erreur ou met trop de temps ?
Cela peut ralentir et/ou bloquer la suite du programme.

3. Peut-on réutiliser ce service dans d’autres cas (email, impression, vocal) ?
Il faut juste l'adapter pour changer les services qu'il contacte.

4. Quelle est la différence entre un service “client” (ex : navigateur) et ce nouveau service ?
Ce service est client des APIs qu'il contacte.
