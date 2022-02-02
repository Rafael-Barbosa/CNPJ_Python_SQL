# CNPJ_Python_SQL

Desenvolvimento de uma pequena aplicação para analisar Dados Públicos CNPJ da Receita Federal e inserir em um Banco de dados 

Os arquivos csv zipados com os dados de CNPJs estão disponíveis em https://www.gov.br/receitafederal/pt-br/assuntos/orientacao-tributaria/cadastros/consultas/dados-publicos-cnpj

O layout dos dados: https://www.gov.br/receitafederal/pt-br/assuntos/orientacao-tributaria/cadastros/consultas/arquivos/novolayoutdosdadosabertosdocnpj-dez2021.pdf


## Deploy

Para fazer o deploy desse projeto rode

```bash
  git clone https://github.com/Rafael-Barbosa/CNPJ_Python_SQL
  pip install -r requirements.txt
```

Para fazer o download dos zip da base de dados basta:

```bash
  python -m main.py -d
```

Caso queira testar o processamento dos dados (parte dos dados)

```bash
  python -m main.py -t
```

### :point_right: No entanto você deverá configurar seu mysql :point_left:

Para mais detalhes: https://somosagility.com.br/instalando-e-configurando-o-servidor-mysql-no-linux-debian/ (debian)

### Teste
 - Processamento dos dados de teste (**Raw -> Standardized -> Conformed**)
 - A aplicação criará um banco de dados e as respectivas tabelas para (EMPRESAS, ESTABELECIMENTOS,SÓCIOS)
 - Por último, inserção no banco de dados (SQL)


### Contrab

O funcionamento do Contrab é simples:

```Python
from crontab import CronTab

cron = CronTab(user='username') # Coloque seu usuário
job = cron.new(command='python main.py -d') # comando para download
```
A base dados CNPJ da Receita atualiza geralmente no íncio da segunda quinzena do mês.
Portanto, todo dia 20 a aplicação será ativada (no caso abaixo às 3:00 am)
```Python
# comando no contrab 0 3 20 * * 
job.every(3).hours()
job.every(20).day()
```
Caso queira configurar direto no sistema operacional 
https://medium.com/totvsdevelopers/entendendo-o-crontab-607bc9f00ed3 (linux)


## Pontos de melhoria

- Implementar classes,funções para todos os dados da Receita Federal
- Desenvolver a parte de exportação do banco de dados
- Otimizar processo de inserção das informações no banco de dados
- Retirar funções redundantes (melhorar aplicação)

## Contribua 
1 - Fork it

2 - Cria sua feature branch (git checkout -b my-new-feature)

3 - Commit suas mudanças (git commit -am "Added some feature")

4 - Push na sua branch (git push origin my-new-feature)

5 - Crie novo Pull Request


_____

#### Stack 

 </a> <a href="https://www.python.org" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="python" width="40" height="40"/> </a> </p>

#### Database
 <a href="https://www.mysql.com/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/mysql/mysql-original-wordmark.svg" alt="mysql" width="60" height="60"/>

#### OS
</a> <a href="https://www.linux.org/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/linux/linux-original.svg" alt="linux" width="40" height="40"/> </a>



