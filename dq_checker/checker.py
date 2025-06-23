from .engine import DQEngine

class DataQualityChecker:
    def __init__(self, data_path, rules_path):
        self.engine = DQEngine(data_path, rules_path)

    def check(self):
        return self.engine.run()
