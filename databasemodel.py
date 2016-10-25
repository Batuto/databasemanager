#-*-coding:utf-8-*-
import psycopg2

"""

def createtable(name,param):
	cur.execute("CREATE TABLE" + name + " (" + param + ");")
	conn.commit()

def inserttable(name,param,value):
	cur.execute("INSERT INTO" + name + " (" + param + ") VALUES("+ value + ");")
	conn.commit()


createtable("test2", "id serial PRIMARY KEY, numeral integer, datos_chidos varchar, otro_campo varchar")
inserttable("test2", "numeral", value)


table = 'products'
fields = '(name, qty, price)'
values = '(ipad, 120, 1243.0)'
"""


#self.conn = psycopg2.connect("dbname=store user=batuto")
#self.cur = conn.cursor()


# FOR PRODUCTS
class QueryModel(object):
	"""
	Docstring
	"""
	def __init__(self, dbname, user, password):
		#
		self.db_usr = "dbname={0} user={1} password={2}".format(dbname, user, password)
		self.conn = psycopg2.connect(self.db_usr)
		self.cur = self.conn.cursor()

	def __parse(self, x , y):
		"""
		Some docstring
		"""
		self.__x = x
		self.__y = y
		if len(x) != len(y):
			return False
		else:
			self.__x = str(self.__x).replace("'", "")
			return self.__x, self.__y

	def create(self, table, fields, values):
		"""This function creates registers in a table.
		"""
		self.table = table
		self.fields, self.values = self.__parse(fields, values)
		self.query = "INSERT INTO {0} {1} values {2};".format(self.table, self.fields, self.values)
		self.cur.execute(self.query)
		return True

	def delete(self, table, field_equ):
		"""This function deletes registers in a table.

			Usage for field_equ:
			field_equ = "fieldname = something"
		"""

		self.query = "DELETE FROM {0} WHERE {1}".format(table, field_equ)
		self.cur.execute(self.query)
		return True

	def edit(self, table, field_values):
		"""This function edits registers in a table.

		SQL Example:

		UPDATE products
		SET stock = False
			price = 0;
		Parameter example:
		field_values = (field1 = "somechar", field2 = False, field3 = 12345, ...)

		"""
		#self.table = table
		#self.fields, self.values = self.__parse(fields, values)
		self.query = "UPDATE {0} SET {1}; ".format(table, field_values)
		self.cur.execute(self.query)
		return True

	def commitq(self):
		self.conn.commit()
		return True

	def disconnect(self):
		"""
		This function terminate the connection.
		"""
		self.cur.close()
		self.conn.close()
		print "dis"
		return True

	def somequery(self, string):
		self.query = "{0}".format(string)
		self.cur.execute(self.query)
		return self.cur.fetchall()





def main():
	dbname = "mama"
	user = "batuto"
	password = "123qwe..."
	database = QueryModel(dbname, user, password)

	table = "product"
	fields = ("kind", "product_name", "perishable", "description", "price")
	values = (1, "Virtual product", True, "A simple description.", 300)
	print database.create(table, fields, values)
	database.commitq()
	database.disconnect()


if __name__ == '__main__':
	main()

"""
def create_product(self, ):
	query = "insert into products (name, qty, price) values ({}, {}, {})".format(name, qty, price)
"""

#cur.close()
#conn.close()

# For debbuging:
# import pdb; pdb.set_trace()
