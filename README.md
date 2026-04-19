# f1-pyspark-analysis

f1-pyspark-analysis/
│
├── 📄 README.md                        ← description du projet
├── 📄 .gitignore
├── 📄 requirements.txt                 ← dépendances Python
│
├── 📁 data/                            ← les fichiers CSV Kaggle
│   ├── circuits.csv
│   ├── constructors.csv
│   ├── constructor_results.csv
│   ├── constructor_standings.csv
│   ├── drivers.csv
│   ├── driver_standings.csv
│   ├── lap_times.csv
│   ├── pit_stops.csv
│   ├── qualifying.csv
│   ├── races.csv
│   ├── results.csv
│   ├── seasons.csv
│   └── status.csv
│
├── 📁 notebooks/
│   ├── 01_ingestion_preparation.ipynb  ← Lara
│   ├── 02_analyse_exploratoire.ipynb   ← Zeineb
│   ├── 03_transformations_score.ipynb  ← Salma
│   └── 04_optimisation_ml.ipynb        ← Ibrahima
│
├── 📁 src/                             ← fonctions réutilisables
│   ├── __init__.py
│   ├── schemas.py                      ← tous les schémas Spark
│   ├── cleaning.py                     ← fonctions de nettoyage
│   └── utils.py                        ← fonctions utilitaires
│
└── 📁 slides/
    └── presentation_f1.pdf             ← slides finales
