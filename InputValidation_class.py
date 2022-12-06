class InputValidation:

    def name_valid():
        try:
            ship_name = str(input('Enter the ships name'))
            return ship_name
        except:
            print("Something went wrong")

    def build_yr_valid():
        try:
          built_yr = int(input('Enter the year the ship was  built'))
          return built_yr
        except:
            print("Something went wrong")

    def crew_size_valid():
        try:
            crew_size = int(input('Enter the crew size'))
            return crew_size
        except:
            print("Something went wrong")

    def company_name_valid():
        try:
            com_name = str(input('Enter the company name'))
            return com_name
        except:
            print("Something went wrong")

    def company_incorporation_year_valid():
        try:
            com_incop_yr = int(input('Enter the year company was incorporated into'))
            return com_incop_yr
        except:
            print("Something went wrong")

    def company_incorporation_state_valid():
        try:
            com_incop_st = int(input('Enter the year company was incorporated into'))
            return com_incop_st
        except:
            print("Something went wrong")

    def max_passengers_valid():
        try:
            max_pass = int(input('Enter the number of passengers'))
            return max_pass
        except:
            print("Something went wrong")

    def percentage_valid():
        try:
            per = int(input('Enter the percentange full'))
            return per
        except:
            print("Something went wrong")

    def rate_per_cabin_valid():
        try:
            rate_per_cab = int(input('Enter rate per cabin'))
            return rate_per_cab
        except:
            print("Something went wrong")

    def size_category_valid():
        try:
            size_cat = str(input('Enter the size Category')).lower()
            return size_cat
        except:
            print("Something went wrong")

    def liquid_type_valid():
        try:
            liquid_type = str(input('Enter the liquid type')).lower()
            return liquid_type
        except:
            print("Something went wrong")       
    
    def capacity_valid():
        try:
            capacity = int(input('Enter the capacity'))
            return capacity
        except:
            print("Something went wrong")

    def trip_no_valid():
        try:
            trip_no = int(input('Enter the trip unique id'))
            return trip_no
        except:
            print("Something went wrong") 