#: encoding: utf-8
import bottle
import cloudstorage
import mistune
from google.appengine.api import app_identity


app = bottle.default_app()
folder = '/{}/utf-8-test/'.format(app_identity.get_default_gcs_bucket_name())


@app.route('/')
def home():
    with open('README.md') as fh:
        return mistune.markdown(fh.read())


@app.route('/list')
def list_files():
    contents = cloudstorage.listbucket(folder)

    return {'contents': [o.__dict__ for o in contents]}


@app.route('/create-ascii')
def create_ascii():
    return _create_file('ascii-filename')


@app.route('/create-utf-8')
def create_utf8():
    return _create_file(u'Señor'.encode('utf-8'))


def _create_file(filename):
    dest = folder + filename

    with cloudstorage.open(dest, 'w') as fh:
        fh.write('foo bar baz')

    return bottle.redirect('/list')


@app.route('/delete')
def delete_file():
    # GCS helpfully decodes UTF-8 for you, is a bit weird because it won't
    # accept unicode when creating an object.
    for stat in cloudstorage.listbucket(folder):
        target = stat.filename.encode('utf-8')
        cloudstorage.delete(target)

    return bottle.redirect('/list')
