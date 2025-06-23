from .base_rule import BaseRule

class DuplicateCheckRule(BaseRule):
    def validate(self, df):
        columns = self.config.get('columns', [])
        duplicates = df[df.duplicated(subset=columns)]
        return duplicates

class NullCheckRule(BaseRule):
    def validate(self, df):
        columns = self.config.get('columns', [])
        nulls = df[df[columns].isnull().any(axis=1)]
        return nulls

class RangeCheckRule(BaseRule):
    def validate(self, df):
        column = self.config.get('column')
        min_val = self.config.get('min')
        max_val = self.config.get('max')
        out_of_range = df[(df[column] < min_val) | (df[column] > max_val)]
        return out_of_range

class StartsWithRule(BaseRule):
    def validate(self, df):
        column = self.config.get('column')
        prefix = self.config.get('prefix')
        if column and prefix:
            not_matching = df[~df[column].astype(str).str.startswith(prefix)]
            return not_matching
        return df.iloc[0:0]  # Return empty DataFrame if config is missing
