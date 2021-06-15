import dbm

# ID, Name, Descripcion, OwnerID, Price, Condition, DataRegistered
items = [
    ['1', 'Lawnmower', 'Tool', '1', '$150', 'Excelente', '2021-01-05'],
    ['2', 'Lawnmower', 'Tool', '2', '$370', 'Fair', '2021-03-10'],
    ['3', 'Bike', 'Tool', '3', '$150', 'Good', '2021-02-05'],
    ['4', 'Diller', 'Tool', '4', '$150', 'Good', '2020-10-25'],
    ['5', 'Spinkler', 'Tool', '5', '$150', 'Average', '2020-12-30'],
    ['6', 'Spinkler', 'Tool', '1', '$150', 'Good', '2021-01-06']
]

# ID, Name, Email
members = [
    ['1', 'Fred', 'freddy@lendydyi.com'],
    ['2', 'Mike', 'micky@lendydyi.com'],
    ['3', 'Bob', 'bobby@hotmail.com'],
    ['4', 'Annie', 'annie@gmail.com'],
    ['5', 'Rin', 'godessRin@thiccThighsSaveLives.com']
]

# ID, ItemID, borrowerID, DateBorrowed, DateReturned
loans = [
    ['1', '1', '3', '4/26/2021', '06/01/2021'],
    ['2', '2', '5', '1/15/2021', '2/25/2021'],
    ['3', '3', '4', '7/26/2020', '01/10/2021'],
    ['4', '4', '1', '4/26/2021', '5/01/2021'],
    ['5', '5', '2', '4/26/2021', 'None'],
]


def createDB(data, dbName):
    try:
        db = dbm.open(dbName, 'c')
        for datum in data:
            db[datum[0]] = ','.join(datum)
    finally:
        db.close()
        print(dbName, 'created')


def readDB(dbName):
    try:
        db = dbm.open(dbName, 'r')
        print('Reading', dbName)
        return [db[datum] for datum in db]
    finally:
        db.close()


def main():
    print('Creating data files...')
    createDB(items, 'itemdb')
    createDB(members, 'memberdb')
    createDB(loans, 'loandb')

    print('reading data files...')
    print(readDB('itemdb'))
    print(readDB('memberdb'))
    print(readDB('loandb'))


if __name__ == "__main__":
    main()
