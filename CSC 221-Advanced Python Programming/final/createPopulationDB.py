# joel moore  may 2022   create_cities2_db.py
'''
this is modified program supplied by pearson publishing from the tony gaddis
text book "starting out with python"
the modifications made were:
1. added two columns to the table country and city area in square miles

'''

# ==================================================  imports

import sqlite3


#============================================  begin program code
def main():
    # Connect to the database.
    conn = sqlite3.connect('cities.db')

    # Get a database cursor.
    cur = conn.cursor()
    
    # Add the Cities table.
    add_cities_table(cur)
    
    # Add rows to the Cities table.
    add_cities(cur)
    
    # Commit the changes.
    conn.commit()

    # Display the cities.
    display_cities(cur)
    
    # Close the connection.
    conn.close()

# The add_cities_table adds the Cities table to the database.
def add_cities_table(cur):
    # If the table already exists, drop it.
    cur.execute('DROP TABLE IF EXISTS Cities')

    # Create the table.
    cur.execute('''CREATE TABLE Cities (CityID INTEGER PRIMARY KEY NOT NULL,
                                        CityName TEXT,
                                        Country TEXT,
                                        Population REAL,
                                        Area REAL)''')

# The add_cities function adds 20 rows to the Cities table.
def add_cities(cur):
    cities_pop = [(1,'Tokyo','Japan',37468000,847.14),
                  (2,'Delhi','India',28514000,16.57),
                  (3,'Shanghai','China',41354159,5761.1),
                  (4,'Sao Paulo','Brazil',22001245,3068.33),
                  (5,'Mumbai','India',18414000,1681.5),
                  (6,'Mexico City','Mexico',21804543,573.0),
                  (7,'Beijing','China',21893994,4940.8),
                  (8,'Osaka','Japan',2753862,86.95),
                  (9,'Cairo','Egypt',21323000,1191.17),
                  (10,'New York','New York',20140000,1223.59),
                  (11,'Dhaka','Bangladesh',21741000,834.432),
                  (12,'Karachi','Pakistan',16617644,1460.0),
                  (13,'Buenos Aires','Argentina',12801000,1837.0),
                  (14,'Kolkata','India',14864919,728.45),
                  (15,'Istanbul','Turkey',14163989,2063.03),
                  (16,'Chongqing','China',32054159,31816.0),
                  (17,'Lagos','Nigeria',23437435,452.23),
                  (18,'Manila','Philippines',13484482,239.22),
                  (19,'Rio de Janeiro','Brazil',12280702,1759.6),
                  (20,'Guangzhou','China',65594622,7672.0)]
    
    for row in cities_pop:
        cur.execute('''INSERT INTO Cities (CityID, CityName, Country, Population, Area)
                       VALUES (?, ?, ?, ?, ?)''', (row[0], row[1], row[2], row[3], row[4]))

# The display_cities function displays the contents of
# the Cities table.
def display_cities(cur):
    print('Contents of cities.db/Cities table:')
    cur.execute('SELECT * FROM Cities')
    results = cur.fetchall()
    for row in results:
        print(f'{row[0]:<3}{row[1]:20}{row[2]:20}{row[3]:,.0f}{row[4]:10,.1f}')

# Execute the main function.
if __name__ == '__main__':
    main()
