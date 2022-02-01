
import pandas as pd

def EMPRECSV():

    
    EMPRECSVdat = 'dados_teste/EMPRECSV.dat'
    EMPRECSV = pd.read_csv(EMPRECSVdat, sep = ";", encoding = 'latin-1', header=None)
    EMPRECSV = EMPRECSV.drop(EMPRECSV.columns[[4,6]], axis=1)
    EMPRECSV.columns = ['CNPJ', 'RAZAO_SOCIAL', 'NAT_JUT', 'QUALI', 'PORT']
    return EMPRECSV

def ESTABELECSV():


    ESTABELECSVdat = 'dados_teste/ESTABELECSV.dat'
    ESTABELECSV = pd.read_csv(ESTABELECSVdat, sep = ";", encoding = 'latin-1', header=None)
    ESTABELECSV = ESTABELECSV.drop(ESTABELECSV.columns[[7,8,9,13,14,15,16,17,21,22,23,24,25,26,27,28,29]], axis=1)
    ESTABELECSV.columns = ['CNPJ', 'ORDEM', 'DV', 'ID','FANTASIA', 'SIT_CAD', 'DAT.SIT', 'INICIO', 'CNAE_P', 'CNAE_S','CEP','UF','MUN']
    return ESTABELECSV



def SOCIOCSV():


    SOCIOCSVdat = 'dados_teste/SOCIOCSV.dat'
    SOCIOCSV = pd.read_csv(SOCIOCSVdat, sep = ";", encoding = 'latin-1', header=None)
    SOCIOCSV = SOCIOCSV.drop(SOCIOCSV.columns[[3,7]], axis=1) 
    SOCIOCSV.columns = ['CNPJ', 'ID', 'NOME_SOCIO', 'QUALI', 'DATA_ENTRE', 'PAIS', 'NOME_REPRE', 'QUALI_REP', 'FAIXA']
    return SOCIOCSV



