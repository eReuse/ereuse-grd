# There are issues with pydot and Python 3 compatibility
# https://github.com/erocarrera/pydot/issues/76
# In the meanwhile we can generate a .dot and then .png
./manage.py graph_models grd > models.dot
dot -Tpng models.dot -o models.png

#############################################
#Traceback (most recent call last):
#  File "./manage.py", line 10, in <module>
#    execute_from_command_line(sys.argv)
#  File "/usr/local/lib/python3.4/dist-packages/django/core/management/__init__.py", line 338, in execute_from_command_line
#    utility.execute()
#  File "/usr/local/lib/python3.4/dist-packages/django/core/management/__init__.py", line 330, in execute
#    self.fetch_command(subcommand).run_from_argv(self.argv)
#  File "/usr/local/lib/python3.4/dist-packages/django/core/management/base.py", line 390, in run_from_argv
#    self.execute(*args, **cmd_options)
#  File "/usr/local/lib/python3.4/dist-packages/django/core/management/base.py", line 441, in execute
#    output = self.handle(*args, **options)
#  File "/usr/local/lib/python3.4/dist-packages/django_extensions/management/utils.py", line 71, in inner
#    ret = func(self, *args, **kwargs)
#  File "/usr/local/lib/python3.4/dist-packages/django_extensions/management/commands/graph_models.py", line 89, in handle
#    self.render_output_pydot(dotdata, **options)
#  File "/usr/local/lib/python3.4/dist-packages/django_extensions/management/commands/graph_models.py", line 141, in render_output_pydot
#    graph = pydot.graph_from_dot_data(dotdata)
#  File "/usr/lib/python3/dist-packages/pydot.py", line 220, in graph_from_dot_data
#    return dot_parser.parse_dot_data(data)
#  File "/usr/lib/python3/dist-packages/dot_parser.py", line 510, in parse_dot_data
#    if data.startswith(codecs.BOM_UTF8):
#TypeError: startswith first arg must be str or a tuple of str, not bytes
