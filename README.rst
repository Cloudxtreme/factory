factory
=======

factory is a Tool to create and manage Docker Machines.

factory is MIT licensed.

.. image:: https://asciinema.org/a/23ujlplez9yyulmqojinw9ei4.png
   :target: https://asciinema.org/a/23ujlplez9yyulmqojinw9ei4

Quick Start
-----------

::
    
    $ git clone https://github.com/prologic/factory.git
    $ cd factory
    $ pip install -r requirements.txt

Usage
-----

::
    
    $ factory up

Configuration
-------------

Simple local virtualbox:

::
    
    machines:
      dev:
        driver=virtualbox

Simple digitalocean:

::
    
    $ export DIGITALOCEAN_ACCESS_TOKEN==...

::
    
    machines:
      dev:
        driver=digitalocean

A digitalocean swarm cluster:

::
    
    $ export DIGITALOCEAN_ACCESS_TOKEN==...

::

    machines:

      node1:
        driver: digitalocean
        swarm:
        swarm-master:
        swarm-discovery: token://...

      node2:
        driver: digitalocean
        swarm:
        swarm-discovery: token://...

Other Commands
--------------

::
  
    $ factory --help
    usage: factory [-h] [-v] [-f FILE] [--verbose] [Command] ...

    Tool for creating and managing Docker Machines

    optional arguments:
      -h, --help            show this help message and exit
      -v, --version         show program's version number and exit
      -f FILE, --file FILE  Specify an alternate factory file (default:
                            factory.yml)
      --verbose             Show more output (default: False)

    Commands:
      [Command]
        ls                  List all machines
        up                  Bring up all machines
        stop                Stop a machine or all machines
        rm                  Remove a machine or all machines
