from __future__ import print_function

from traceback import format_exc


from sh import docker_machine

from domains.api import Domains


from .utils import process


class Services(object):

    def __init__(self, config):
        self.config = config


class Factory(object):

    def __init__(self, config):
        self.config = process(config)

        self.domains = Domains(config["domains"]) if "domains" in config else None
        self.services = Services(config["services"]) if "services" in config else None

    def _ip(self, machine):
        return docker_machine.ip(machine).strip()

    def _machines_up(self):
        for name, config in self.config["machines"].items():
            try:
                print("Creating machine: {} ... ".format(name), end="")
                config = {k: (v is None and True) or v for k, v in config.items()}
                docker_machine.create(name, **config)
                print("OK")
            except Exception as e:
                print("ERR\nERROR: {0}\n{1}".format(e, format_exc()))

    def _domains_up(self):
        if self.domains is None:
            return

        context = {
            "machines": {k: {"ip": self._ip(k)} for k in self.config["machines"]}
        }

        self.domains.sync(context)

    def _services_up(self):
        pass

    def _machines_rm(self, machines):
        machines = machines or self.config["machines"]
        for machine in machines:
            try:
                print("Removing machine: {} ... ".format(machine), end="")
                docker_machine.rm(machine)
                print("OK")
            except Exception as e:
                print("ERR\nERROR: {0}\n{1}".format(e, format_exc()))

    def _domains_rm(self):
        if self.domains is None:
            return

        self.domains.delete()

    def ls(self):
        print(docker_machine.ls())

    def up(self):
        self._machines_up()
        self._domains_up()
        self._services_up()

    def stop(self, machines):
        machines = machines or self.config["machines"]
        for machine in machines:
            try:
                print("Stopping machine: {} ... ".format(machine), end="")
                docker_machine.stop(machine)
                print("OK")
            except Exception as e:
                print("ERR\nERROR: {0}\n{1}".format(e, format_exc()))

    def rm(self, machines):
        self._machines_rm(machines)
        self._domains_rm()

    def env(self, machine):
        print(docker_machine.env(machine).strip())

    def ip(self, machine):
        print(self._ip(machine))
