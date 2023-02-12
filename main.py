import psycopg2
from faker import Faker

#Conexão com db
con = psycopg2.connect(
    host='localhost',
    database='Data Test',
    user='postgres',
    password='Bap0205*'
)

cur = con.cursor()

#carrega lib faker em pt-br
fake = Faker(locale='pt-br')

base_sql = '''
    INSERT INTO followers
        (nome, email, usuario)
    VALUES
        ('{}', '{}', '{}')
    '''

#criando 1k de registros no db
for i in range(1000):
    nome = fake.name()
    email = fake.email()
    usuario = fake.user_name()
    sql = base_sql.format(nome, email, usuario)
    cur.execute(sql)

#commit no db e encerra
con.commit()
con.close()