import Ship_class
import Revenue_class
import DB_class

class CruiseShip(Ship_class.Ship):
    def __init__(self,ship_name,year_built,crew_size,trip_id,com_name,com_year,us_state,max_num_pass,percent_full,cabin_rate):
        super(CruiseShip,self).__init__(ship_name,year_built,crew_size,trip_id,com_name,com_year,us_state)
        self.max_num_pass = max_num_pass
        self.percent_full = percent_full
        self.cabin_rate = cabin_rate

    def revenue(self):
        rev_obj = Revenue_class.Revenue()
        self.rev = self.max_num_pass*self.cabin_rate
        rev_obj.insert_revenue(self.ship_name,self.rev,self.trip_id)
        print(f'{self.rev}')

    def insert_cruise_ship(self):
        db1 = DB_class.DB()
        print('Connection to DB successful! for cabin')
        self.query = ("INSERT INTO ship_cruise (ship_name,built_year,crew_size,company_name,company_inc_year,company_inc_state,max_passenger,per,rate_cabin,trip_id) VALUES (?,?,?,?,?,?,?,?,?,?)")
        self.values = [self.ship_name,
                        self.year_built,
                        self.crew_size,
                        self.com_name,
                        self.com_year,
                        self.us_state,
                        self.max_num_pass,
                        self.percent_full,
                        self.cabin_rate,
                        self.trip_id
                        ]

        db1.cursor.execute(self.query,self.values)
        print('Query Executed')
        db1.conn.commit()
        print('Query committed')