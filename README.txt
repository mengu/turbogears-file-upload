This is a simple example project for TurboGears users to have an idea
about how to implement a file upload system with TurboGears 2.0.3

This file is for you to describe the fileupload application. Typically
you would include information such as the information below:

Installation and Setup
======================

Install ``fileupload`` using the setup.py script::

    $ cd fileupload
    $ python setup.py install

Create the project database for any model classes defined::

    $ paster setup-app development.ini

Start the paste http server::

    $ paster serve development.ini

While developing you may want the server to reload after changes in package files (or its dependencies) are saved. This can be achieved easily by adding the --reload option::

    $ paster serve --reload development.ini

Then you are ready to go.

