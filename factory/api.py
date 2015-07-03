from __future__ import print_function


from sh import docker_machine
from progress.spinner import Spinner


class Factory(object):

    def __init__(self, config):
        self.config = config

    def ls(self):
        print(docker_machine.ls())

    def up(self, file, detached=False):
        for name, config in self.config.machines.items():
            config = {k: (v is None and True) or v for k, v in config.items()}
            progress = Spinner("Creating machine {}: ".format(name))
            for _ in docker_machine.create(name, _iter_noblock=True, **config):
                progress.next()
            progress.finish()

    def stop(self, machines):
        machines = machines or self.config.machines
        for machine in machines:
            print("Stopping machine: {}".format(machine))
            docker_machine.stop(machine)

    def rm(self, machines):
        machines = machines or self.config.machines
        for machine in machines:
            print("Removing machine: {}".format(machine))
            docker_machine.rm(machine)

    def env(self, machine):
        print(docker_machine.env(machine).strip())

    def ip(self, machine):
        print(docker_machine.ip(machine).strip())
