import sqlite3

conn = sqlite3.connect("ecoloop.db")
cursor = conn.cursor()

cursor.execute("""
SELECT * FROM informacoes;
""")

for linha in cursor.fetchall():
    print(linha)

conn.close()
