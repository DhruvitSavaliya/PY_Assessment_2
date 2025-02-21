from database import Database

db = Database()
db.execute_query("""
    CREATE TABLE IF NOT EXISTS guests (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(100) NOT NULL,
        room_number INT NOT NULL UNIQUE,
        check_in_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        balance FLOAT NOT NULL
    )
""")
print("Table Created Successfully!")
db.close()
