import mysql.connector

# conneting mysql
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="password",
    use_pure=True,
)
cursor = mydb.cursor()

# creating database if not exists
cursor.execute("CREATE DATABASE IF NOT EXISTS caregiving")

# getting database
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="password",
  use_pure=True,
  database="caregiving"
)
mycursor = mydb.cursor()

#creting table for user
mycursor.execute("CREATE TABLE IF NOT EXISTS users (PK_user_id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), email VARCHAR(255) UNIQUE, password VARCHAR(255), mobile VARCHAR(10) UNIQUE)")

# creating tables for elder and younger if not exists
mycursor.execute("CREATE TABLE IF NOT EXISTS youngers (PK_younger_id INT AUTO_INCREMENT PRIMARY KEY,FK_user_id Integer references users(PK_user_id), rating FLOAT)")
mycursor.execute("CREATE TABLE IF NOT EXISTS elders (PK_elder_id INT AUTO_INCREMENT PRIMARY KEY,FK_user_id Integer references users(PK_user_id), FK_younger_id Integer references youngers(PK_younger_id), available BOOLEAN Default True, fund Integer, rating FLOAT)")

# Request table for younger to elder
mycursor.execute("CREATE TABLE IF NOT EXISTS request (PK_request_id INT AUTO_INCREMENT PRIMARY KEY, FK_younger_id integer references youngers(PK_younger_id), FK_elder_id integer references elders(PK_elder_id), request_status BOOLEAN Default False)")

# reviews table
mycursor.execute("CREATE TABLE IF NOT EXISTS reviews (PK_request_id INT AUTO_INCREMENT PRIMARY KEY, FK_user_id Integer references users(PK_user_id), review TEXT, rating integer, review_by VARCHAR(255))")
