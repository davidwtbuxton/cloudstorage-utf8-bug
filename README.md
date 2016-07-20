Test for Google Cloud Storage and UTF-8 encoding
================================================

The Google Cloud Storage docs say [object names can be UTF-8 encoded strings][names], which is true, and works great when deployed to App Engine.

But the same code fails when running locally with the dev server. Tested with SDK 1.9.38.


Testing
-------

This app demonstrates the bug.

- [/list](/list) returns a JSON response showing the contents of a bucket.
- [/create-ascii](/create-ascii) creates a new file in the bucket, named 'ascii-filename'.
- [/create-utf-8](/create-utf-8) creates a new file in the bucket, named 'Señor' using UTF-8 encoding.
- [/delete](/delete) deletes the bucket contents.

On App Engine, you can create a file with non-ASCII characters in the filename. On the local development server, you get a 500 response.

[Test it for yourself on App Engine][appspot].


Setup
-----

[Source code][github] is on GitHub.

Install requirements:

    pip install --target . bottle==0.12.9 GoogleAppEngineCloudStorageClient==1.9.22.1
    pip install --target . --no-binary :all: mistune==0.7.3

Run the development server:

    dev_appserver .

Go to http://localhost:8080 in your browser.


Updated 20 July 2016


[names]: https://cloud.google.com/storage/docs/naming#objectnames
[github]: https://github.com/davidwtbuxton/cloudstorage-utf8-bug
[appspot]: https://cloudstorage-utf8-bug-dot-davidwtbuxton-test.appspot.com/