# Databricks notebook source
# MAGIC %md ##### 1. Read Input Dataset

# COMMAND ----------

source = "dbfs:/databricks-datasets/learning-spark-v2/people/people-10m.delta"
df = spark.read.format("delta").load(source)

# COMMAND ----------

display(df)

# COMMAND ----------

# MAGIC %md ##### 2. Apply Transformations

# COMMAND ----------

from utils.transformers import convertTimestampToDate, addETLMetadata


transformed_df = df.transform(
    lambda df: convertTimestampToDate(df, "birthDate")
).transform(lambda df: addETLMetadata(df, source))

# COMMAND ----------

display(transformed_df)

# COMMAND ----------
print(transformed_df.count())

# COMMAND ----------
# MAGIC %md ##### 3. Write to Data Lake
