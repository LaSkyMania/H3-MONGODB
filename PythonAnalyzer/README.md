# Lancement d'un Docker Elasticsearch

```sh
docker run --name mon-elasticsearch -d -p 9200:9200 -p 9300:9300 -e "discovery.type=single-node" docker.elastic.co/elasticsearch/elasticsearch:7.15.0
```

## 🔍 Vérifier les plugins installés
curl -X GET "http://localhost:9200/_cat/plugins?v"

## 🏗️ Création d'un index avec analyseur personnalisé

```sh
curl -X PUT "http://localhost:9200/french" -H "Content-Type: application/json" -d '{
  "settings": {
    "analysis": {
      "filter": {
        "french_elision": {
          "type": "elision",
          "articles_case": true,
          "articles": ["l", "m", "t", "qu", "n", "s", "j", "d", "c", "jusqu", "quoiqu", "lorsqu", "puisqu"]
        },
        "french_synonym": {
          "type": "synonym",
          "ignore_case": true,
          "expand": true,
          "synonyms": [
            "réviser, étudier, bosser",
            "mayo, mayonnaise",
            "grille, toaste"
          ]
        },
        "french_stemmer": {
          "type": "stemmer",
          "language": "light_french"
        }
      },
      "analyzer": {
        "french_heavy": {
          "tokenizer": "icu_tokenizer",
          "filter": [
            "french_elision",
            "icu_folding",
            "french_synonym",
            "french_stemmer"
          ]
        },
        "french_light": {
          "tokenizer": "icu_tokenizer",
          "filter": [
            "french_elision",
            "icu_folding"
          ]
        }
      }
    }
  }
}'
```

## 📝 Création du fichier analyzer.py

J'ai créer un petit script Python

### ▶️ Exécution du fichier

python analyzer.py

## 📝 Création du fichier analyzer2.py

J'ai créer un petit script Python

### ▶️ Exécution du fichier

python analyzer2.py