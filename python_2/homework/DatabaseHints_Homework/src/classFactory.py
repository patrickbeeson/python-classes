"""
classFactory: function to return tailored classes
"""

def build_row(table, cols):
    """Build a class that creates instances of specific rows"""
    class DataRow:
        """Generic data row class, specialized by surrounding function"""
        def __init__(self, data):
            """Uses data and column names to inject attributes"""
            assert len(data)==len(self.cols)
            for colname, dat in zip(self.cols, data):
                setattr(self, colname, dat)
        def __repr__(self):
            return "{0}_record({1})".format(self.table, ", ".join(["{0!r}".format(getattr(self, c)) for c in self.cols]))
        def retrieve(self, curs, *args):
            query = 'SELECT * FROM {}'.format(self.table)
            if len(args):
                curs.execute('{} WHERE {}'.format(query, (' AND '.join(args))))
            else:
                curs.execute('{}'.format(query))
            for r in curs.fetchall():
                yield DataRow(r)

    DataRow.table = table
    DataRow.cols = cols.split()
    return DataRow

#if __name__ == "__main__":
#    import mysql.connector
#    from database import login_info
#    db = mysql.connector.Connect(**login_info)
#    curs = db.cursor()
#    condition = 'weight > 100'
#    condition1 = 'id > 2'
#    Animal_Row = build_row("animal", "id name family weight")
#    actual_animal = Animal_Row([2, "Polly", "Parrot", 100])
#    
#    for data_row in actual_animal.retrieve(curs, condition, condition1):
#        print(data_row)
