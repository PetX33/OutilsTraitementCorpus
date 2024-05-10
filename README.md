# Outils de Traitement de Corpus

- Tâche choisi : La classificaiton de texte, plus spécifiquement la multi-classification de texte, dont les classes sont les langues.
- Corpus : papluca/language-identification (<https://huggingface.co/datasets/papluca/language-identification>).
  - 90 000 échantillons de textes avec leurs étiquettes de langue correspondantes, répartis équitablement entre 20 langues.
  - Les échantillons proviennent du Multilingual Amazon Reviews Corpus, XNLI et STSb Multi MT.
  - Principalement conçu pour entraîner des modèles d'identification linguistique, ce modèle papluca/xlm-roberta-base-language-detection atteint une précision de 99,6% sur l'ensemble de tests. Autres modèles : xlm-roberta-base-language-detection, deberta-v3-base-tasksource-nli, deberta-v3-large-tasksource-nli, mdeberta-v3-base-tasksource-nli, xlm-roberta-base-lora-language-detection, language_identification.
  - Langues incluses : Les 20 langues présentes dans l'ensemble de données couvrent un large éventail, incluant l'arabe, le bulgare, l'allemand, le grec moderne, l'anglais, l'espagnol, le français, l'hindi, l'italien, le japonais, le néerlandais, le polonais, le portugais, le russe, le swahili, le thaï, le turc, l'urdu, le vietnamien et le chinois.
  - Structure :
    - Chaque instance est composée d'un texte et de son étiquette de langue correspondante, par exemple : {'labels': 'fr', 'text': 'Conforme à la description, produit pratique.'}.
    - L'ensemble est divisé en trois parties : entraînement (70 000 échantillons), validation et test (10 000 échantillons chacun), avec une distribution équilibrée par langue.
  - Ce corpus a été créé  lors de l'événement The Hugging Face Course en novembre 2021 pour former un modèle de détection de langue robuste. Il est issues de trois corpus multilingues spécifiques ([Multilingual Amazon Reviews Corpus](https://huggingface.co/datasets/amazon_reviews_multi), [XNLI](https://huggingface.co/datasets/xnli)et [STSb Multi MT](https://huggingface.co/datasets/stsb_multi_mt)). Aucune donnée personnelle ou sensible n'y est incluse.


# Explication des différents script

### 1. [**extract_data.ipynb**](./scripts/data/raw/extract_data.ipynb) (cours 2)
   - **Objectif** : Ce script automatise l'extraction de données textuelles multilingues depuis des pages Wikipédia aléatoires pour diverses langues. Il est conçu pour collecter et enregistrer des paragraphes dans des fichiers textuels, structurés par langue.

   - **Description du processus** :
    - **Initialisation du pilote** : Utilisation de Selenium WebDriver avec Chrome pour naviguer sur le web.
    - **Extraction des URL aléatoires** : Récupération d'URLs de pages Wikipédia aléatoires pour une liste prédéfinie de langues via des requêtes automatisées à leurs pages spéciales.
    - **Extraction de contenu** : Récupération de paragraphes et de titres d'articles à partir des URLs obtenues.
    - **Traitement des liens interlangues** : Collecte des URLs de pages similaires dans d'autres langues disponibles via les liens interlangues pour chaque article.
    - **Sauvegarde des données** : Écriture des paragraphes extraits dans des fichiers textuels, nommés et organisés par langue et titre d'article, dans un dossier spécifié.
    - **Gestion de données** : Comptabilisation du nombre de fichiers écrits pour chaque langue pour éviter les duplicatas et s'assurer de la diversité du dataset.
    - **Fermeture et nettoyage** : Fermeture du pilote du navigateur à la fin de l'exécution pour libérer les ressources.
    
   - **Utilité du script** : Ce script est essentiel pour construire un corpus textuel diversifié nécessaire pour l'entraînement et l'évaluation des modèles de classification linguistique. Il permet une collecte de données large et variée en termes de langue et de contenu, facilitant ainsi les études sur le traitement multilingue du texte.
    
### 2. [**clean_data.ipynb**](./scripts/data/clean/clean_data.ipynb) (cours 2)
   - **Objectif** : Ce script vise à nettoyer les données textuelles en supprimant les éléments indésirables tels que les numéros de lignes, les chiffres isolés, les retours à la ligne, et en normalisant les espaces. Il transforme les fichiers textuels bruts en versions nettoyées, plus adaptées aux analyses et au traitement ultérieurs.
    
   - **Description du processus** :
    - **Importation des bibliothèques** : Utilisation de modules comme `re` pour les expressions régulières, `os` pour la manipulation des fichiers, et `chardet` pour la détection de l'encodage.
    - **Définition de la fonction de nettoyage** : Création d'une fonction `clean_text` pour appliquer plusieurs règles de nettoyage au texte, y compris la suppression de références et la normalisation des espaces.
    - **Nettoyage des fichiers** : La fonction `clean_data` parcourt tous les fichiers du dossier spécifié, détecte leur encodage, lit et nettoie leur contenu, puis enregistre le texte nettoyé dans un nouveau dossier.
    - **Gestion des encodages** : Chaque fichier est ouvert en mode binaire pour détecter son encodage avec `chardet`, puis relu et écrit en utilisant cet encodage pour préserver l'intégrité des données.
    - **Écriture des fichiers nettoyés** : Les fichiers sont enregistrés avec le même nom dans un dossier de destination, assurant une organisation facile et une correspondance directe avec les fichiers d'origine.
    
   - **Utilité du script** : Ce script est crucial pour préparer les données en vue de leur utilisation dans des tâches de traitement du langage naturel, en éliminant les erreurs et incohérences qui pourraient affecter les performances des modèles. Il assure que les données entrées dans le système de traitement sont de haute qualité et uniformes, ce qui est essentiel pour obtenir des résultats fiables et reproductibles.

### 3. [**create_csv.ipynb**](./scripts/data/csv/csv.ipynb) (cours 2)
   - **Objectif** : Ce script crée un fichier CSV contenant des paires de phrases segmentées provenant de fichiers texte multilingues. Chaque ligne du CSV inclut une paire de phrases et l'étiquette de langue associée. L'objectif est de fournir un ensemble de données équilibré, prêt pour des tâches de traitement du langage naturel.
    
   - **Description du processus** :
    - **Importation des bibliothèques** : Utilisation de bibliothèques comme `os` pour la gestion des fichiers, `pandas` pour la manipulation de DataFrames, `spacy` et `stanza` pour la segmentation linguistique.
    - **Chargement des modèles de langue** : Chargement des modèles de segmentation adaptés aux langues couramment traitées, notamment le japonais, le chinois et l'arabe. Un modèle par défaut est également utilisé pour les autres langues.
    - **Définition de la fonction de segmentation** : Création de la fonction `segment_sentences` pour segmenter les textes en phrases selon la langue. Les modèles NLP spécifiques garantissent une segmentation précise.
    - **Création du CSV équilibré** : La fonction `create_csv` collecte les fichiers texte dans un dossier, segmente leur contenu en phrases, regroupe les phrases par paires et limite le nombre de paires pour chaque langue afin d'obtenir un échantillon équilibré.
    - **Manipulation et stockage des données** :
      - Les paires de phrases sont stockées dans un dictionnaire par langue.
      - Un DataFrame `df_balanced` est créé, étiquetant chaque paire par langue, puis sauvegardé dans un fichier CSV.
    
   - **Utilité du script** : Ce script facilite la création d'un ensemble de données équilibré pour les modèles de traitement du langage naturel, en regroupant les paires de phrases segmentées par langue. Le CSV ainsi créé est essentiel pour la formation et l'évaluation de modèles multilingues, et simplifie l'accès aux données textuelles multilingues dans un format structuré.

### 4. [**analyse_morpho.ipynb**](./scripts/analyse_morpho/analyse_morpho.ipynb) (cours 3)
  

### 5. [**mesures.ipynb**](./scripts/mesures/evaluation.ipynb) (cours 4)
   

### 6. [**evaluation.ipynb**](./scripts/mesures/evaluation.ipynb) (cours 5) 
   
