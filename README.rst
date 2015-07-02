factory
=======

factory is a Tool to create and manage Docker Machines.

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

::
    
    machines:
        dev:
          driver=virtualbox

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
