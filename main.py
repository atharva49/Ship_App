import ShipType_class
import PrintData_class

if __name__ == '__main__':
    repeat_flag = True

    while repeat_flag:
            ip = int(input('=== Menu ===\n1.To add a ship\n2.To print the ship information for all ships in the system\n3.To print the ship name and revenue of all ships\n4.To print the ship name, company name and state of incorporation for NY,WA,TX ships\n5.To exit program\n\n'))

            print(f'Your selection {ip}')

            if ip==1: # Enter the ship 
                ship_data = ShipType_class.ShipType.ship_type()
                print(ship_data)
            elif ip==2:# Print ship data
                p1 = PrintData_class.PrintData()
                print(p1.parse_tables())
                pass
            elif ip==5:# Exit the program
                repeat_flag = False
                print('Exiting the program')