

def Download ():

    import requests
    import wget
    from bs4 import BeautifulSoup
    from urllib.request import urlopen

    newfile = open('zipfiles.txt','w')

    page =requests.get('https://www.gov.br/receitafederal/pt-br/assuntos/orientacao-tributaria/cadastros/consultas/dados-publicos-cnpj')

    soup = BeautifulSoup(page.content)

    for anchor in soup.findAll('a', href=True):
        links = anchor['href']
        if links.endswith('EMPRECSV.zip'):
            newfile.write(links + '\n')
        if links.endswith('ESTABELE.zip'):
            newfile.write(links + '\n')
        if links.endswith('SOCIOCSV.zip'):
            newfile.write(links + '\n')
    newfile.close()

    with open('zipfiles.txt', 'r') as links:
        for link in links:
            if link:
                print(link + ' Download iniciado...')
                wget.download(link[:-1],  './data_files/%s'%(link[link.index('K'):-1]))



