# Databricks notebook source
print ("robinsonn loves yookyung a lot")

# COMMAND ----------

# MAGIC %sql
# MAGIC select ("Yookyung♡︎♡︎♡︎")

# COMMAND ----------

# MAGIC %md
# MAGIC # Yookyung 
# MAGIC ## Yookyung
# MAGIC
# MAGIC
# MAGIC
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC **# Title 1**
# MAGIC ## Title 2
# MAGIC

# COMMAND ----------

# MAGIC %run ./Includes/Setup
# MAGIC

# COMMAND ----------

print(full_name)

# COMMAND ----------

# MAGIC %fs ls '/databricks-datasets'

# COMMAND ----------

# MAGIC %fs ls

# COMMAND ----------

dbutils.help()

# COMMAND ----------

dbutils.fs.help()

# COMMAND ----------

files = dbutils.fs.ls('/databricks-datasets/')
print(files)

# COMMAND ----------

display(files)

# COMMAND ----------

# MAGIC %fs ls

# COMMAND ----------

# MAGIC %fs ls '/databricks-results/'

# COMMAND ----------

dbutils.fs.ls('/databricks-datasets/')

# COMMAND ----------

# MAGIC %fs ls '/databricks-datasets/'
