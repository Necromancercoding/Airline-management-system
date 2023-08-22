import pymysql
import MySQLdb

db=pymysql.connect(host="localhost", user="root", password="raikkonenrox123", port=3306, db="Airseatbooking")
db.open