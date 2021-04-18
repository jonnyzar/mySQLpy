#!/usr/bin/python3.9

import mysql.connector

def main():

#access database -u root -pmutillidae

	mydb = mysql.connector.connect( \
		host='localhost',\
        user='root',\
        password='mutillidae'
        )

	print ("[+] Connected to mysql server:")
	print (mydb)

	mycursor = mydb.cursor()

	print (mycursor)

#make a request
#	mycursor.execute("CREATE DATABASE fooDB")

#	mycursor.execute("DROP DATABASE fooDB")
#	mycursor.execute("DROP DATABASE DB")

	mycursor.execute("SHOW DATABASES")
	temp = mycursor
#retrieve the results
#explore tables within all databases

	for DB in temp:
		print(DB)
				
		nextdb = mysql.connector.connect( \
			host='localhost',\
			user='root',\
			password='mutillidae',\
			database=DB[0]
			)
		print(nextdb)
		nextcursor = nextdb.cursor()
		nextcursor.execute('SHOW TABLES')
		for table in nextcursor:
			print (table)

	return 0


if __name__=="__main__":
    main()


