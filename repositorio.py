class Respositorio:

    def select(self, db_connection: any) -> None:
        conection = db_connection.conectar()
        print('conectei ao banco {}'.format(conection))
        print('fazendo um SELECT * FROM...')
        db_connection.desconctar()
    
    def insert(self, db_connection:any) -> None:
        conection = db_connection.conectar()
        print('conectei ao banco {}'.format((conection)))
        print('fazendo um INSERT VALUES...')
        db_connection.desconectar()