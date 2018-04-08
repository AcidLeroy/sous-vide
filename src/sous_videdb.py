import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT, ISOLATION_LEVEL_DEFAULT
import datetime

class SousVideDB:
    def __init__(self):
        self.DSN = "dbname=postgres  host=localhost user=postgres"

    @property
    def set_point(self):
        pass

    @set_point.setter
    def set_point(self, value: int):
        with psycopg2.connect(self.DSN) as conn:
            with conn.cursor() as cur:
                cur.execute('select * from add_setpoint(%s)', (value,))

    @set_point.getter
    def set_point(self):
        with psycopg2.connect(self.DSN) as conn:
            with conn.cursor() as cur:
                cur.execute('select * from get_latest_setpoints(1);')
                return cur.fetchone()

    @property
    def current_temperature(self):
        pass

    @current_temperature.setter
    def current_temperature(self,value: float):
        with psycopg2.connect(self.DSN) as conn:
            with conn.cursor() as cur:
                cur.execute('select * from add_temperature(%s)', (value,))

    @current_temperature.getter
    def current_temperature(self) -> (datetime.datetime, float):
        with psycopg2.connect(self.DSN) as conn:
            with conn.cursor() as cur:
                cur.execute('select * from get_latest_temps(1);')
                return cur.fetchone()

    @property
    def mode(self):
        pass

    @mode.setter
    def mode(self,value: str):
        with psycopg2.connect(self.DSN) as conn:
            with conn.cursor() as cur:
                cur.execute('select * from set_mode(%s)', (value,))

    @mode.getter
    def mode(self):
        with psycopg2.connect(self.DSN) as conn:
            with conn.cursor() as cur:
                cur.execute('select * from get_latest_modes(1);')
                return cur.fetchone()
