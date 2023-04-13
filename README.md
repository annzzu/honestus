Ana Zurabashvili
--------------------
Version: odoo 16
---------------------
This is my first Honestus Task.
You can run this project by adding in custom file and connect it with odoo 16
---------------------

> - [ ]  Script path: odoo-bin
> - [ ]  Parameters: -c odoo.conf -u honestus
--------------------
### odoo.conf

```
[options]
admin_passwd ={admin password}
db_host=False
db_port=5432
db_user={user}
db_password={db password}
db_list = True
http_port = 8069
addons_path = {Odoo location}/odoo-16/addons,{Odoo location}/customaddons/honestus
# db_name={database name}
# update=honestus

```