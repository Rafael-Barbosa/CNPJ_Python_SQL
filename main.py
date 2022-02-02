import getopt, sys

from process import insert_sql
from process import prodata
import os
from download import Down

lst = sys.argv[1:]
options = "td"
long_options = ["TESTE", "DOWNLOAD"]

try:

    arguments, values = getopt.getopt(lst, options, long_options)

    root = 'root'
    password = 'password'
    host = '127.0.0.1'
    database = 'CNPJ3'
    Empre = 'Empre'
    Estabele = 'Estabele'
    Socio = 'Socio'


    for currentArgument, currentValue in arguments:

        if currentArgument in ("-t", "--TESTE"):
         print("Processando Teste")
         
         connection = insert_sql.SQL(root, password, host, database, Empre, Estabele, Socio)
         connection.insert()
         connection.insert_emprecsv()
         connection.insert_estabele()
         connection.insert_socio()
         #os.system('mysqldump -u root -p%s %s > database.sql' %(password,database))
        elif currentArgument in ("-d", "--DOWNLOAD"):
         print("Download Dados Publicos CNPJ")
         Down.Download()

except getopt.error as err:
    print("Error")
