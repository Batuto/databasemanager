#-*-coding:utf-8-*-
from bottle import template, route, post, error, debug, static_file, get, post, request, run, redirect
from databasemodel import QueryModel
count = 0
basedatos = QueryModel("store", "batuto", "123qwe...")

def checklogin(user, password):
	query = "SELECT user,password FROM dbuser WHERE user='{0}';".format(user)
	algo = basedatos.somequery(query)
	"""try:
	except:
		return False"""
	if user == algo[0] and password == algo[1]:
		return True
	else:
		return False

@route("/")
def indx():
	return template("./mysite/views/index.tpl")

@route("/", method="POST")
def login():
	user = request.forms.get("username")
	password = request.forms.get("password")
	if checklogin(user, password):
		a = "Granted Access!"
	else:
		a = "Wrong user and/or password."

	return template("./mysite/views/base.tpl", title="Hi", base="<br><p>{0}</p>".format(a))

@route("/menu")
def menu():
	#if validated:
	return template("./mysite/views/menu.tpl", base="Hi")

@route("/product")
def product():
	rows = basedatos.somequery("SELECT * FROM product;")
	global count
	print len(rows),"len"
	if count < 0:
		count = 0
	if len(rows)-1 < count:
		count = len(rows)-1
	print count
	#print rows
	return template("./mysite/views/displaytable.tpl", rows=rows, name="Product Table", data=("Kind", "Id", "Name", "Perishable", "Description", "Price"), path="product", count=count)

@route("/product", method="POST")
def productD():
	global count
	kind = request.forms.get("Kind")
	idd = request.forms.get("Id")
	name = request.forms.get("Name")
	perishable = request.forms.get("Perishable")
	if not perishable:
		perishable = False
	description = request.forms.get("Description")
	price = request.forms.get("Price")

	if request.forms.get("Siguiente") == "Siguiente":
		count += 1
		print count
		redirect("/product")
		return True

	if request.forms.get("Anterior") == "Anterior":
		count -= 1
		print count
		redirect("/product")
		return True


	else:
		print request.forms.get("Anterior"),"<<"
		print name, "<<"

		modflag = request.forms.get("Modificar")
		print modflag,"<<<<<<"
		if request.forms.get("Modificar", False):
			valores = "kind = {0}, product_name = '{1}', perishable = {2}, description = '{3}', price = {4} WHERE product_id={5}".format(kind, name, perishable, description, price, count+1)
			basedatos.edit("product", valores)
			basedatos.commitq()
			redirect("/product")
			return


		insertar = request.forms.get("Insertar")
		print insertar
		if insertar == "on":
			print "entrando"
			basedatos.create("product", ("kind","product_name","perishable","description","price"), (kind,name,perishable,description,price))
			basedatos.commitq()
		redirect("/product")

@route("/purchase")
def purchase():
	rows = basedatos.somequery("SELECT * FROM purchase;")
	print rows
	return template("./mysite/views/displaytable.tpl", rows=rows, name="Purchase Table")

@route("/store")
def store():
	rows = basedatos.somequery("SELECT * FROM store;")
	#print rows
	return template("./mysite/views/displaytable.tpl", rows=rows, name="Store Table")

@route("/supplier")
def supplier():
	rows = basedatos.somequery("SELECT * FROM supplier;")
	#print rows
	return template("./mysite/views/displaytable.tpl", rows=rows, name="Supplier Table", path="supplier", data=("Rfc", "Name", "Phone", "Address", "Email"))


@route("/static/<path:path>")
def send_static(path):
	return static_file(path, root="./mysite/static/")

run(host='0.0.0.0', port=8080, reloader=True, debug=True)
