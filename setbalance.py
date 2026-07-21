import sqlite3
conn = sqlite3.connect(r"C:\mcacet documents\Bank-Fraud-Detection-main\BankNH.db")
cur = conn.cursor()
cur.execute("UPDATE NEWBANK SET BAL = 50000 WHERE USERNAME = 'shruti'")
conn.commit()
for r in cur.execute("SELECT USERNAME, BAL FROM NEWBANK"):
    print(r)
conn.close()
print("Done")