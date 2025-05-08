# method vs @classmethod vs @staticmethod
# method - self, método de instância
# @classmethod - cls, método de classe
# @staticmethod - método estático (❌self, ❌cls)

def __init__(self, host='localhost'):
        self.host = host
        self.user = None
        self.password = None