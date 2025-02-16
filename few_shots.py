few_shots = [
    {
        "Question": "What is the total stock quantity of all t-shirts?",
        "SQLQuery": "SELECT SUM(stock_quantity) FROM t_shirts;",
        "SQLResult": "Result of the SQL query",
        "Answer": "58"
    },
    {
        "Question": "Which brand has the highest total stock quantity?",
        "SQLQuery": "SELECT brand, SUM(stock_quantity) AS total_stock FROM t_shirts GROUP BY brand ORDER BY total_stock DESC LIMIT 1;",
        "SQLResult": "Result of the SQL query",
        "Answer": "Clothing"
    },
    {
        "Question": "What is the total inventory value of all t-shirts?",
        "SQLQuery": "SELECT SUM(price * stock_quantity) FROM t_shirts;",
        "SQLResult": "Result of the SQL query",
        "Answer": "11055"
    },
    {
        "Question": "How many t-shirts are available in size 'L'?",
        "SQLQuery": "SELECT SUM(stock_quantity) FROM t_shirts WHERE size = 'L';",
        "SQLResult": "Result of the SQL query",
        "Answer": "6"
    },
    {
        "Question": "How many t-shirts are priced above 100?",
        "SQLQuery": "SELECT COUNT(*) FROM t_shirts WHERE price > 100;",
        "SQLResult": "Result of the SQL query",
        "Answer": "10"
    },
    {
        "Question": "Which color t-shirt has the highest stock quantity?",
        "SQLQuery": "SELECT color, SUM(stock_quantity) AS total_stock FROM t_shirts GROUP BY color ORDER BY total_stock DESC LIMIT 1;",
        "SQLResult": "Result of the SQL query",
        "Answer": "Red"
    },
    {
        "Question": "What is the average price of t-shirts in stock?",
        "SQLQuery": "SELECT AVG(price) FROM t_shirts;",
        "SQLResult": "Result of the SQL query",
        "Answer": "203.75"
    },
    {
        "Question": "Which brand has the most expensive t-shirt?",
        "SQLQuery": "SELECT brand FROM t_shirts ORDER BY price DESC LIMIT 1;",
        "SQLResult": "Result of the SQL query",
        "Answer": "Electronics"
    },
    {
        "Question": "What is the highest discount percentage available?",
        "SQLQuery": "SELECT MAX(pct_discount) FROM discounts;",
        "SQLResult": "Result of the SQL query",
        "Answer": "45.00"
    },
    {
        "Question": "How many discounted t-shirts are available?",
        "SQLQuery": "SELECT COUNT(DISTINCT t_shirt_id) FROM discounts;",
        "SQLResult": "Result of the SQL query",
        "Answer": "10"
    },
    {
        "Question": "Which t-shirt has the highest discount?",
        "SQLQuery": "SELECT t_shirt_id FROM discounts ORDER BY pct_discount DESC LIMIT 1;",
        "SQLResult": "Result of the SQL query",
        "Answer": "10"
    },
    {
        "Question": "How many t-shirts are available in black color?",
        "SQLQuery": "SELECT SUM(stock_quantity) FROM t_shirts WHERE color = 'Black';",
        "SQLResult": "Result of the SQL query",
        "Answer": "11"
    },
    {
        "Question": "How many red-colored t-shirts are in stock?",
        "SQLQuery": "SELECT SUM(stock_quantity) FROM t_shirts WHERE color = 'Red';",
        "SQLResult": "Result of the SQL query",
        "Answer": "15"
    },
    {
        "Question": "What is the total revenue from all Beauty brand t-shirts without discount?",
        "SQLQuery": "SELECT SUM(price * stock_quantity) FROM t_shirts WHERE brand = 'Beauty';",
        "SQLResult": "Result of the SQL query",
        "Answer": "905"
    },
    {
        "Question": "How many t-shirts are available in size 'S' across all brands?",
        "SQLQuery": "SELECT SUM(stock_quantity) FROM t_shirts WHERE size = 'S';",
        "SQLResult": "Result of the SQL query",
        "Answer": "5"
    },
    {
        "Question": "Which brand has the lowest-priced t-shirt?",
        "SQLQuery": "SELECT brand FROM t_shirts ORDER BY price ASC LIMIT 1;",
        "SQLResult": "Result of the SQL query",
        "Answer": "Clothing"
    }
]
