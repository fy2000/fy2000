# -*- coding: utf-8 -*-
import configparser


class ConfigSetting:
    def __init__(self, inifile: str):
        cfgp = configparser.ConfigParser()
        cfgp.read(inifile)
        self.filedir = cfgp.get(configparser.DEFAULTSECT, 'filedir')
        self.backdir = cfgp.get(configparser.DEFAULTSECT, 'backdir')
        self.iszip = cfgp.getboolean(configparser.DEFAULTSECT, 'iszip')
        self.isdel = cfgp.getboolean(configparser.DEFAULTSECT, 'isdel')
        self.charextlist = cfgp.get(configparser.DEFAULTSECT, 'charext').split(",")

    def is_cfg_available(self):
        if len(self.filedir) == 0 or self.filedir is None:
            return False
        if not self.isdel and (len(self.backdir) == 0 or self.filedir is None):
            return False
        return True
