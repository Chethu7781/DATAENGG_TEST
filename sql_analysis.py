import mysql.connector

try:
    connection = mysql.connector.connect(host='localhost',
                                         database='mantis',
                                         user='mantisuser',
                                         password='Chethu@7781')

    # for creating the table

    mySql_Create_Table_Query = """CREATE TABLE TABLE_IND ( 
                             Customer_Name varchar(255) NOT NULL,
                             Customer_ID int(18) NOT NULL,
                             Customer_Open_Date Date NOT NULL,
                             Last_Consulted_Date Date,
                             Vaccination_Type char(5),
                             Doctor_Consulted char(255),
                             State char(5),
                             Country char(5),
                             Date_of_Birth char(8),
                             Is_Active char(1),
                             PRIMARY KEY (Customer_ID)) """

    cursor1 = connection.cursor()
    result = cursor1.execute(mySql_Create_Table_Query)   # for creating a table
    print("TABLE_IND Table created successfully ")

    # for selecting unique countries from the ETL TABLE

    sql_select_Query1 = "select DISTINCT(Country) from ETL_Table"
    cursor2 = connection.cursor()
    cursor2.execute(sql_select_Query1)
    records = cursor2.fetchall()
    unique  = set()
    for row in records:
        unique.add(row["country_column_no"])

    print(len(list(unique)))

    # for dynamically creating the empty tables
    
    for i in unique:
        query_create_table = "select * INTO TABLE+'_'{i} FROM TABLE_IND"
        cursor3 = connection.cursor()
        cursor3.execute(query_create_table)

    sql_select_Query2 = "select * from ETL_Table"
    cursor3 = connection.cursor()
    cursor3.execute(sql_select_Query2)
    result3 = cursor3.fetchall()

    for k in result3:
        for con in unique:
            if k["country_column_no"] == con:
                mySql_insert_query = """INSERT INTO TABLE_{con} (Customer_Name, Customer_ID, C_OD,
                                    C_LD, Vaccination_Type, Country, State, DOB, IS_ACTIVE) 
                                    VALUES {k} """
except mysql.connector.Error as error:
    print("error:",error)