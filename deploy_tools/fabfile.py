from fabric.contrib.files import append, exists, sed
from fabric.api import env, local, run
import random


REPO_URL = 'https://github.com/ereuse/grd-sandbox.git'


def _create_directory_structure_if_necessary(site_folder):
    for subfolder in ('media', 'static', 'virtualenv', 'source'):
        run('mkdir -p %s/%s' % (site_folder, subfolder))


def _get_latest_source(source_folder):
    if exists(source_folder + '/.git'):
        run('cd %s && git fetch' % (source_folder,))
    else:
        run('git clone %s %s' % (REPO_URL, source_folder))
    current_commit = local("git log -n 1 --format=%H", capture=True)
    run('cd %s && git reset --hard %s' % (source_folder, current_commit))


def _install_debian_packages():
    # TODO move debian dependencies to grd
    DEB_PACKAGES = [
        'python3', 'python3-pip', 'python3-psycopg2',
        'postgresql', 'postgresql-client', 'postgresql-contrib',
        'postgresql-9.4-postgis-2.1',
    ]
    
    run(
        'sudo apt-get update;'
        'sudo apt-get install %s;' % ' '.join(DEB_PACKAGES)
    )


def _install_postgres_extensions():
    # TODO: initialize database (if doesn't exists)
    # install extension (must be superuser to create it).
    # Include extension in the default template (template1)?
    # http://stackoverflow.com/a/11584751/1538221
    run(
        "sudo -u postgres "
        "psql -d template1 -c 'CREATE EXTENSION IF NOT EXISTS hstore;'"
        "psql -d template1 -c 'CREATE EXTENSION IF NOT EXISTS postgis;'"
    )


def _update_settings(source_folder, site_name):
    settings_path = source_folder + '/ereuse/settings.py'
    #sed(settings_path, "DEBUG = True", "DEBUG = False")
    sed(settings_path,
        'ALLOWED_HOSTS =.+$',
        'ALLOWED_HOSTS = ["%s"]' % (site_name,)
    )
    secret_key_file = source_folder + '/ereuse/secret_key.py'
    if not exists(secret_key_file):
        chars = 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)'
        key = ''.join(random.SystemRandom().choice(chars) for _ in range(50))
        append(secret_key_file, "SECRET_KEY = '%s'" % (key,))
    append(settings_path, '\nfrom .secret_key import SECRET_KEY')


def _update_virtualenv(source_folder):
    virtualenv_folder = source_folder + '/../virtualenv'
    if not exists(virtualenv_folder + '/bin/pip'):
        run('virtualenv --python=python3 %s' % (virtualenv_folder,))
    
    # install ereuse-sandbox requirements
    # XXX keep until split sandbox & testing
    run('%s/bin/pip install -r %s/ereuse/requirements.txt' % (
            virtualenv_folder, source_folder
    ))
    
    run('%s/bin/pip install -r %s/ereuse/requirements_production.txt' % (
            virtualenv_folder, source_folder
    ))
    
    # install GRD requirements
    grd_folder = "%s/src/grd/grd/" % virtualenv_folder
    run('%s/bin/pip install -r %s/requirements.txt' % (
            virtualenv_folder, grd_folder
    ))


def _update_static_files(source_folder):
    run('cd %s && ../virtualenv/bin/python3 manage.py collectstatic --noinput' % ( # 1
        source_folder,
    ))


def _update_database(source_folder):
    run('cd %s && ../virtualenv/bin/python3 manage.py migrate --noinput' % (
        source_folder,
    ))


def _reload_services():
    run('sudo service apache2 reload')


def deploy():
    site_folder = '/home/ereuse/sites/%s' % env.host
    source_folder = site_folder + '/source'
    _create_directory_structure_if_necessary(site_folder)
    _get_latest_source(source_folder)
    _update_settings(source_folder, env.host)
    _update_virtualenv(source_folder)
    _update_static_files(source_folder)
    _update_database(source_folder)
    _reload_services()

def first_deploy():
    # TODO see ~/INSTALL
    # It requires superuser privileges
    _install_debian_packages()
    _install_postgres_extensions()


def load_initial_data():
    # TODO run script that populates DB with initial data
    raise Exception("Not implemented yet")
