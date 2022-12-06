import Ship_class
import Revenue_class
import DB_class

class LiquidCargoShip(Ship_class.Ship):
    def __init__(self,ship_name,year_built,crew_size,trip_id,com_name,com_year,us_state,liquid_type,capacity):
        super(LiquidCargoShip,self).__init__(ship_name,year_built,crew_size,trip_id,com_name,com_year,us_state)
        self.liquid_type = liquid_type
        self.capacity = capacity

    def revenue(self):
        self.rev_per_K_lit= 0
        if self.liquid_type == 'vege':
            self.rev_per_K_lit = 2000
        elif self.liquid_type == 'crude':
            self.rev_per_K_lit = 7000
        else:
            self.rev_per_K_lit = 8000
        self.rev = self.capacity*self.rev_per_K_lit

        rev_obj = Revenue_class.Revenue()
        rev_obj.insert_revenue(self.ship_name,self.rev,self.trip_id)

    def insert_liquid_cargo_ship(self):
        db1 = DB_class.DB()
        print('Connection to DB successful! for cabin')
        self.query = ("INSERT INTO ship_liquid_cargo (ship_name,built_year,crew_size,company_name,company_inc_year,company_inc_state,liquid_type,capacity,trip_id) VALUES (?,?,?,?,?,?,?,?,?)")
        self.values = [self.ship_name,
                        self.year_built,
                        self.crew_size,
                        self.com_name,
                        self.com_year,
                        self.us_state,
                        self.liquid_type,
                        self.capacity,
                        self.trip_id]

        db1.cursor.execute(self.query,self.values)
        print('Query Executed')
        db1.conn.commit()
        print('Query committed')