# DROP Table

city_table_drop = "drop table if exists city"
employee_table_drop = "drop table if exists employee"

# create table
city_table_create = (
                    """
                        create table if not exists city
                        (
                            CityID SERIAL PRIMARY KEY
                            , CityName VARCHAR(200) UNIQUE NOT NULL
                            , State VARCHAR(100)
                            , Pincode VARCHAR(100) UNIQUE NOT NULL);
                        
                        ALTER SEQUENCE city_cityid_seq RESTART WITH 1001; 

                    """
)


employee_table_create = (
                        """
                            create table if not exists employee
                            (
                                EmployeeID SERIAL PRIMARY KEY
                                , EmployeeFirstName VARCHAR(100) NOT NULL
                                , EmployeeLastName VARCHAR(100) NOT NULL
                                , EmployeeCityID INT REFERENCES City(CityID) NOT NULL);

                            ALTER SEQUENCE employee_employeeid_seq RESTART WITH 9001;

        """

   ) 

# Query lists
drop_table_queries = [city_table_drop, employee_table_drop]
create_table_queries = [city_table_create, employee_table_create]