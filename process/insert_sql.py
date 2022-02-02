
from . import prodata

class SQL():

    
    def __init__(self, user, password,host,database,table_emprecsv,table_estabelecsv,table_sociocsv):
        self.user = user
        self.password = password
        self.host = host
        self.database = database
        self.table_emprecsv = table_emprecsv
        self.table_estabelecsv = table_estabelecsv
        self.table_sociocsv = table_sociocsv


    def insert(myc):
        import mysql.connector
        global cnx,mycursor
        cnx = mysql.connector.connect(user=myc.user, password=myc.password, host=myc.host)
        mycursor = cnx.cursor()
        mycursor.execute("CREATE DATABASE %s" %(myc.database))
        mycursor.execute("USE %s" %(myc.database))
        
        mycursor = cnx.cursor(buffered=True)
        
        print("Conectado ao Banco de Dados ")

    
    def insert_emprecsv(tb): 
        P = prodata.Process()
        dat=P.EMPRECSV()
        mycursor.execute("CREATE TABLE %s (CNPJ VARCHAR(255), RAZAO_SOCIAL VARCHAR(255), NAT_JUT VARCHAR(255), QUALI VARCHAR(255), PORT VARCHAR(255) )" %(tb.table_emprecsv))
        for index, row in dat.iterrows():
            mycursor.executemany("INSERT INTO Empre (CNPJ,RAZAO_SOCIAL,NAT_JUT,QUALI, PORT) values(%s,%s,%s,%s,%s)", [(row.CNPJ, row.RAZAO_SOCIAL, row.NAT_JUT, row.QUALI, row.PORT)])
        print("Inserido no Banco de Dados Emprecsv")


    def insert_estabele(tb): 
        P = prodata.Process()
        dat=P.ESTABELECSV()
        mycursor.execute("CREATE TABLE %s (CNPJ VARCHAR(255), ORDEM VARCHAR(255), DV VARCHAR(255), ID VARCHAR(255), FANTASIA VARCHAR(255), SIT_CAD VARCHAR(255), DAT_SIT VARCHAR(255), INICIO VARCHAR(255), CNAE_P VARCHAR(255), CNAE_S VARCHAR(255), CEP VARCHAR(255), UF VARCHAR(255), MUN VARCHAR(255) )" %(tb.table_estabelecsv))
        for index, row in dat.iterrows():
            mycursor.executemany("INSERT INTO Estabele (CNPJ,ORDEM,DV,ID,FANTASIA,SIT_CAD,DAT_SIT,INICIO,CNAE_P,CEP,UF,MUN) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", [(row.CNPJ, row.ORDEM, row.DV, row.ID, row.FANTASIA, row.SIT_CAD, row.DAT_SIT, row.INICIO, row.CNAE_P,row.CEP,row.UF,row.MUN)])
        print("Inserido no Banco de Dados Estabelecsv")


    def insert_socio(tb): 
        P = prodata.Process()
        dat=P.SOCIOCSV()
        
        mycursor.execute("CREATE TABLE %s (CNPJ VARCHAR(255), ID VARCHAR(255), NOME_SOCIO VARCHAR(255), QUALI VARCHAR(255), DATA_ENTRE VARCHAR(255), PAIS VARCHAR(255), NOME_REPRE VARCHAR(255), QUALI_REP VARCHAR(255), FAIXA VARCHAR(255))" %(tb.table_sociocsv))
        for index, row in dat.iterrows():
            mycursor.executemany("INSERT INTO Socio  (CNPJ,ID,NOME_SOCIO,QUALI,DATA_ENTRE,PAIS,NOME_REPRE,QUALI_REP,FAIXA) values(%s,%s,%s,%s,%s,%s,%s,%s,%s)", [(row.CNPJ, row.ID, row.NOME_SOCIO, row.QUALI, row.DATA_ENTRE, row.PAIS, row.NOME_REPRE, row.QUALI_REP, row.FAIXA)])
        print("Inserido no Banco de Dados Sociocsv")


