factory
=======

factory is a Tool to create and manage Docker Machines.

Installation
------------

Either pull the automatically updated [Docker](http://docker.com/) image:

    $ docker pull prologic/factory

Or install from the development repository:

    $ git clone https://github.com/prologic/factory.git
    $ cd factory
    $ pip install -r requirements.txt

Usage
-----

    $ factory up

Configuration
-------------

    machines:
        dev:
          - driver=virtualbox

     services:
         hello:
           $machine: dev
           image: prologic/hello
