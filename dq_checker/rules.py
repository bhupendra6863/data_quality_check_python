from .base_rule import BaseRule
import re

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
        column = self.config.get('columns')
        min_val = self.config.get('min')
        max_val = self.config.get('max')
        out_of_range = df[(df[column] < min_val) | (df[column] > max_val)]
        return out_of_range

class StartsWithRule(BaseRule):
    def validate(self, df):
        column = self.config.get('columns')
        prefix = self.config.get('prefix')
        if column and prefix:
            not_matching = df[~df[column].astype(str).str.startswith(prefix)]
            return not_matching
        return df.iloc[0:0]  # Return empty DataFrame if config is missing

class RegexCheckRule(BaseRule):
    def validate(self, df):
        column = self.config.get('column')
        pattern = self.config.get('pattern')
        if column and pattern:
            not_matching = df[~df[column].astype(str).str.match(pattern)]
            return not_matching
        return df.iloc[0:0]  # Return empty DataFrame if config is missing

class RegexCheckEmailRule(BaseRule):
    def validate(self, df):
        column = self.config.get('column')
        pattern = self.config.get('pattern')
        if column and pattern:
            not_matching = df[~df[column].astype(str).str.match(pattern)]
            return not_matching
        return df.iloc[0:0]

class RegexCheckSignupDateRule(BaseRule):
    def validate(self, df):
        column = self.config.get('column')
        pattern = self.config.get('pattern')
        if column and pattern:
            not_matching = df[~df[column].astype(str).str.match(pattern)]
            return not_matching
        return df.iloc[0:0]
