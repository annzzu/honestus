Ana Zurabashvili
--------------------
Version: odoo 16
---------------------
This is my first Honestus Task.
You can run this project by adding in custom file and connect it with odoo 16
---------------------
You can find some description/illustration on google
slide  :
https://docs.google.com/presentation/d/1o8geBJ3iZ3IcPV1LQJ6v6XmA43qWgSRQ2Wsn_ahUh-8/edit?usp=sharing

README will be updated any moment now.

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

[//]: # (db_name=honestus_1)

[//]: # (update=honestus)
```