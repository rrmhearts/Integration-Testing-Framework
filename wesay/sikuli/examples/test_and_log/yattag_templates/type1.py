from __future__ import with_statement
from yattag import Doc

def template(fail):
	doc, tag, text = Doc().tagtext()
	with tag("li"):
		text(str(fail.thing1) + " and also " + str(fail.thing2))
	return doc.getvalue()
