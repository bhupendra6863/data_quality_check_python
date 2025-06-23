import pandas as pd
import yaml
from .rules import DuplicateCheckRule, NullCheckRule, RangeCheckRule, StartsWithRule

class DQEngine:
    RULE_MAPPING = {
        'duplicate_check': DuplicateCheckRule,
        'null_check': NullCheckRule,
        'range_check': RangeCheckRule,
        'starts_with': StartsWithRule,
    }

    def __init__(self, data_path, rules_path):
        self.data_path = data_path
        self.rules_path = rules_path
        self.df = pd.read_csv(data_path)
        with open(rules_path, 'r') as f:
            rules_yaml = yaml.safe_load(f)
            # Support both list and dict style YAML for backward compatibility
            if isinstance(rules_yaml, dict) and 'rules' in rules_yaml:
                self.rules = rules_yaml['rules']
            else:
                # Convert dict style to list of rules
                self.rules = [
                    {'type': k, **(v if isinstance(v, dict) else {})}
                    for k, v in rules_yaml.items()
                ]

    def run(self):
        results = {}
        for rule_cfg in self.rules:
            rule_type = rule_cfg['type']
            rule_cls = self.RULE_MAPPING.get(rule_type)
            if rule_cls:
                rule = rule_cls(rule_cfg)
                results[rule_type] = rule.validate(self.df)
            else:
                results[rule_type] = f"Unknown rule type: {rule_type}"
        return results
