from pyspark.sql import SparkSession
from pyspark.sql.functions import col

spark = SparkSession.builder.appName("AWSGlueETLPoC").getOrCreate()

# Read CSV from S3
df = spark.read.option("header", "true").csv("s3://example-bucket/raw/")

# Deduplication
dedup_df = df.dropDuplicates(["business_key", "updated_ts"])

# Incremental logic (example timestamp)
last_processed_ts = "2024-10-01 00:00:00"

incremental_df = dedup_df.filter(col("updated_ts") > last_processed_ts)

# Write to PostgreSQL
incremental_df.write \
    .format("jdbc") \
    .option("url", "jdbc:postgresql://hostname:5432/dbname") \
    .option("dbtable", "inbound_table") \
    .option("user", "username") \
    .option("password", "password") \
    .mode("append") \
    .save()
