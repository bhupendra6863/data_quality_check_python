from .base_rule import BaseRule
import re

class DuplicateCheckRule(BaseRule):
    def validate(self, df):
        try:
            columns = self.config.get('columns', [])
            duplicates = df[df.duplicated(subset=columns)]
            return duplicates
        except Exception as e:
            return f"DuplicateCheckRule error: {e}"

class NullCheckRule(BaseRule):
    def validate(self, df):
        try:
            columns = self.config.get('columns', [])
            nulls = df[df[columns].isnull().any(axis=1)]
            return nulls
        except Exception as e:
            return f"NullCheckRule error: {e}"

class RangeCheckRule(BaseRule):
    def validate(self, df):
        try:
            column = self.config.get('columns')
            min_val = self.config.get('min')
            max_val = self.config.get('max')
            out_of_range = df[(df[column] < min_val) | (df[column] > max_val)]
            return out_of_range
        except Exception as e:
            return f"RangeCheckRule error: {e}"

class StartsWithRule(BaseRule):
    def validate(self, df):
        try:
            column = self.config.get('columns')
            prefix = self.config.get('prefix')
            if column and prefix:
                not_matching = df[~df[column].astype(str).str.startswith(prefix)]
                return not_matching
            return df.iloc[0:0]  # Return empty DataFrame if config is missing
        except Exception as e:
            return f"StartsWithRule error: {e}"

class RegexCheckRule(BaseRule):
    def validate(self, df):
        try:
            column = self.config.get('column')
            pattern = self.config.get('pattern')
            if column and pattern:
                not_matching = df[~df[column].astype(str).str.match(pattern)]
                return not_matching
            return df.iloc[0:0]  # Return empty DataFrame if config is missing
        except Exception as e:
            return f"RegexCheckRule error: {e}"

class RegexCheckEmailRule(BaseRule):
    def validate(self, df):
        try:
            column = self.config.get('column')
            pattern = self.config.get('pattern')
            if column and pattern:
                not_matching = df[~df[column].astype(str).str.match(pattern)]
                return not_matching
            return df.iloc[0:0]
        except Exception as e:
            return f"RegexCheckEmailRule error: {e}"

class RegexCheckSignupDateRule(BaseRule):
    def validate(self, df):
        try:
            column = self.config.get('column')
            pattern = self.config.get('pattern')
            if column and pattern:
                not_matching = df[~df[column].astype(str).str.match(pattern)]
                return not_matching
            return df.iloc[0:0]
        except Exception as e:
            return f"RegexCheckSignupDateRule error: {e}"
