import Ship_class
import Revenue_class
import DB_class

class DryCargoShip(Ship_class.Ship):
    def __init__(self,ship_name,year_built,crew_size,trip_id,com_name,com_year,us_state,size_cat,percent_full):
        super(DryCargoShip,self).__init__(ship_name,year_built,crew_size,trip_id,com_name,com_year,us_state)
        self.size_cat = size_cat
        self.percent_full = percent_full

    def revenue(self):
        self.max_cap = 0
        self.rev_per_ton = 0
        if self.size_cat == 'handysize':
            self.max_cap = 35000
            self.rev_per_ton = 2000
        elif self.size_cat == 'capesize':
            self.max_cap = 59000
            self.rev_per_ton = 7000
        else:
            self.max_cap = 90000
            self.rev_per_ton = 8000

        self.rev = (self.percent_full/100)*self.max_cap*self.rev_per_ton
        
        rev_obj = Revenue_class.Revenue()
        rev_obj.insert_revenue(self.ship_name,self.rev,self.trip_id)

    def insert_dry_cargo_ship(self):
        db1 = DB_class.DB()
        print('Connection to DB successful! for cabin')
        self.query = ("INSERT INTO ship_dry_cargo (ship_name,built_year,crew_size,company_name,company_inc_year,company_inc_state,size_category,percentage,trip_id) VALUES (?,?,?,?,?,?,?,?,?)")
        self.values = [self.ship_name,
                        self.year_built,
                        self.crew_size,
                        self.com_name,
                        self.com_year,
                        self.us_state,
                        self.size_cat,
                        self.percent_full,
                        self.trip_id]

        db1.cursor.execute(self.query,self.values)
        print('Query Executed')
        db1.conn.commit()
        print('Query committed')