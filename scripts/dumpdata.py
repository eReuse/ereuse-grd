# NOTE just copy following instructions into a test to dump the current
# data of the database
from django.core.management import call_command                                                                         
call_command('dumpscript', 'grd') 
