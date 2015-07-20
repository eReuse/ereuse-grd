#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file has been automatically generated.
# Instead of changing it, create a file called import_helper.py
# and put there a class called ImportHelper(object) in it.
#
# This class will be specially casted so that instead of extending object,
# it will actually extend the class BasicImportHelper()
#
# That means you just have to overload the methods you want to
# change, leaving the other ones inteact.
#
# Something that you might want to do is use transactions, for example.
#
# Also, don't forget to add the necessary Django imports.
#
# This file was generated with the following command:
# ./manage.py dumpscript grd
#
# to restore it, run
# manage.py runscript module_name.this_script_name
#
# example: if manage.py is at ./manage.py
# and the script is at ./some_folder/some_script.py
# you must make sure ./some_folder/__init__.py exists
# and run  ./manage.py runscript some_folder.some_script

from django.db import transaction

class BasicImportHelper(object):

    def pre_import(self):
        pass

    # You probably want to uncomment on of these two lines
    # @transaction.atomic  # Django 1.6
    # @transaction.commit_on_success  # Django <1.6
    def run_import(self, import_data):
        import_data()

    def post_import(self):
        pass

    def locate_similar(self, current_object, search_data):
        # You will probably want to call this method from save_or_locate()
        # Example:
        #   new_obj = self.locate_similar(the_obj, {"national_id": the_obj.national_id } )

        the_obj = current_object.__class__.objects.get(**search_data)
        return the_obj

    def locate_object(self, original_class, original_pk_name, the_class, pk_name, pk_value, obj_content):
        # You may change this function to do specific lookup for specific objects
        #
        # original_class class of the django orm's object that needs to be located
        # original_pk_name the primary key of original_class
        # the_class      parent class of original_class which contains obj_content
        # pk_name        the primary key of original_class
        # pk_value       value of the primary_key
        # obj_content    content of the object which was not exported.
        #
        # You should use obj_content to locate the object on the target db
        #
        # An example where original_class and the_class are different is
        # when original_class is Farmer and the_class is Person. The table
        # may refer to a Farmer but you will actually need to locate Person
        # in order to instantiate that Farmer
        #
        # Example:
        #   if the_class == SurveyResultFormat or the_class == SurveyType or the_class == SurveyState:
        #       pk_name="name"
        #       pk_value=obj_content[pk_name]
        #   if the_class == StaffGroup:
        #       pk_value=8

        search_data = { pk_name: pk_value }
        the_obj = the_class.objects.get(**search_data)
        #print(the_obj)
        return the_obj


    def save_or_locate(self, the_obj):
        # Change this if you want to locate the object in the database
        try:
            the_obj.save()
        except:
            print("---------------")
            print("Error saving the following object:")
            print(the_obj.__class__)
            print(" ")
            print(the_obj.__dict__)
            print(" ")
            print(the_obj)
            print(" ")
            print("---------------")

            raise
        return the_obj


importer = None
try:
    import import_helper
    # We need this so ImportHelper can extend BasicImportHelper, although import_helper.py
    # has no knowlodge of this class
    importer = type("DynamicImportHelper", (import_helper.ImportHelper, BasicImportHelper ) , {} )()
except ImportError as e:
    # From Python 3.3 we can check e.name - string match is for backward compatibility.
    if 'import_helper' in str(e):
        importer = BasicImportHelper()
    else:
        raise

import datetime
from decimal import Decimal
from django.contrib.contenttypes.models import ContentType

try:
    import dateutil.parser
except ImportError:
    print("Please install python-dateutil")
    sys.exit(os.EX_USAGE)

def run():
    importer.pre_import()
    importer.run_import(import_data)
    importer.post_import()

def import_data():
    # Initial Imports
    from django.contrib.auth.models import User

    # Processing model: Device

    from grd.models import Device

    grd_device_1 = Device()
    grd_device_1.id = '//xsr.cat/device/1234'
    grd_device_1.hid = 'XPS13-1111-2222'
    grd_device_1.type = 'computer'
    grd_device_1 = importer.save_or_locate(grd_device_1)

    # Processing model: Agent

    from grd.models import Agent

    grd_agent_1 = Agent()
    grd_agent_1.name = 'XSR'
    grd_agent_1.description = ''
    grd_agent_1.user =  importer.locate_object(User, "id", User, "id", 1, {'username': 'ereuse', 'is_staff': True, 'is_superuser': True, 'is_active': True, 'first_name': '', 'date_joined': datetime.datetime(2015, 7, 20, 12, 22, 10, 97604, tzinfo=<UTC>), 'last_login': None, 'password': 'pbkdf2_sha256$20000$txVP7VTbH6Mx$g09pX9Ge0bXHwXcSoXCDwiqXWpHp/fjNtCW3EkEX7tk=', '_agent_cache': 'XSR', 'email': 'test@localhost', 'id': 1, 'last_name': ''} )
    grd_agent_1 = importer.save_or_locate(grd_agent_1)

    # Processing model: Event

    from grd.models import Event

    grd_event_1 = Event()
    grd_event_1.timestamp = dateutil.parser.parse("2015-07-20T12:22:10.244184+00:00")
    grd_event_1.type = 'register'
    grd_event_1.data = {}
    grd_event_1.event_time = dateutil.parser.parse("2012-04-10T22:38:20.604391+00:00")
    grd_event_1.by_user = 'foo'
    grd_event_1.agent = grd_agent_1
    grd_event_1.device = grd_device_1
    grd_event_1 = importer.save_or_locate(grd_event_1)

    # Processing model: Location

    from grd.models import Location

    grd_location_1 = Location()
    grd_location_1.lat = 27.9878943
    grd_location_1.lon = 86.9247837
    grd_location_1.event = grd_event_1
    grd_location_1 = importer.save_or_locate(grd_location_1)


