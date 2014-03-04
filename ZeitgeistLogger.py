import sublime, sublime_plugin
from os.path import basename
import subprocess

class ZeitgeistPlugin(sublime_plugin.EventListener):
	def on_load(self, view):
		if view.file_name() != None:
			print "name: %s file_name: %s " %(basename(view.file_name()), view.file_name())
			out = subprocess.Popen(["python", "zeitgeist-logger.py", 
				basename(view.file_name()), view.file_name()],
				stdout=subprocess.PIPE).communicate()[0]
			print "zeitgeist-logger outcome: %s" % out