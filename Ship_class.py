import Company_class

class Ship(Company_class.Company):
    def __init__(self,ship_name,year_built,crew_size,com_name,com_year,us_state,trip_id):
        super(Ship,self).__init__(com_name,com_year,us_state)
        self.ship_name = ship_name
        self.year_built = year_built
        self.crew_size = crew_size
        self.trip_id = trip_id