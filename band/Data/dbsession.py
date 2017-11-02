import sqlalchemy

from band.data.modelbase import SqlAlchemyBase
import band.data.album
import band.data.track


class DbSessionFactory:
    @staticmethod
    def global_init(db_file):
        if not db_file or not db_file.strip():
            raise Exception("You must specify a data file.")

        conn_str = 'sqlite:///' + db_file
        print("Connecting to db with conn string: {}".format(conn_str))

        engine = sqlalchemy.create_engine(conn_str, echo=False)
        SqlAlchemyBase.metadata.create_all(engine)
