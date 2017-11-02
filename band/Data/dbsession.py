import sqlalchemy

from band.data.modelbase import SqlAlchemyBase


class DbSessionFactory:
    @staticmethod
    def global_init(db_file):
        if not db_file or not db_file.strip():
            raise Exception("You must specify a data file.")

        conn_str = 'sqlite:///' + db_file

        engine = sqlalchemy.create_engine(conn_str, echo=False)
