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
First of all, I would like to have an opportunity to see the problem. It would be helpful to decide much more optimized version. The useful thing would be to see how the cron is written and how the xml data is attached to the cron. If there was a possibility to change xml formatted file with another format, such as CSV or JSON it would be more optimized due to its faster and easier. 


Before I would start to do something, I mean coding, I would surf the google and search some optimization, xml parsing and some good practices. 

However, this problem is only for discussion. Isn’t it ?



In order to resolve the problem, we need to optimize the code that reads and interpret XML File.
There is potential solving method.

The book objects in the xml have primary field (mostly string and float) we know how each field looks like. So in my
opinion if we know and the fields are primary, it could be more optimized to write our own xml parser. Existing xml
parser is heavy, in spite of it’s recommended to use one, we can decide not to use it.  
Or it can be done ->  xml parse into json object.

-[ ] Split the large XML file into smaller chunks for processing. We can use a library like lxml or ElementTree to
 parse ( or do the one I have mentioned previously) in the XML file and divide it into smaller parts.

-[ ]  Every chunk should be released into different threads Process to improve the performance. (use multi threads)

-[ ] We can store/update data directly. We can use Odoo ORM to interact with the database and store the products. Or
 like I said before the book contains primary data we can use sql queries to make process more optimized (it’s faster)
 This will improve performance and prevent the system from running out of memory.

- [ ] During the processing of the data, I would add implementation of error handling and logging mechanisms to monitor
  the processing and detect any issues that might arise. And it’s depended on to business logic when we want to commit
  this data storing process, in my opinion I would right commit code in the end of the process (every thread finishes).
  And if there would be given demand to update data in the system beside failure I would skip this object and update
  remaining ones.

If there would be given demand to update data if there is any problem I would write code to reply this cron.

If there is any error rollback.
---------------------------
Splitting the large XML file and writing parser: 8-12 hours

Implementing a multi-threading: 10-12 hours

Error handling and logging: 10 hours

Code optimization: 8- more hours

I have given max hours on each process. he total estimated would be around 40-60 hours. (it's not sum but there could be
some unplanned situations)

