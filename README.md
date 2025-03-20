# Umano vs AI: alcune considerazioni sulla semplificazione manuale e automatica del corpus ItaIst
Giuliana Fiorentino e Marco Russodivito

## Abstract
È noto che la comunicazione istituzionale e la lingua amministrativa non sono sempre accessibili a ampie fette della popolazione italiana (PIEMONTESE 2023a, 2023b). Il contributo mette a confronto l'attività di semplificazione manuale di alcuni testi amministrativi con la semplificazione automatica ottenuta utilizzando modelli di intelligenza artificiale (d'ora in poi preferiamo usare l'acronimo inglese e quindi useremo AI) basati sui Large Language  Models (d'ora in poi LLMs) allo scopo di valutare similitudini e differenze tra i due metodi di semplificazione per validare il futuro sviluppo di un applicativo di semplificazione automatica dei testi basato su modelli di AI (che sarà denominato sempl.it).

Per valutare contrastivamente la semplificazione manuale (umana) e quella automatica (AI) occorre disporre di una metrica per la misurazione della complessità / semplicità della lingua di un testo (FIORENTINO/GANFI 2024), in modo da verificare innanzitutto se le trasformazioni applicate al testo migliorano le metriche, ossia aumentano gli indici di leggibilità. In vista di addestrare un modello di AI basato sui LLMs specializzandolo nella semplificazione automatica di testi amministrativi occorre altresì disporre di un corpus di testi amministrativi di varie tipologie (VELLUTINO 2018).

La prima parte del contributo introduce il tema della semplificazione della lingua amministrativa  e in generale della comunicazione istituzionale semplice; la parte centrale presenta e discute l'impostazione dello studio sperimentale e i risultati della comparazione tra semplificazione manuale e semplificazione automatica. Nelle conclusioni ci si sofferma sulle prospettive future, tenuto conto dell'esistenza di alcune criticità relativamente all'affidabilità delle operazioni automatiche di semplificazione di testi (cfr. anche DE CESARE, 2023; TAVOSANIS 2024; FIORENTINO/TAVOSANIS in corso di stampa).

## Setup
Create a virtual environment
```sh
python3 -m venv venv
source venv/bin/activate
```

Install dependencies
```sh
pip install -r requirements.txt
```

## Replication Package Content
* `corpora`: folder that contains the `original`, `gpt4`, `reviewer1` and `reviewer2` corpora analyzed in `.csv` format.
* `corpora_with_metrics`: folder that contains the corpora analyzed with the metrics extracted in `.csv` and `.json` format.
* `rules_and_issues`: folder that contains `issues.json` and `rules.json` automatically clusterized. It also contains `issues_rev.json` and `rules_rev.json` manually clusterized.
* `human_pdf`: folder that contains a human-readable `.pdf` file for each analyzed document with metrics.
* `1_metrics_extractor.ipynb`: notebook to extract metrics from each corpus. It employs [italian-ats-evaluator](https://github.com/RedHitMark/italian-ats-evaluator).
* `2_metrics_overview.ipynb`: jupyter notebook used to summarize the metrics.
* `3_metrics_visuals.ipynb`: jupyter notebook used to draw some visuals about metrics.
* `4_issues_rules_taxonomy.ipynb`: jupyter notebook used to perform clustering on issues and rules.
* `5_issues_rules_visualization_and_comparison.ipynb`: jupyter notebook used to draw some visuals about issues and rules.
* `automatic_simplification.py`: script used to automatically simplify the `original` corpus with OpenAI `gpt4` model.
* `create_human_pdfs.py`: script used to create human-readable `.pdf`.

## Acknowledgements
This contribution is a result of the research conducted within the framework of the PRIN 2020 (Progetti di Rilevante Interesse Nazionale) "VerbACxSS: on analytic verbs, complexity, synthetic verbs, and simplification. For accessibility" (Prot. 2020BJKB9M), funded by the Italian Ministero dell'Università e della Ricerca.
