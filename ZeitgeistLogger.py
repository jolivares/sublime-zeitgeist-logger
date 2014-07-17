import sublime, sublime_plugin
import os, sys, subprocess, threading
from os.path import basename, abspath, dirname, join

LOGGER_CMD = 'zeitgeist-logger'

def _log_file(view):
	if view.file_name() != None:
		name = basename(view.file_name())
		uri = view.file_name()
		
		print("name: %s file_name: %s " % (name, uri))
		
		out = subprocess.Popen([_load_CMD(), name, uri],
								stdout=subprocess.PIPE).communicate()[0]
		print("zeitgeist-logger outcome: %s" % out)

def _load_CMD():
	working_path = join(abspath(dirname(__file__)), LOGGER_CMD)
	default_path = join(sublime.packages_path(), 'ZeitgeistLogger', LOGGER_CMD)
	installed_path = join(sublime.packages_path(), 'ZeitgeistLogger', LOGGER_CMD)	
	
	if os.path.isfile(default_path):
		return default_path
	elif os.path.isfile(installed_path):
		return installed_path
	elif os.path.isfile(working_path):
		return working_path
	else:
		return join('.', LOGGER_CMD)

class ZeitgeistPlugin(sublime_plugin.EventListener):
	def on_load(self, view):
		t = threading.Thread(target=_log_file, args=(view,), kwargs={})
		t.start()
