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
