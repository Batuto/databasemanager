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
	#print rows
	return template("./mysite/views/displaytable.tpl", rows=rows, name="Product Table", data=("Kind", "Id", "Name", "Perishable", "Description", "Price"), path="product")

@route("/product", method="POST")
def productD():
	if request.forms.get("Anterior") == "on":
		redirect("/menu")
	print request.forms.get("Anterior"),"<<"
	kind = request.forms.get("Kind")
	idd = request.forms.get("Id")
	name = request.forms.get("Name")
	perishable = request.forms.get("Perishable")
	if not perishable:
		perishable = False
	description = request.forms.get("Description")
	price = request.forms.get("Price")
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
	return template("./mysite/views/displaytable.tpl", rows=rows, name="Supplier Table")


@route("/static/<path:path>")
def send_static(path):
	return static_file(path, root="./mysite/static/")

run(host='localhost', port=8080, reloader=True, debug=True)