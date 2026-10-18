
import sqlite3

DB_NAME = "restaurant.db"


def setup_database():
    with sqlite3.connect(DB_NAME) as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS menu (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                category TEXT NOT NULL,
                description TEXT NOT NULL,
                price REAL NOT NULL,
                available INTEGER NOT NULL DEFAULT 1
            )
        """)

        count = conn.execute(
            "SELECT COUNT(*) FROM menu"
        ).fetchone()[0]

        if count == 0:
            items = [
                ("Margherita Pizza", "Pizza",
                 "Tomato sauce, mozzarella, fresh basil", 10.00, 1),
                ("Pepperoni Pizza", "Pizza",
                 "Tomato sauce, mozzarella, pepperoni", 12.50, 1),
                ("Chicken Burger", "Burgers",
                 "Grilled chicken, lettuce, tomato, house sauce", 9.00, 1),
                ("Caesar Salad", "Salads",
                 "Romaine lettuce, parmesan, croutons, Caesar dressing", 7.50, 1),
                ("French Fries", "Sides",
                 "Crispy golden potato fries", 3.00, 1),
                ("Chocolate Cake", "Desserts",
                 "Chocolate sponge cake with chocolate frosting", 5.00, 1),
                ("Fresh Orange Juice", "Drinks",
                 "Freshly squeezed orange juice", 3.50, 1),
            ]

            conn.executemany("""
                INSERT INTO menu
                (name, category, description, price, available)
                VALUES (?, ?, ?, ?, ?)
            """, items)


def get_menu():
    with sqlite3.connect(DB_NAME) as conn:
        conn.row_factory = sqlite3.Row
        rows = conn.execute(
            "SELECT * FROM menu WHERE available = 1"
        ).fetchall()
        return [dict(row) for row in rows]


def search_menu(keyword):
    with sqlite3.connect(DB_NAME) as conn:
        conn.row_factory = sqlite3.Row
        rows = conn.execute("""
            SELECT * FROM menu
            WHERE available = 1
              AND (name LIKE ? OR category LIKE ?
                   OR description LIKE ?)
        """, (f"%{keyword}%", f"%{keyword}%", f"%{keyword}%")).fetchall()
        return [dict(row) for row in rows]
