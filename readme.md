# Explication

[data](data) : données de l'expérimentation
- [database](data/database) : données récoltées via le plugin et sauvegardées en BDD
- [forms](data/forms) : réponses aux différentes formulaires
- [uploads](data/uploads) : uploads envoyés par les utilisateurs

[generated](generated) : fichiers générés
- [code-analysis](generated/code-analysis) : fichiers générés par l'analyse de code
- [database](generated/database) : fichiers généres à partir des informations de la BDD
- [forms](generated/forms) : fichiers générés à partir des formulaires
- [reports-no-bug](generated/reports-no-bug) : reports générés à partir des uploads grace au script Powershell [CodeAnalyser.ps1](CodeAnalyzer.ps1) (le projet contient des classes sans bugs)

[notebooks](notebooks) : notebook Jupyter
- [arrange data](notebooks/arrange_data) : notebook de préparation des données
- [analysis](notebooks/analysis) : notebook d'analyse des données