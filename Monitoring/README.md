# 🚀 Mon Guide sur le Monitoring

## 📌 Introduction

Je vous présente ici mon travail sur le Monitoring, une pratique essentielle pour surveiller et analyser les performances des applications. J’ai exploré des outils tels que Elasticsearch, Kibana, Filebeat, Logstash pour collecter, stocker et visualiser les données. 📊

## 🐳 Installation ## 🐳 Installation de Filebeat, Logstash et Elasticsearch

J'ai choisi d'installer Filebeat, Logstash et Elasticsearch en utilisant Docker, ce qui est une méthode rapide et efficace. Voici comment j'ai procédé :

1. J'ai vérifié que Docker était bien installé sur mon système.
2. Ensuite, j'ai récupéré les images Docker de Filebeat, Logstash et Elasticsearch depuis Docker Hub avec les commandes :
   ```sh
   docker pull docker.elastic.co/elasticsearch/elasticsearch:7.15.0
   docker pull docker.elastic.co/logstash/logstash:7.15.0
   docker pull docker.elastic.co/beats/filebeat:7.15.0
   ```
3. Pour lancer un conteneur Elasticsearch, j’ai utilisé :
   ```sh
    docker run --name mon-elasticsearch -d -p 9200:9200 -p 9300:9300 -e "discovery.type=single-node" docker.elastic.co/elasticsearch/elasticsearch:7.15.0
    ```
4. Pour lancer un conteneur Logstash, j’ai utilisé :
    ```sh
    docker run --name mon-logstash -d docker.elastic.co/logstash/logstash:7.15.0
    ```
5. Pour lancer un conteneur Filebeat, j’ai utilisé :
    ```sh
    docker run --name mon-filebeat -d docker.elastic.co/beats/filebeat:7.15.0
    ```
6. Pour vérifier que mes conteneurs fonctionnaient bien
    ```sh
    docker ps
    ```
7. Enfin, j’ai accédé à Elasticsearch avec le client CLI intégré :
    ```sh
    docker exec -it mon-elasticsearch bash
    ```
8. Pour accéder à Kibana, j’ai utilisé :
    ```sh
    docker run --link mon-elasticsearch:elasticsearch -p 5601:5601 docker.elastic.co/kibana/kibana:7.15.0
    ```

Bravo ! 🎉 Filebeat, Logstash et Elasticsearch étaient prêts à être utilisés !

---

### 🔹 Création des graphiques

J’ai créé plusieurs graphiques pour visualiser les données dans Kibana :

1. **Histogramme** : J’ai affiché le nombre de logs par niveau de gravité.
2. **Camembert** : J’ai affiché la répartition des logs par source.
3. **Courbe** : J’ai affiché l’évolution du nombre de logs dans le temps.

## 📌 Conclusion

J’ai réussi à installer et configurer Filebeat, Logstash et Elasticsearch pour collecter, stocker et visualiser les données. J’ai également créé des graphiques pour analyser les logs et surveiller les performances. Le Monitoring est un outil puissant pour améliorer la qualité des applications et détecter les problèmes rapidement. 🚀