Solution Design
--------------------
Task 5
--------------------

Customer is facing following problem: when processing xml file via cron-job, cron-job fails, doesn’t process all lines (
connection timem-out, CPU time limit exceeded). File is very big and increasing limit_time_real_cron or other params on
odoo.config, doesn’t solves the issue.

The cron-job is creating/updating products from xml file.
Xml could look like this, but with much more <book>
tags: https://learn.microsoft.com/en-us/previous-versions/windows/desktop/ms762271(v=vs.85)

```
<?xml version="1.0"?>
<catalog>
   <book id="bk101">
      <author>Gambardella, Matthew</author>
      <title>XML Developer's Guide</title>
      <genre>Computer</genre>
      <price>44.95</price>
      <publish_date>2000-10-01</publish_date>
      <description>An in-depth look at creating applications 
      with XML.</description>
   </book>
   <book id="bk102">
      <author>Ralls, Kim</author>
      <title>Midnight Rain</title>
      <genre>Fantasy</genre>
      <price>5.95</price>
      <publish_date>2000-12-16</publish_date>
      <description>A former architect battles corporate zombies, 
      an evil sorceress, and her own childhood to become queen 
      of the world.</description>
   </book>
   ...
</catalog>
```

-[ ] Write a solution design, how you would fix this issue

-[ ] Provide estimation for development


---------------------------
first of all whe 