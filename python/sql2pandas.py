import pandas as pd
import pymysql as sql
import warnings

warnings.filterwarnings("ignore", category=UserWarning)

conn = sql.connect(
        host="localhost",
        user="nikin",
        password="1234",
        database="bookshop"
    )

cursor = conn.cursor()

query = 'SELECT * FROM books'

df = pd.read_sql(query, conn)

conn.close()

def good_books(books: pd.DataFrame) -> pd.DataFrame:
    result = books[ (books['price'] > 50) | (books['edition'] < 2000) ]
    desired_columns = ['name', 'price', 'edition']
    return result.loc[:, desired_columns ]

print(good_books(df))
