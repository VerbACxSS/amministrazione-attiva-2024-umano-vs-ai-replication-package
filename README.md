# Umano vs AI: alcune considerazioni sulla semplificazione manuale e automatica del corpus ItaIst
Giuliana Fiorentino e Marco Russodivito

## Abstract
Il contributo mette a fuoco contrastivamente l'attività di semplificazione manuale applicata a un sottoinsieme del corpus ItaIst e la semplificazione automatica ottenuta dal prototipo del software ATS che stiamo utilizzando e mettendo a punto come prodotto applicativo risultante dal progetto PRIN VerbAcxSS (l'applicativo è denominato SEMPL-IT).

Il campione prescelto per questa analisi rappresenta una selezione dai testi di ItaIst, corpus costituito da 208 testi amministrativi provenienti da 8 regioni italiane (Basilicata, Calabria, Campania, Lazio, Lombardia, Molise, Toscana, Veneto) e riferiti a 3 aree tematiche: rifiuti, sanità, servizi pubblici. Per ciascuna area tematica sono state considerate 2 tipologie di testi (carte dei servizi e bandi di gara per la prima area tematica; atti generali di pianificazione e accreditamenti per la seconda area tematica; carte dei servizi e razionalizzazione delle partecipazioni pubbliche per la terza area tematica).

Il contributo discute in che modo sono tenute in conto le diverse istruzioni per la semplificazione che costituiscono la lista condivisa di parametri e operazioni che si è andata costituendo nella letteratura specialistica sul tema (cfr. Fiorentino, Ganfi in corso di stampa per una ricognizione sui parametri di semplificazione condivisi dalla maggior parte della letteratura italiana).

La prima parte del contributo discute le differenze tra operazioni di semplificazione e operazioni di sintesi realizzate con il supporto dell'intelligenza artificiale. Nella seconda parte si presentano i risultati del confronto tra le operazioni automatiche e quelle realizzate manualmente. Le conclusioni si soffermano criticamente sull'affidabilità delle operazioni automatiche.

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