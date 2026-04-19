from pyspark.sql.types import (
    StructType, StructField,
    IntegerType, StringType, FloatType, DoubleType
)

# ---------- drivers.csv ----------
schema_drivers = StructType([
    StructField("driverId",      IntegerType(), True),
    StructField("driverRef",     StringType(),  True),
    StructField("number",        StringType(),  True),
    StructField("code",          StringType(),  True),
    StructField("forename",      StringType(),  True),
    StructField("surname",       StringType(),  True),
    StructField("dob",           StringType(),  True),
    StructField("nationality",   StringType(),  True),
    StructField("url",           StringType(),  True),
])

# ---------- results.csv ----------
schema_results = StructType([
    StructField("resultId",        IntegerType(), True),
    StructField("raceId",          IntegerType(), True),
    StructField("driverId",        IntegerType(), True),
    StructField("constructorId",   IntegerType(), True),
    StructField("number",          StringType(),  True),
    StructField("grid",            IntegerType(), True),
    StructField("position",        StringType(),  True),
    StructField("positionText",    StringType(),  True),
    StructField("positionOrder",   IntegerType(), True),
    StructField("points",          FloatType(),   True),
    StructField("laps",            IntegerType(), True),
    StructField("time",            StringType(),  True),
    StructField("milliseconds",    StringType(),  True),
    StructField("fastestLap",      StringType(),  True),
    StructField("rank",            StringType(),  True),
    StructField("fastestLapTime",  StringType(),  True),
    StructField("fastestLapSpeed", StringType(),  True),
    StructField("statusId",        IntegerType(), True),
])

# ---------- races.csv ----------
schema_races = StructType([
    StructField("raceId",    IntegerType(), True),
    StructField("year",      IntegerType(), True),
    StructField("round",     IntegerType(), True),
    StructField("circuitId", IntegerType(), True),
    StructField("name",      StringType(),  True),
    StructField("date",      StringType(),  True),
    StructField("time",      StringType(),  True),
    StructField("url",       StringType(),  True),
])

# ---------- constructors.csv ----------
schema_constructors = StructType([
    StructField("constructorId",  IntegerType(), True),
    StructField("constructorRef", StringType(),  True),
    StructField("name",           StringType(),  True),
    StructField("nationality",    StringType(),  True),
    StructField("url",            StringType(),  True),
])

# ---------- constructor_standings.csv ----------
schema_constructor_standings = StructType([
    StructField("constructorStandingsId", IntegerType(), True),
    StructField("raceId",                 IntegerType(), True),
    StructField("constructorId",          IntegerType(), True),
    StructField("points",                 FloatType(),   True),
    StructField("position",               IntegerType(), True),
    StructField("positionText",           StringType(),  True),
    StructField("wins",                   IntegerType(), True),
])

# ---------- driver_standings.csv ----------
schema_driver_standings = StructType([
    StructField("driverStandingsId", IntegerType(), True),
    StructField("raceId",            IntegerType(), True),
    StructField("driverId",          IntegerType(), True),
    StructField("points",            FloatType(),   True),
    StructField("position",          IntegerType(), True),
    StructField("positionText",      StringType(),  True),
    StructField("wins",              IntegerType(), True),
])

# ---------- circuits.csv ----------
schema_circuits = StructType([
    StructField("circuitId",  IntegerType(), True),
    StructField("circuitRef", StringType(),  True),
    StructField("name",       StringType(),  True),
    StructField("location",   StringType(),  True),
    StructField("country",    StringType(),  True),
    StructField("lat",        DoubleType(),  True),
    StructField("lng",        DoubleType(),  True),
    StructField("alt",        StringType(),  True),
    StructField("url",        StringType(),  True),
])