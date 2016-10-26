#-*-coding:utf-8-*-
from bottle import template, route, post, error, debug, static_file, get, post, request, run, redirect
from databasemodel import QueryModel
count = 0
visual = True
basedatos = QueryModel("store", "batuto", "123qwe...")

dataproduct = ("Kind", "Id", "Name", "Perishable", "Description", "Price")

get_names = basedatos.somequery("select column_name from information_schema.columns where table_name = 'product';")
column_headers = [element[0] for element in get_names]
print column_headers

def checklogin(user, password):
    query = "SELECT user,password FROM dbuser WHERE user='{0}';".format(user)
    algo = basedatos.somequery(query)
    """try:
    except:
        return False"""
    print algo,type(algo),repr(algo)
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
    global count, visual
    print len(rows),"len"
    if count < 0:
        count = 0
    if len(rows)-1 < count:
        count = len(rows)-1
    print count
    #print rows
    return template("./mysite/views/displaytable.tpl", rows=rows, name="Product Table", data=dataproduct, path="product", count=count, visual=visual)

@route("/modificar/<model>/<id>")
def item(model, id):
    query = "SELECT * FROM {0} WHERE {0}_id = {1} ;".format(model, id)
    print query
    row = basedatos.somequery(query)
    print row,"<---------------------------------------"
    get_names = "select column_name,data_type from information_schema.columns where table_name = '{0}';".format(model)
    return template("./mysite/views/record.tpl", row = row, data = dataproduct, path = model)

"""@route("/guardar/<model>/<id>", method="POST")
def guardar(model, id):
    print request.forms
    #rows = get_model_headers()
    #values = parse_values(post)
    print request.forms
    query = ["{} = {}".format(k, request.forms.get(k)) for k in request.forms.iterkeys()]
    print query"""

@route("/guardar/product/<id>", method = "POST")
def guardarD(id):

    kind = request.forms.get("Kind")
    idd = request.forms.get("Id")
    name = request.forms.get("Name")
    perishable = bool(request.forms.get("Perishable", False))
    print perishable,"<<<<<<<<<<<<<<"
    description = request.forms.get("Description")
    price = request.forms.get("Price")
    valores = "kind = {0}, product_name = '{1}', perishable = {2}, description = '{3}', price = {4} WHERE product_id={5}".format(kind, name, perishable, description, price, id)
    basedatos.edit("product", valores)
    basedatos.commitq()
    redirect("/product")
    #print request.forms
    #print request.forms
    #query = ["{} = {}".format(k, request.forms.get(k)) for k in request.forms.iterkeys()]
    #print query

@route("/borrar/product/<id>", method = "POST")
def borrarD(id):
    field_equ = "product_id = {0}".format(id)
    basedatos.delete("product", field_equ)
    basedatos.commitq()
    redirect("/product")

@route("/nuevo/<path>")
def nuevo(path):
    global dataproduct
    
    if path == "product":
        data = dataproduct

    return template("./mysite/views/new_record.tpl", data = data, path = path)




@route("/product/guardar", method="POST")
def productDS():
    kind = request.forms.get("Kind")
    idd = request.forms.get("Id")
    name = request.forms.get("Name")
    print request.forms.get("comes_from")
    perishable = request.forms.get("Perishable")
    if not perishable:
        perishable = False
    description = request.forms.get("Description")
    price = request.forms.get("Price")
    if request.forms.get("Insertar", False):
        print "entrando"
        basedatos.create("product", ("kind","product_name","perishable","description","price"), (kind,name,perishable,description,price))
        basedatos.commitq()
    redirect("/product")

"""@route("/product/modificar", method="POST")
def productDM():
    global count
    print request.forms.get("Modificar")
    kind = request.forms.get("Kind")
    idd = request.forms.get("Id")
    name = request.forms.get("Name")
    perishable = request.forms.get("Perishable")
    
    if not perishable:
        perishable = False
    description = request.forms.get("Description")
    price = request.forms.get("Price")
    if request.forms.get("Modificar", False):
        valores = "kind = {0}, product_name = '{1}', perishable = {2}, description = '{3}', price = {4} WHERE product_id={5}".format(kind, name, perishable, description, price, count+1)
        basedatos.edit("product", valores)
        basedatos.commitq()
        redirect("/product")

@route("/product", method="POST")
def productD():
    global count
    print request.forms.get("Modificar")
    kind = request.forms.get("Kind")
    idd = request.forms.get("Id")
    name = request.forms.get("Name")
    perishable = request.forms.get("Perishable")
    if not perishable:
        perishable = False
    description = request.forms.get("Description")
    price = request.forms.get("Price")

    if request.forms.get("Siguiente", False):
        count += 1
        print count
        visual = True
        redirect("/product")

    if request.forms.get("Anterior", False):
        count -= 1
        print count
        visual = True
        redirect("/product")
    #
    redirect("/product")
        
"""

@route("/purchase")
def purchase():
    rows = basedatos.somequery("SELECT * FROM purchase;")
    print rows
    return template("./mysite/views/displaytable.tpl", rows=rows, name="Purchase Table", visual=visual)

@route("/store")
def store():
    rows = basedatos.somequery("SELECT * FROM store;")
    #print rows
    return template("./mysite/views/displaytable.tpl", rows=rows, name="Store Table", visual=visual)

@route("/supplier")
def supplier():
    rows = basedatos.somequery("SELECT * FROM supplier;")
    #print rows
    return template("./mysite/views/displaytable.tpl", rows=rows, name="Supplier Table", path="supplier", data=("Rfc", "Name", "Phone", "Address", "Email"), visual=visual)


@route("/static/<path:path>")
def send_static(path):
    return static_file(path, root="./mysite/static/")

run(host='localhost', port=8080, reloader=True, debug=True)