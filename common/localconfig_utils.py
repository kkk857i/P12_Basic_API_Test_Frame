
import os
import configparser

current_path=os.path.dirname(__file__)
config_path=os.path.join(os.path.dirname(__file__), '..','config/config.ini')

class LocalconfigUtils():

    def __init__(self,config_path=config_path):
        self.cfg=configparser.ConfigParser()
        self.cfg.read(config_path,encoding='utf-8')

    @property   #把方法边为属性方法
    def URL(self):
        url_value=self.cfg.get('default','URL')
        return url_value

    @property
    def LOG_PATH(self):
        log_path_value = self.cfg.get('path','LOG_PATH')
        return log_path_value

    @property
    def REPORT_PATH(self):
        report_path_value = self.cfg.get('path', 'REPORT_PATH')
        return report_path_value

    @property
    def LOG_LEVEL(self):
        log_level_value = int(self.cfg.get('log','LOG_LEVEL'))
        return log_level_value

    @property
    def APPID(self):
        appid_value = (self.cfg.get('default','APPID'))
        return appid_value

    @property
    def SECRET(self):
        secret_value = (self.cfg.get('default','SECRET'))
        return secret_value

local_config=LocalconfigUtils()

if __name__=='__main__':
    print(local_config.SECRET)
