import sublime, sublime_plugin
import os, sys, subprocess, threading
from os.path import basename, abspath, dirname, join

LOGGER_CMD = 'zeitgeist-logger'
LOGGED_FLAG = 'logged-to-zeitgeist'

def _log_file(view):
	if view.file_name() != None and view.get_status(LOGGED_FLAG) == "":		
		name = basename(view.file_name())
		uri = view.file_name()

		print("name: {0} file_name: {1} ".format(name, uri))

		out = subprocess.Popen([_load_CMD(), name, uri],
								stdout=subprocess.PIPE).communicate()[0]
		view.set_status(LOGGED_FLAG, 'OK')
		print("zeitgeist-logger outcome: {0}".format(out))

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
	def on_post_save(self, view):
		t = threading.Thread(target=_log_file, args=(view,), kwargs={})
		t.start()
