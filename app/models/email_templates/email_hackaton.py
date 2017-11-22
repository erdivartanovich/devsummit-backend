import os, codecs
from app.services.helper import Helper


class EmailHackaton():
	"""docstring for EmailPurchase"""

	def __init__(self, file_name):
		currpath = os.path.abspath(os.curdir)
		file_path = "%s/%s" % ("app/models/email_templates", file_name)
		path = os.path.join(currpath, file_path)
		f = codecs.open(path, 'r', 'utf-8')
		template_list = f.read()
		f.close()
		self.template = str(template_list)

	def build(self, name, content=''):
		return self.template.replace('[ name ]', name) + content
