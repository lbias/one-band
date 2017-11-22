import sqlalchemy
import sqlalchemy.orm

from band.data.modelbase import SqlAlchemyBase
import band.data.album
import band.data.track


class DbSessionFactory:
    factory = None
    
    @staticmethod
    def global_init(db_file):
        if DbSessionFactory.factory:
            return
                
        if not db_file or not db_file.strip():
            raise Exception("You must specify a data file.")

        conn_str = 'sqlite:///' + db_file
        print("Connecting to db with conn string: {}".format(conn_str))

        engine = sqlalchemy.create_engine(conn_str, echo=True)
        SqlAlchemyBase.metadata.create_all(engine)
        DbSessionFactory.factory = sqlalchemy.orm.sessionmaker(bind=engine)
        
    @staticmethod
    def create_session():    
        return DbSessionFactory.factory()
