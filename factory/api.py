from __future__ import print_function


from sh import docker_machine


class Factory(object):

    def __init__(self, config):
        self.config = config

    def ls(self):
        print(docker_machine.ls())

    def up(self, file, detached=False):
        for name, config in self.config.machines.items():
            print("Creating machine: {}".format(name))
            print(config)
            docker_machine.create(name, **config)

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
