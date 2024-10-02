import sqlite3
import pandas as pd

def main():
    # Establish connection to the database
    conn = sqlite3.connect('db/your_database.db')  # Update with your database path
    
    # Define your SQL query
    sql = """
   SELECT
    c.customer_name AS Customer,
    printf('$%.2f', (s.price_per_month * s.subscription_length)) AS Amount_Due
FROM
    orders o
JOIN
    customers c ON o.customer_id = c.customer_id
JOIN
    subscriptions s ON o.subscription_id = s.subscription_id
WHERE
    o.order_status = 'unpaid' AND
    s.description LIKE '%Fashion Magazine%'
GROUP BY
    c.customer_id;
    """

    df = None  # Initialize df to None

    # Execute the SQL query
    try:
        df = pd.read_sql(sql, conn)
        print("Query executed successfully.")
        if not df.empty:
            print("Data retrieved:")
            print(df)
        else:
            print("No data found.")
    except Exception as e:
        print(f"An error occurred: {e}")

    # Check if df is not None before trying to save to CSV
    if df is not None:
        df.to_csv('data/fashion_magazines.csv', index=False)
        print("Data saved to 'data/fashion_magazines.csv'.")
    else:
        print("No data to save.")

    # Close the connection
    conn.close()

if __name__ == '__main__':
    main()