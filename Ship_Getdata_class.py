import InputValidation_class

class Ship_Getdata:

    def cruise_ship():
        ship_name =InputValidation_class.InputValidation.name_valid()
        built_yr =InputValidation_class.InputValidation.build_yr_valid()
        crew_size =InputValidation_class.InputValidation.crew_size_valid()
        com_name =InputValidation_class.InputValidation.company_name_valid()
        com_incop_yr =InputValidation_class.InputValidation.company_incorporation_year_valid()
        com_incop_st =InputValidation_class.InputValidation.company_incorporation_state_valid()
        max_pass =InputValidation_class.InputValidation.max_passengers_valid()
        per =InputValidation_class.InputValidation.percentage_valid()
        rate_per_cab =InputValidation_class.InputValidation.rate_per_cabin_valid()
        trip_no =InputValidation_class.InputValidation.trip_no_valid()
        return ship_name,built_yr,crew_size,com_name,com_incop_yr,com_incop_st,max_pass,per,rate_per_cab,trip_no


    def dry_cargo():
        ship_name =InputValidation_class.InputValidation.name_valid()
        built_yr =InputValidation_class.InputValidation.build_yr_valid()
        crew_size =InputValidation_class.InputValidation.crew_size_valid()
        com_name =InputValidation_class.InputValidation.company_name_valid()
        com_incop_yr =InputValidation_class.InputValidation.company_incorporation_year_valid()
        com_incop_st =InputValidation_class.InputValidation.company_incorporation_state_valid()
        size_cat =InputValidation_class.InputValidation.size_category_valid()
        per =InputValidation_class.InputValidation.percentage_valid()
        trip_no =InputValidation_class.InputValidation.trip_no_valid()
        return ship_name,built_yr,crew_size,com_name,com_incop_yr,size_cat,com_incop_st,per,trip_no

    def liquid_cargo():
        ship_name =InputValidation_class.InputValidation.name_valid()
        built_yr =InputValidation_class.InputValidation.build_yr_valid()
        crew_size =InputValidation_class.InputValidation.crew_size_valid()
        com_name =InputValidation_class.InputValidation.company_name_valid()
        com_incop_yr =InputValidation_class.InputValidation.company_incorporation_year_valid()
        com_incop_st =InputValidation_class.InputValidation.company_incorporation_state_valid()
        liquid_type =InputValidation_class.InputValidation.liquid_type_valid()
        capacity =InputValidation_class.InputValidation.percentage_valid()
        trip_no =InputValidation_class.InputValidation.trip_no_valid()
        return ship_name,built_yr,crew_size,com_name,com_incop_yr,liquid_type,com_incop_st,capacity,trip_no