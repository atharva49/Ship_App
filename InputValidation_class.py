import sys
class InputValidation:


    def name_valid():
        try:
            ship_name = str(input('Enter the ships name \n'))
            return ship_name
        except:
            print("Something went wrong \n")

    def build_yr_valid():
        try:
          built_yr = int(input('Enter the year the ship was  built \n'))
          return built_yr
        except TypeError as e:
            print(f'Data Entered is not number \n please Enter Number \n TE \n {e} \n')
            InputValidation.build_yr_valid()
        except ValueError as e:
            print(f'Data Entered is not number \n please Enter Number \n VE \n{e} \n')
            InputValidation.build_yr_valid()
        except Exception as e :
            print(f"Something went wrong \n {e} \n ")
            sys.exit(0)

    def crew_size_valid():
        try:
            crew_size = int(input('Enter the crew size \n'))
            return crew_size
        except TypeError as e:
            print(f'Data Entered is not number \n please Enter Number \n TE \n {e} \n')
            InputValidation.crew_size_valid()
        except ValueError as e:
            print(f'Data Entered is not number \n please Enter Number \n VE \n{e} \n')
            InputValidation.crew_size_valid()
        except Exception as e :
            print(f"Something went wrong \n {e} \n ")
            sys.exit(0)

    def company_name_valid():
        try:
            com_name = str(input('Enter the company name \n'))
            return com_name
        except:
            print("Something went wrong \n")

    def company_incorporation_year_valid():
        try:
            com_incop_yr = int(input('Enter the year company was incorporated into \n'))
            return com_incop_yr
        except TypeError as e:
            print(f'Data Entered is not number \n please Enter Number \n TE \n {e} \n')
            InputValidation.company_incorporation_year_valid()
        except ValueError as e:
            print(f'Data Entered is not number \n please Enter Number \n VE \n{e} \n')
            InputValidation.company_incorporation_year_valid()
        except Exception as e :
            print(f"Something went wrong \n {e} \n ")
            sys.exit(0)

    def company_incorporation_state_valid():
        try:
            com_incop_st = str(input('Enter the State in which company was incorporated \n'))
            return com_incop_st
        except:
            print("Something went wrong \n")

    def max_passengers_valid():
        try:
            max_pass = int(input('Enter the number of passengers \n'))
            return max_pass
        except TypeError as e:
            print(f'Data Entered is not number \n please Enter Number \n TE \n {e} \n')
            InputValidation.max_passengers_valid()
        except ValueError as e:
            print(f'Data Entered is not number \n please Enter Number \n VE \n{e} \n')
            InputValidation.max_passengers_valid()
        except Exception as e :
            print(f"Something went wrong \n {e} \n ")
            sys.exit(0)

    def percentage_valid():
        try:
            per = int(input('Enter the percentange full \n'))
            return per
        except TypeError as e:
            print(f'Data Entered is not number \n please Enter Number \n TE \n {e} \n')
            InputValidation.percentage_valid()
        except ValueError as e:
            print(f'Data Entered is not number \n please Enter Number \n VE \n{e} \n')
            InputValidation.percentage_valid()
        except Exception as e :
            print(f"Something went wrong \n {e} \n ")
            sys.exit(0)

    def rate_per_cabin_valid():
        try:
            rate_per_cab = int(input('Enter rate per cabin \n'))
            return rate_per_cab
        except TypeError as e:
            print(f'Data Entered is not number \n please Enter Number \n TE \n {e} \n')
            InputValidation.rate_per_cabin_valid()
        except ValueError as e:
            print(f'Data Entered is not number \n please Enter Number \n VE \n{e} \n')
            InputValidation.rate_per_cabin_valid()
        except Exception as e :
            print(f"Something went wrong \n {e} \n ")
            sys.exit(0)

    def size_category_valid():
        try:
            size_cat = str(input('Enter the size Category \n')).lower()
            return size_cat
        except:
            print("Something went wrong \n")

    def liquid_type_valid():
        try:
            liquid_type = str(input('Enter the liquid type \n')).lower()
            return liquid_type
        except:
            print("Something went wrong \n")       
    
    def capacity_valid():
        try:
            capacity = int(input('Enter the capacity in percentage\n'))
            return capacity
        except TypeError as e:
            print(f'Data Entered is not number \n please Enter Number \n TE \n {e} \n')
            InputValidation.capacity_valid()
        except ValueError as e:
            print(f'Data Entered is not number \n please Enter Number \n VE \n{e} \n')
            InputValidation.capacity_valid()
        except Exception as e :
            print(f"Something went wrong \n {e} \n ")
            sys.exit(0)

    def trip_no_valid():
        try:
            trip_no = int(input('Enter the trip unique id \n'))
            return trip_no
        except TypeError as e:
            print(f'Data Entered is not number \n please Enter Number \n TE \n {e} \n')
            InputValidation.trip_no_valid()
        except ValueError as e:
            print(f'Data Entered is not number \n please Enter Number \n VE \n{e} \n')
            InputValidation.trip_no_valid()
        except Exception as e :
            print(f"Something went wrong \n {e} \n ")
            sys.exit(0)