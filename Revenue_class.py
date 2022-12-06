import DB_class

class Revenue:
    def insert_revenue(self,ship_name,revenue,trip_id):
        self.ship_name = ship_name
        self.revenue = revenue
        self.trip_no = trip_id
        db_obj = DB_class.DB()
        self.query = ("INSERT INTO revenue (ship_name,revenue,trip_id) VALUES (?,?,?)")
        self.values =[self.ship_name,self.revenue,self.trip_no]
        db_obj.cursor.execute(self.query,self.values)
        print('Revenue Query Executed')
        db_obj.conn.commit()
        print('Revenue Query committed')