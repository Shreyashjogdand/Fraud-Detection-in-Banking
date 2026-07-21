import sqlite3, os

print("This script is running in folder:")
print("  ", os.getcwd())
print()
print("It will use this database file:")
print("  ", os.path.abspath("BankNH.db"))
print()

conn = sqlite3.connect("BankNH.db")
cur = conn.cursor()
print("shruti's balance in THIS database:")
for r in cur.execute("SELECT USERNAME, BAL FROM NEWBANK WHERE USERNAME='shruti'"):
    print("  ", r)
conn.close()