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
model_access = models.execute_kw(db, uid, password, 'sale.order', 'check_access_rights', ['write'], {'raise_exception': False})
print(model_access)

# get the sales orders in draft state
draft_quotes = models.execute_kw(db, uid, password, 'sale.order', 'search', [[['state', '=', 'draft']]])
print(draft_quotes)

# confirm the draft quotes
if_confirmed = models.execute_kw(db, uid, password, 'sale.order', 'action_confirm', [draft_quotes])
print(if_confirmed)
