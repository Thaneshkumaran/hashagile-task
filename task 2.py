import mysql.connector

# Connect to MySQL database
def create_connection():
    return mysql.connector.connect(
        host="localhost",
        user="thanesh",
        password="123456",
        database="thanesh"
    )

# 1. Create a new collection (table)
def createCollection(p_collection_name):
    connection = create_connection()
    cursor = connection.cursor()
    query = f"""
        CREATE TABLE IF NOT EXISTS {p_collection_name} (
            employee_id INT PRIMARY KEY AUTO_INCREMENT,
            first_name VARCHAR(255),
            last_name VARCHAR(255),
            department VARCHAR(255),
            salary FLOAT,
            age INT
        );
    """
    cursor.execute(query)
    connection.commit()
    print(f"Table {p_collection_name} created successfully.")
    cursor.close()
    connection.close()

# 2. Index data excluding a specific column
def indexData(p_collection_name, p_exclude_column):
    connection = create_connection()
    cursor = connection.cursor()
    
    # Define columns excluding the specified column
    columns = ['first_name', 'last_name', 'department', 'salary', 'age']
    
    if p_exclude_column in columns:
        columns.remove(p_exclude_column)

    # Example data to insert (ensure it matches the columns structure)
    data = [
        ('John', 'Doe', 'HR', 60000, 30),          # Correct: 5 values
        ('Jane', 'Smith', 'Engineering', 80000, 25),
        ('Mark', 'Brown', 'Finance', 75000, 40),
        # Add more rows as necessary
    ]

    col_str = ', '.join(columns)
    placeholders = ', '.join(['%s'] * len(columns))
    
    query = f"INSERT INTO {p_collection_name} ({col_str}) VALUES ({placeholders})"
    
    for row in data:
        # Debugging: Print the current row and its length
        print(f"Processing row: {row} with length: {len(row)}")
        
        # Create row_data by excluding the specified column
        row_data = [val for i, val in enumerate(row) if i < len(columns) and columns[i] != p_exclude_column]

        # Check if the lengths match
        if len(row_data) != len(columns):
            print(f"Row {row} does not match expected columns {columns}. Skipping...")
            continue

        print(f"Inserting data: {row_data}")  # Debugging: Print the row data to be inserted
        cursor.execute(query, row_data)

    connection.commit()
    print(f"Data inserted into {p_collection_name}, excluding {p_exclude_column}.")
    cursor.close()
    connection.close()

# 3. Search by column
def searchByColumn(p_collection_name, p_column_name, p_column_value):
    connection = create_connection()
    cursor = connection.cursor()
    query = f"SELECT * FROM {p_collection_name} WHERE {p_column_name} = %s"
    cursor.execute(query, (p_column_value,))
    results = cursor.fetchall()

    if results:
        for row in results:
            print(row)
    else:
        print(f"No records found in {p_collection_name} where {p_column_name} = {p_column_value}.")

    cursor.close()
    connection.close()

# 4. Get employee count
def getEmpCount(p_collection_name):
    connection = create_connection()
    cursor = connection.cursor()
    query = f"SELECT COUNT(*) FROM {p_collection_name}"
    cursor.execute(query)
    result = cursor.fetchone()
    print(f"Total employee count: {result[0]}")
    cursor.close()
    connection.close()

# 5. Delete employee by ID
def delEmpById(p_collection_name, p_employee_id):
    connection = create_connection()
    cursor = connection.cursor()
    query = f"DELETE FROM {p_collection_name} WHERE employee_id = %s"
    cursor.execute(query, (p_employee_id,))
    connection.commit()

    print(f"Employee with ID {p_employee_id} deleted from {p_collection_name}.")
    cursor.close()
    connection.close()

# 6. Get department facet (count employees by department)
def getDepFacet(p_collection_name):
    connection = create_connection()
    cursor = connection.cursor()
    query = f"SELECT department, COUNT(*) FROM {p_collection_name} GROUP BY department"
    cursor.execute(query)
    results = cursor.fetchall()

    print("Department Facet (Employee count by department):")
    for row in results:
        print(f"Department: {row[0]}, Count: {row[1]}")
    
    cursor.close()
    connection.close()

createCollection("employees")
indexData("employees", "salary")
searchByColumn("employees", "department", "HR")
getEmpCount("employees")
delEmpById("employees", 1)
getDepFacet("employees")
def delEmpById(p_collection_name, p_employee_id):
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute(f"DELETE FROM {p_collection_name} WHERE employee_id = %s", (p_employee_id,))
    connection.commit()
    cursor.close()
    connection.close()
    print(f"Employee with ID {p_employee_id} deleted from {p_collection_name}.")
def getDepFacet(p_collection_name):
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute(f"""
        SELECT department, COUNT(*) AS count
        FROM {p_collection_name}
        GROUP BY department
    """)
    results = cursor.fetchall()
    cursor.close()
    connection.close()
    print(f"Department facets in {p_collection_name}: {results}")
    return results

# Function Executions
v_nameCollection = 'Hash_Thanesh'
v_phoneCollection = 'Hash_1234'  # Replace with your phone's last four digits

createCollection(v_nameCollection)
createCollection(v_phoneCollection)
getEmpCount(v_nameCollection)
delEmpById(v_nameCollection, '1')  # Replace with a valid employee ID to delete
getEmpCount(v_nameCollection)
searchByColumn(v_nameCollection, 'department', 'IT')
searchByColumn(v_phoneCollection, 'department', 'IT')
getDepFacet(v_nameCollection)
getDepFacet(v_phoneCollection)
