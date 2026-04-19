from pyspark.sql import functions as F
from pyspark.sql.types import IntegerType


def load_csv(spark, filepath, schema):
    """
    Charge un fichier CSV du dataset F1 Kaggle.
    - nullValue='\\N' : convention MySQL utilisée dans ce dataset
    - escape='"'      : gestion des guillemets dans les champs
    """
    return spark.read \
        .option("header", True) \
        .option("nullValue", "\\N") \
        .option("escape", '"') \
        .schema(schema) \
        .csv(filepath)


def count_nulls(df, name):
    """Affiche le nombre de valeurs nulles par colonne."""
    print(f"\n🔍 Valeurs nulles — {name}")
    null_counts = df.select([
        F.count(F.when(F.col(c).isNull(), c)).alias(c)
        for c in df.columns
    ])
    null_counts.show(truncate=False)


def remove_duplicates(df, name, key_cols):
    """Supprime les doublons sur les colonnes clés et affiche un rapport."""
    total    = df.count()
    distinct = df.dropDuplicates(key_cols).count()
    dupes    = total - distinct
    print(f"🔁 {name:<30} | Total: {total:>7} | Doublons sur {key_cols}: {dupes}")
    return df.dropDuplicates(key_cols)


def clean_drivers(df):
    """
    Nettoyage de la table drivers :
    - Suppression si driverId/surname/forename null
    - Conversion dob en DateType
    - Création colonne fullName
    """
    df = df.dropna(subset=["driverId", "surname", "forename"])
    df = df.withColumn("dob", F.to_date(F.col("dob"), "yyyy-MM-dd"))
    df = df.withColumn("fullName", F.concat_ws(" ", F.col("forename"), F.col("surname")))
    return df


def clean_results(df):
    """
    Nettoyage de la table results :
    - Conversion position en IntegerType
    - Création flag 'finished'
    - Conversion milliseconds en LongType
    - Suppression si clés primaires nulles
    """
    df = df.withColumn("position_int", F.col("position").cast(IntegerType()))
    df = df.withColumn("finished", F.when(F.col("position_int").isNotNull(), True).otherwise(False))
    df = df.withColumn("milliseconds", F.col("milliseconds").cast("long"))
    df = df.dropna(subset=["resultId", "raceId", "driverId"])
    return df


def clean_races(df):
    """
    Nettoyage de la table races :
    - Conversion date en DateType
    - Suppression si clés primaires nulles
    """
    df = df.dropna(subset=["raceId", "year", "name"])
    df = df.withColumn("date", F.to_date(F.col("date"), "yyyy-MM-dd"))
    return df


def clean_constructors(df):
    """Nettoyage de la table constructors."""
    return df.dropna(subset=["constructorId", "name"])


def clean_driver_standings(df):
    """Nettoyage de la table driver_standings."""
    return df.dropna(subset=["driverStandingsId", "raceId", "driverId"])


def clean_constructor_standings(df):
    """Nettoyage de la table constructor_standings."""
    return df.dropna(subset=["constructorStandingsId", "raceId", "constructorId"])