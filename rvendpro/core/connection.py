import psycopg2

HOST = '172.16.2.89'
DBNAME = 'dbaimp'
PORT = 5457
USER = 'usr_aplicacao'
PASSWORD = 'aplicacao'

# Create your views here.
def get_data():
    #str_connection = "host='{HOST}' dbname='{DBNAME}' port='{PORT}' user='{USER}' password='{PASSWORD}'".format(**settings.DATABASES['default'])
    str_connection = "host='{0}' dbname='{1}' port='{2}' user='{3}' password='{4}'".format(
       HOST, DBNAME, PORT, USER, PASSWORD
    )
    conn = psycopg2.connect(str_connection)
    with conn.cursor() as cursor:
        #cursor.execute("SELECT fct_vendpro2('IMP','2018-01-01','2018-01-31")
        cursor.execute("SELECT * FROM TabVendPro limit 100")
        rows = cursor.fetchall()

    #print (rows)

    # convert to dict
    data = []
    num_fields = len(cursor.description)
    field_names = [i[0] for i in cursor.description]
    for row in rows:
        register = {field_names[num]: value for num, value in enumerate(row)}
        data.append(register)

    return data
