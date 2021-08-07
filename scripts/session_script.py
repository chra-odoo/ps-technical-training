from xmlrpc import client

url = 'https://chra-odoo-ps-technical-training-main-3011614.dev.odoo.com'
db = 'chra-odoo-ps-technical-training-main-3011614'
username = 'admin'
password = 'admin'

common = client.ServerProxy("%s/xmlrpc/2/common" % url)
print(common.version())

uid = common.authenticate(db, username, password, {})
print(uid)

# check for model access
models = client.ServerProxy("%s/xmlrpc/2/object" % url)
model_access = models.execute_kw(db, uid, password, 'academy.session', 'check_access_rights', ['write'], {'raise_exception': False})
print(model_access)

# get courses intermediate or beginner
courses = models.execute_kw(db, uid, password, 'academy.course', 'search_read', [[['level', 'in', ['intermediate', 'beginner']]]])
print(courses)

course = models.execute_kw(db, uid, password, 'academy.course', 'search', [[['name', '=', 'Accounting 200']]])
print(course)

session_fields = models.execute_kw(db, uid, password, 'academy.session', 'fields_get', [], {'attributes': ['string', 'type', 'required']})
print(session_fields)