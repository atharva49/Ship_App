import DB_class

class PrintData:

    def print_all_ships(self,table_name):
        import pandas as pd
        self.tb_name = table_name
        
        db1 = DB_class.DB()
        print('Connection to DB successful!')

        # self.query = (f"SELECT * FROM {self.table_name}")
        # data = db1.cursor.execute(self.query)

        df = pd.read_sql_query(f'SELECT * FROM {self.tb_name}', db1.conn)
        print(f'======================================={self.tb_name}=================================================')
        print(df)
        print(f'======================================================================================================')


    def parse_tables(self):
        tables = {1:'ship_cruise',2:'ship_dry_cargo',3:'ship_liquid_cargo'}
        print_data_obj = PrintData()
        for i in tables:
            print_data_obj.print_all_ships(tables[i])

        DB_class.DB().CloseCursor()
        print('Cursor closing successful!')

        return 'Data printed successfully'