import psycopg2
import datetime

class SousVideDB:
    def __init__(self):
        self.DSN = "password=raspberry dbname=sousvidedb  host=localhost user=pi"

    def __enter__(self): 
        self.conn = psycopg2.connect(self.DSN)
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb): 
        self.conn.commit()
        self.conn.close()

    def get_stats(self, minutes): 
        """
        Get status on relay, temperature and setpoint for current time minus minutes
        """
        now = datetime.datetime.now()
        delta = datetime.timedelta(minutes=minutes)
        new = now - delta
        result = {}
        with self.conn.cursor() as cur:
            cur.execute('select timestamp, temperature from temperature_table where timestamp > %s;', (new,))
            result['temperature'] = cur.fetchall()
            cur.execute('select timestamp, setpoint from setpoint_table where timestamp > %s;', (new,))
            result['setpoint'] = cur.fetchall()
            cur.execute('select timestamp, relay_on from relay_table where timestamp > %s;', (new,))
            result['relay'] = cur.fetchall()


        return result

    @property
    def set_point(self):
        pass

    @set_point.setter
    def set_point(self, value: int):
        with self.conn.cursor() as cur:
            cur.execute('select * from add_setpoint(%s)', (value,))
        self.conn.commit()

    @set_point.getter
    def set_point(self):
        with self.conn.cursor() as cur:
            cur.execute('select * from get_latest_setpoints(1);')
            return cur.fetchone()

    @property
    def current_temperature(self):
        pass

    @current_temperature.setter
    def current_temperature(self,value: float):
        with self.conn.cursor() as cur:
            cur.execute('select * from add_temperature(%s)', (value,))
        self.conn.commit()

    @current_temperature.getter
    def current_temperature(self) -> (datetime.datetime, float):
        with self.conn.cursor() as cur:
            cur.execute('select * from get_latest_temps(1);')
            return cur.fetchone()

    @property
    def mode(self):
        pass

    @mode.setter
    def mode(self,value: str):
        with self.conn.cursor() as cur:
            cur.execute('select * from set_mode(%s)', (value,))
        self.conn.commit()

    @mode.getter
    def mode(self):
        with self.conn.cursor() as cur:
            cur.execute('select * from get_latest_modes(1);')
            return cur.fetchone()

    @property
    def relay_on(self):
        pass

    @relay_on.setter
    def relay_on(self,value: bool):
        with self.conn.cursor() as cur:
            cur.execute('select * from set_relay_on(%s)', (value,))
        self.conn.commit()

    @relay_on.getter
    def relay_on(self):
        with self.conn.cursor() as cur:
            cur.execute('select * from get_latest_relay_on(1);')
            return cur.fetchone()
