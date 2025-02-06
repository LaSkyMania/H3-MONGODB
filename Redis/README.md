# 🚀 Mon Guide sur Redis

## 📌 Introduction

Je vous présente ici mon travail sur Redis, une base de données en mémoire ultra-rapide que j'ai explorée en profondeur. Redis peut être utilisé comme base de données, cache ou encore comme courtier de messages. Il prend en charge plusieurs structures de données comme les chaînes de caractères, les listes, les ensembles et les ensembles triés.

J'ai découvert que Redis offre une large gamme de fonctionnalités comme les transactions, le scripting Lua, la messagerie Pub/Sub et plusieurs options de persistance. Que ce soit en mode serveur unique ou en cluster, Redis garantit des performances optimales. 🚀

---

## 🐳 Installation de Redis avec Docker

J'ai choisi d'installer Redis en utilisant Docker, ce qui est une méthode rapide et efficace. Voici comment j'ai procédé :

1. J'ai vérifié que Docker était bien installé sur mon système.
2. Ensuite, j'ai récupéré l’image Redis depuis Docker Hub avec la commande :
   ```sh
   docker pull redis
   ```
3. Pour lancer un conteneur Redis, j’ai utilisé :
   ```sh
   docker run --name mon-redis -d redis
   ```
4. Pour vérifier que mon conteneur fonctionnait bien, j’ai exécuté :
   ```sh
   docker ps
   ```
5. Enfin, j’ai accédé à Redis avec le client CLI intégré :
   ```sh
   docker exec -it mon-redis redis-cli
   ```

Bravo ! 🎉 Redis était prêt à être utilisé !

---

## 🛠️ Commandes Redis de base

J’ai expérimenté plusieurs types de structures de données et leurs commandes associées.

### 🔹 Chaînes de caractères (Strings)
- Création / Mise à jour :
  ```sh
  SET utilisateur "JeanDupont"
  SETEX session 3600 "data_session"
  ```
- Lecture :
  ```sh
  GET utilisateur
  ```
- Suppression :
  ```sh
  DEL utilisateur
  ```

### 🔹 Hashes
- Création :
  ```sh
  HSET user:1 nom "Alice"
  ```
- Lecture :
  ```sh
  HGET user:1 nom
  ```
- Suppression :
  ```sh
  HDEL user:1 email
  ```

### 🔹 Listes
- Ajout en début ou fin de liste :
  ```sh
  LPUSH fruits "pomme" "banane"
  RPUSH fruits "cerise"
  ```
- Lecture :
  ```sh
  LRANGE fruits 0 -1
  ```
- Suppression :
  ```sh
  LPOP fruits
  ```

### 🔹 Ensembles
- Ajout d’éléments :
  ```sh
  SADD couleurs "rouge" "vert"
  ```
- Lecture :
  ```sh
  SMEMBERS couleurs
  ```
- Suppression :
  ```sh
  SREM couleurs "vert"
  ```

### 🔹 Ensembles triés
- Ajout avec score :
  ```sh
  ZADD scores 10 "joueur1"
  ```
- Lecture :
  ```sh
  ZRANGE scores 0 -1
  ```
- Suppression :
  ```sh
  ZREM scores "joueur1"
  ```

---

## 🐍 Connexion de Redis avec Python

J’ai également testé Redis avec Python en utilisant la bibliothèque `redis-py`.

### 📦 Installation
```sh
pip install redis
```

### 🔌 Connexion
```python
import redis
r = redis.Redis(host='localhost', port=6379, db=0)
```

### 🔄 Manipulation des données
```python
r.set('user:1:name', 'Jean Dupont')
nom_utilisateur = r.get('user:1:name').decode('utf-8')
print(nom_utilisateur)
```

J’ai exploré d'autres fonctionnalités comme la gestion de pools de connexion, l’exécution de transactions et la messagerie Pub/Sub. Redis s’est révélé être un outil puissant et flexible ! 💪

---

## 📌 Conclusion

Grâce à cette exploration de Redis, j’ai pu comprendre comment optimiser le stockage en mémoire et améliorer la performance des applications. J’ai découvert de nombreuses commandes et appris à interagir avec Redis via Python. 🐍

Redis est un outil incontournable pour les applications nécessitant des accès rapides aux données. Je continuerai à explorer ses fonctionnalités avancées pour enrichir mes projets. 🔥