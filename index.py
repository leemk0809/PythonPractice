#!python
print("content-type:text/html; charset=utf-8;\n")
import cgi
form = cgi.FieldStorage()
if 'id' in form:
    pageId = form["id"].value
    _desc = open('data/'+pageId, 'r').read()
else:
    pageId = 'Welcome'
    _desc = 'Hello, web'
print('''
<!doctype html>
<html>
<head>
  <title>WEB1 - Welcome</title>
  <meta charset="utf-8">
</head>
<body>
  <h1><a href="index.py">WEB</a></h1>
  <ol>
    <li><a href="index.py?id=HTML">HTML</a></li>
    <li><a href="index.py?id=CSS">CSS</a></li>
    <li><a href="index.py?id=JavaScript">JavaScript</a></li>
    <li><a href="index.py?id=Python">Python</a></li>
  </ol>
  <h2>{title}</h2>
  <p>{desc}</p>
</body>
</html>
'''.format(title=pageId, desc=_desc))
