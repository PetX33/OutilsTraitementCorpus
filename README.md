# Outils de Traitement de Corpus

- Tâche : Text Classification, plus spécifiquement le multi-class text classification, dont les classes sont les langues.
- Corpus : papluca/language-identification (https://huggingface.co/datasets/papluca/language-identification). Taille : 90 000 lignes (15,3 Mo).
- Type de prédiction possible : identification de la langue d'un texte
- Modèles utilisés : il a servi au xlm-roberta-base-language-detection, deberta-v3-base-tasksource-nli, deberta-v3-large-tasksource-nli, mdeberta-v3-base-tasksource-nli, xlm-roberta-base-lora-language-detection, language_identification
- Corpus : Collection de 90 000 échantillons, composée de passage de texte et de l'étiquette de la langue correspondante. Cet ensemble de données a été créé à partir de 3 sources : Multilingual Amazon Reviews Corpus, XNLI et STSb Multi MT. Lors de l'événement communautaire The Hugging Face Course, qui a eu lieu en novembre 2021, dans le but de recueillir un ensemble de données avec suffisamment d'échantillons pour chaque langue pour former un modèle de détection de langage robuste. L'ensemble de données peut être utilisé pour entraîner un modèle d'identification linguistique. Ce corpus est une version plus fine du xlm-roberta-base qui a été formé sur cet ensemble de données et atteint actuellement une précision de 99,6 % sur l'ensemble de tests.
L'ensemble de données Language Identification contient du texte en 20 langues, qui sont : arabe (ar), bulgare (bg), allemand (de), grec moderne (el), anglais (en), espagnol (es), français (fr), hindi (hi), italien (it), japonais (ja) , néerlandais (nl), polonais (pl), portugais (pt), russe (ru), swahili (sw), thaï (th), turc (tr), ourdou (ur), vietnamien (vi), et chinois (zh).
L'ensemble de données d'identification linguistique comporte 3 divisions : train, valide et test. L'ensemble de trains contient 70 000 échantillons, tandis que la validation et le test en série 10 000 chacun. Toutes les fractions sont parfaitement équilibrées : l'ensemble des trains contient 3500 échantillons par langue, tandis que la validation et les ensembles de test en contiennent 500. Cet ensemble de données a été développé comme référence pour l'évaluation de modèles de classification de texte multi-classes (équilibrés).
Pour chaque instance, il y a une chaîne pour le texte et une chaîne pour l'étiquette (la balise de langue). Voici un exemple :
{'labels': 'fr', 'text': 'Conforme à la description, produit pratique.'}
