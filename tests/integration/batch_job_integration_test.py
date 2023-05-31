# Databricks notebook source
# MAGIC %md ##### Install Dependencies

# COMMAND ----------

# MAGIC %pip install nutter

# COMMAND ----------

# MAGIC %md ##### Set up test fixures and run integration test.

# COMMAND ----------

from runtime.nutterfixture import NutterFixture, tag


class BatchJobTestFixture(NutterFixture):
    def before_all(self):
        sqlContext.sql("CREATE DATABASE IF NOT EXISTS guanjie_db_tmp")
        sqlContext.sql(
            "CREATE OR REPLACE TABLE guanjie_db_tmp.people10m SHALLOW CLONE guanjie_db.people10m"
        )

    def run_batch_job_test(self):
        dbutils.notebook.run(
            "../../notebooks/batch_job",
            600,
            {"sink": "guanjie_db_tmp.people10m"},
        )

    def assertion_batch_job_test(self):
        some_tbl = sqlContext.sql("SELECT COUNT(*) AS total FROM guanjie_db_tmp.people10m")
        first_row = some_tbl.first()
        print(first_row)
        assert first_row[0] > 0

    def after_all(self):
       sqlContext.sql("DROP DATABASE guanjie_db_tmp CASCADE")

result = BatchJobTestFixture().execute_tests()
print(result.to_string())
# Comment out the next line (result.exit(dbutils)) to see the test result report from within the notebook
# result.exit(dbutils)
