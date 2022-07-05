import mysql.connector
from mysql.connector import Error

def conn_data_base(query):
    try:
        connection = mysql.connector.connect(host='mysql09-farm2.uni5.net',database='prinnx42',user='prinnx42',password='prinnx2022')
        if connection.is_connected():
            db_Info = connection.get_server_info()
            print("Conxão com o banco feita com sucesso! ", db_Info)
            cursor = connection.cursor()
            cursor.execute(query)
            record = cursor.fetchall()
    except Error as e:
        print("Erro: ", e)
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("Conexão com o MySQL fechada!")
        
    return record