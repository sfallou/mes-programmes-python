#!/usr/bin/python3
# -*- coding: UTF-8 -*-
html_header = 'Content-type: text/html\r\n\r\n'
html_code= '''
<!DOCTYPE html>
<html>
  <head>
        <meta charset="utf-8" />
        <title>Hello World</title>
  </head>
   <body>
        Hello World!
        <H3><FONT COLOR="Royal blue">
 	Page web produite par un script Python
	</FONT></H3>
  
 <FORM ACTION="print_result.py" METHOD="get">
<P>Veuillez entrer votre nom dans le champ ci-dessous, s.v.p. :</P>
<P><INPUT NAME="visiteur" SIZE=20 MAXLENGTH=20 TYPE="text"></P>
<P>Veuillez également me fournir une phrase quelconque :</P>
<TEXTAREA NAME="phrase" ROWS=2 COLS=50>Mississippi</TEXTAREA>
<P>J'utiliserai cette phrase pour établir un histogramme.</P>
<INPUT TYPE="submit" NAME="send" VALUE="Action">
</FORM>
    </body>
</html>
'''
print(html_header)
print(html_code)
