import sublime, sublime_plugin
from os.path import basename
import subprocess

LOGGER_CMD = 'zeitgeist-logger.py'

class ZeitgeistPlugin(sublime_plugin.EventListener):
	def on_load(self, view):
		if view.file_name() != None:
			name = basename(view.file_name())
			uri = view.file_name()
			
			print "name: %s file_name: %s " % (name, uri)
			
			out = subprocess.Popen(["./" + LOGGER_CMD, name, uri],
									stdout=subprocess.PIPE).communicate()[0]
			print "zeitgeist-logger outcome: %s" % out