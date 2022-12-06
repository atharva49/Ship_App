class DB:
    import pyodbc 
    from datetime import datetime

    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

    conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=DESKTOP-5651VBR;'
                      'Database=SHIP_APP;'
                      'Trusted_Connection=yes;')
    cursor = conn.cursor()
    print(f'Connection to DB successful! {dt_string}')
    
    def CloseCursor(self):
        self.cursor.close()
        print('Connection closed succesfully')   