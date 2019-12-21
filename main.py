import sqlite3 as lite

class Database(object):
    
    def __init__(self):
        global cone
        try:
            cone = lite.connect('main.db')
            with cone:
                cur = cone.cursor()
                sql = "CREATE TABLE IF NOT EXISTS main(Id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, type TEXT, number INTEGER, Mobile INTEGER)"
                cur.execute(sql)
        except Exception:
            print("Unable To Create DB!")
        
    def insertdata(self, data):
        try:
            with cone:
                cur = cone.cursor()
                sql = "INSERT INTO main(name, type, number, mobile) VALUES(?,?,?,?)"
                cur.execute(sql,data)
                return True
        except Exception:
            return False

    def fetchdata(self):
        try:
            with cone:
                cur = cone.cursor()
                sql = "SELECT * FROM main"
                cur.execute(sql)
                return cur.fetchall()
        except Exception:
            return False
    
    def deletedata(self, id):
        try:
            with cone:
                cur = cone.cursor()
                cur.execute("DELETE FROM main WHERE id = ?", [id])
                return True
        except Exception:
            return False

def main():

    print('#'*30)
    print("\n:: PARKING MANAGEMENT ::\n")
    print('#'*30)

    db = Database()

    print('\nPress 1. Insert New Entry')
    print('\nPress 2. Show All Entry')
    print('\nPress 3. Delete Entry')

    print('\n')
    print('#'*30)

    choice = input("\n Enter a Choice: ")

    if choice == '1':
        name = input("\n Enter Name of Ownner: ")
        typeof = input("\n Type of Vehicle: ")
        number = input("\n Enter Vehicle Number: ")
        mobile = input("\n Enter Mobile Number: ")

        if db.insertdata([name, typeof, number, mobile]):
            print("Entry inserted Sucess")
        else:
            print("Something went wrong")
    
    elif choice == '2':
        print("\n:: List :: \n")

        for iteam in db.fetchdata():
            print("\n ID : " + str(iteam[0]))
            print("\n Name of Owner : " + str(iteam[1]))
            print("\n Type of Vehicle : " + str(iteam[2]))
            print("\n Vehicle Number : " + str(iteam[3]))
            print("\n Mobile No : " + str(iteam[4]))
            print("\n")
    
    elif choice == '3':
        record_id = input("Enter the ID No: ")

        if db.deletedata(record_id):
            print("Entry deleted Sucessfully ")
        else:
            print("Something went wrong")

    else:
        print("\n Enterd Number IS Out Of Range")

if __name__ == '__main__':
    main()