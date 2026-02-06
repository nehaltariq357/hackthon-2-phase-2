from src.database import create_db_and_tables

def main():
    print("Initializing database tables...")
    create_db_and_tables()
    print("Database tables created successfully!")

if __name__ == "__main__":
    main()