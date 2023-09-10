import os

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import create_database, database_exists


class Database:
    """Class for general database settings"""

    DB_PATH = "database/database-file/order-management.sqlite3"
    BASE = declarative_base()

    def __init__(self):
        self._engine = None
        self._session = None

    def _create_database(self) -> None:
        """Database creation method"""
        db_directory = os.path.join(os.getcwd(), "database", "database-file")

        if not os.path.isdir(db_directory):
            os.makedirs(db_directory)

        db_url = self._engine.url

        if not database_exists(db_url):
            create_database(db_url)

        self.BASE.metadata.create_all(self._engine)

    def _create_engine(self) -> None:
        """Engine creation method"""
        db_url = f"sqlite:///{self.DB_PATH}"
        self._engine = create_engine(
            db_url, echo=False, connect_args={"check_same_thread": False}
        )

    def _create_session(self) -> None:
        """Method to create a session"""
        session_maker = sessionmaker(bind=self._engine)
        self._session = session_maker()

    def _close_session(self) -> None:
        """Method to close a session"""
        self._session.close()

    def _create_filter(self, filter_parameters: dict) -> list:
        desired_filter = [
            column == value for column, value in filter_parameters.items()
        ]

        return desired_filter

    def setup_database_environment(self) -> None:
        """Method to set up the database environment"""
        self._create_engine()
        self._create_database()

    def insert_data_table(self, insert_data: object) -> None:
        """Method for inserting data into a table"""
        self._create_session()

        try:
            self._session.add(insert_data)
            self._session.commit()
        except Exception as error:
            self._session.rollback()
            raise error
        finally:
            self._close_session()

    def update_data_table(
        self, table: object, filter_update: dict, new_data: dict
    ) -> None:
        """Method for update data of a table"""
        self._create_session()

        try:
            desired_filter = self._create_filter(filter_update)

            self._session.query(table).filter(*desired_filter).update(new_data)
            self._session.commit()
        except Exception as error:
            self._session.rollback()
            raise error
        finally:
            self._close_session()

    def delete_data_table(self, table: object, filter_delete: dict) -> None:
        """Method for delete data of a table"""
        self._create_session()

        try:
            desired_filter = self._create_filter(filter_delete)

            self._session.query(table).filter(*desired_filter).delete()
            self._session.commit()
        except Exception as error:
            self._session.rollback()
            raise error
        finally:
            self._close_session()

    def select_value_table_parameter(
        self, column: object, filter_select: dict
    ):
        """Method to query the value of a desired parameter"""
        self._create_session()

        try:
            desired_filter = self._create_filter(filter_select)
            value = self._session.query(column).filter(*desired_filter).first()
            value_fixed = "" if value is None else value[0]
        except Exception as error:
            value_fixed = error
            raise error
        finally:
            self._close_session()

        return value_fixed

    def select_data_table(self, table: object, filter_select: dict):
        """Method to select all data from a desired query"""
        self._create_session()

        try:
            desired_filter = self._create_filter(filter_select)
            data = self._session.query(table).filter(*desired_filter).all()
            data_fixed = "" if data is None else data
        except Exception as error:
            data_fixed = error
            raise error
        finally:
            self._close_session()

        return data_fixed
