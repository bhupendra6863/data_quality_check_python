class BaseRule:
    def __init__(self, config):
        self.config = config

    def validate(self, df):
        raise NotImplementedError("Each rule must implement the validate method.")
