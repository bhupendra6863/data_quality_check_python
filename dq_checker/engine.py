import pandas as pd
import yaml
from .rules import DuplicateCheckRule, NullCheckRule, RangeCheckRule, StartsWithRule, RegexCheckEmailRule, RegexCheckSignupDateRule

class DQEngine:
    RULE_MAPPING = {
        'duplicate_check': DuplicateCheckRule,
        'null_check': NullCheckRule,
        'range_check': RangeCheckRule,
        'starts_with': StartsWithRule,
        'regex_check_email': RegexCheckEmailRule,
        'regex_check_signup_date': RegexCheckSignupDateRule,
    }

    def __init__(self, data_path, rules_path):
        self.data_path = data_path
        self.rules_path = rules_path
        try:
            self.df = pd.read_csv(data_path)
        except Exception as e:
            raise RuntimeError(f"Error loading data file '{data_path}': {e}")
        try:
            with open(rules_path, 'r') as f:
                rules_yaml = yaml.safe_load(f)
                self.rules = rules_yaml['rules']
        except Exception as e:
            raise RuntimeError(f"Error loading rules file '{rules_path}': {e}")

    def run(self):
        results = {}
        for rule_cfg in self.rules:
            rule_type = rule_cfg['type']
            rule_cls = self.RULE_MAPPING.get(rule_type)
            try:
                if rule_cls:
                    rule = rule_cls(rule_cfg)
                    results[rule_type] = rule.validate(self.df)
                else:
                    results[rule_type] = f"Unknown rule type: {rule_type}"
            except Exception as e:
                results[rule_type] = f"Error in rule '{rule_type}': {e}"
        return results
