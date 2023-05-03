import sqlite3


def exdata(cur):
  cur.execute("SELECT * FROM users;")
  one_result = cur.fetchone()
  print(one_result)

  cur.execute("SELECT * FROM users;")
  three_results = cur.fetchmany(3)
  print(three_results)

  cur.execute("SELECT * FROM users;")
  three_results = cur.fetchall()
  print(three_results)


def adddata(cur,conn):
  customers = [
    ('00005', 'Stephanie', 'Stewart', 'female'), ('00006', 'Sincere', 'Sherman', 'female'),
    ('00007', 'Sidney', 'Horn', 'male'),
    ('00008', 'Litzy', 'Yates', 'female'), ('00009', 'Jaxon', 'Mills', 'male'), ('00010', 'Paul', 'Richard', 'male'),
    ('00011', 'Kamari', 'Holden', 'female'), ('00012', 'Gaige', 'Summers', 'female'),
    ('00013', 'Andrea', 'Snow', 'female'),
    ('00014', 'Angelica', 'Barnes', 'female'), ('00015', 'Leah', 'Pitts', 'female'),
    ('00016', 'Dillan', 'Olsen', 'male'),
    ('00017', 'Joe', 'Walsh', 'male'), ('00018', 'Reagan', 'Cooper', 'male'), ('00019', 'Aubree', 'Hogan', 'female'),
    ('00020', 'Avery', 'Floyd', 'male'), ('00021', 'Elianna', 'Simmons', 'female'),
    ('00022', 'Rodney', 'Stout', 'male'),
    ('00023', 'Elaine', 'Mcintosh', 'female'), ('00024', 'Myla', 'Mckenzie', 'female'),
    ('00025', 'Alijah', 'Horn', 'female'),
    ('00026', 'Rohan', 'Peterson', 'male'), ('00027', 'Irene', 'Walters', 'female'),
    ('00028', 'Lilia', 'Sellers', 'female'),
    ('00029', 'Perla', 'Jefferson', 'female'), ('00030', 'Ashley', 'Klein', 'female')
  ]

  cur.executemany("INSERT INTO users VALUES(?, ?, ?, ?);", customers)
  conn.commit()


def main():
  conn = sqlite3.connect('datafile.db')

  cur = conn.cursor()
  cur.execute("""CREATE TABLE IF NOT EXISTS users(
     userid INT PRIMARY KEY,
     fname TEXT,
     lname TEXT,
     gender TEXT);
  """)
  conn.commit()
  exdata(cur)
  conn.close()

if __name__ == "__main__":
	main()