"""Part 1: Historical ingestion.

Goal: get years of past game results from the Kaggle CSVs into your database.

TODO:
  1. Load one CSV (start with the regular season compact results) with pandas
     and explore it: what columns are there? what does one row represent?
  2. Load the teams file and the tournament results file too.
  3. Do light cleanup only (column names, data types). Real transformations
     belong in Part 3.
  4. Write each file into its own "raw" table in the database.
  5. Make the script safe to run twice without duplicating data.

Questions to answer before you code:
  - How will you connect to the database without hard-coding the password?
    (hint: .env.example)
  - Where in the data does it say who was home, away, or neutral site?
"""
