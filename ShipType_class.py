import Ship_Getdata_class
import CruiseShip_class
import DryCargoShip_class
import LiquidCargoShip_class

class ShipType:
    def ship_type():

        input_getdata_obj = Ship_Getdata_class.Ship_Getdata
        
        type = int(input('1-Cruise Ship; 2-Dry Cargo; 3-Liquid Cargo Ship'))

        if type == 1: # Cruise Ship
            print(f'Your selection {type} - Cruise Ship')

            #Get input 
            cruise_ship_data = input_getdata_obj.cruise_ship()

            #Insert data into Ship Database
            cruise_ship_obj = CruiseShip_class.CruiseShip(cruise_ship_data[0],cruise_ship_data[1],cruise_ship_data[2],cruise_ship_data[3],cruise_ship_data[4],cruise_ship_data[5],cruise_ship_data[6],cruise_ship_data[7],cruise_ship_data[8],cruise_ship_data[9])
            cruise_ship_obj.insert_cruise_ship()

            #Insert data into Revenue Database
            cruise_ship_obj.revenue()

            return (f'{cruise_ship_data[0]} data entered successfully')          

        elif type ==2: # Dry Cargo
            print(f'Your selection {type} - Dry Cargo')

            #Get input 
            dry_cargo_ship_data = input_getdata_obj.dry_cargo()

            #Insert data into Database
            dry_cargo_ship_obj = DryCargoShip_class.DryCargoShip(dry_cargo_ship_data[0],dry_cargo_ship_data[1],dry_cargo_ship_data[2],dry_cargo_ship_data[3],dry_cargo_ship_data[4],dry_cargo_ship_data[5],dry_cargo_ship_data[6],dry_cargo_ship_data[7],dry_cargo_ship_data[8])
            dry_cargo_ship_obj.insert_dry_cargo_ship()

            #Insert data into Revenue Database
            dry_cargo_ship_obj.revenue()  

            return (f'{dry_cargo_ship_data[0]} data entered successfully')   
        else:
            print(f'Your selection {type} - Liquid Cargo Ship')

            #Get input 
            liquid_cargo_ship_data = input_getdata_obj.liquid_cargo()

            #Insert data into Database
            liquid_cargo_ship_obj = LiquidCargoShip_class.LiquidCargoShip(liquid_cargo_ship_data[0],liquid_cargo_ship_data[1],liquid_cargo_ship_data[2],liquid_cargo_ship_data[3],liquid_cargo_ship_data[4],liquid_cargo_ship_data[5],liquid_cargo_ship_data[6],liquid_cargo_ship_data[7],liquid_cargo_ship_data[8])
            liquid_cargo_ship_obj.insert_liquid_cargo_ship()

            #Insert data into Revenue Database
            liquid_cargo_ship_obj.revenue()  

            return (f'{liquid_cargo_ship_data[0]} data entered successfully')   