import os
import tempfile
import pandas as pd
import yaml
from dq_checker.checker import DataQualityChecker

def test_data_quality_checker_end_to_end():
    # Create a temporary CSV file
    df = pd.DataFrame({
        'id': [1, 2, 2, 4],
        'name': ['Alice', None, 'Bob', 'Charlie'],
        'age': [25, 30, 30, 40],
        'email': ['alice@example.com', 'bob@example.com', 'bob@example.com', 'notanemail'],
        'signup_date': ['2021-01-01', '2021-02-01', '2021-02-01', '2021/03/01']
    })
    with tempfile.NamedTemporaryFile(mode='w', suffix='.csv', delete=False) as csvfile:
        df.to_csv(csvfile.name, index=False)
        data_path = csvfile.name
    # Create a temporary YAML rules file
    rules = [
        {'type': 'null_check', 'columns': ['name']},
        {'type': 'duplicate_check', 'columns': ['id']},
        {'type': 'range_check', 'columns': 'age', 'min': 20, 'max': 35},
        {'type': 'starts_with', 'columns': 'email', 'prefix': 'alice'},
        {'type': 'regex_check_email', 'column': 'email', 'pattern': r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\\.[A-Za-z]{2,}$'},
        {'type': 'regex_check_signup_date', 'column': 'signup_date', 'pattern': r'^\\d{4}-\\d{2}-\\d{2}$'}
    ]
    rules_yaml = {'rules': rules}
    with tempfile.NamedTemporaryFile(mode='w', suffix='.yaml', delete=False) as yamlfile:
        yaml.dump(rules_yaml, yamlfile)
        rules_path = yamlfile.name
    # Run the checker
    dq = DataQualityChecker(data_path, rules_path)
    results = dq.check()
    # Clean up temp files
    os.remove(data_path)
    os.remove(rules_path)
    # Assert that all rule types are present in results
    assert 'null_check' in results
    assert 'duplicate_check' in results
    assert 'range_check' in results
    assert 'starts_with' in results
    assert 'regex_check_email' in results
    assert 'regex_check_signup_date' in results
    # Assert at least one result is not empty
    assert any(isinstance(val, pd.DataFrame) and not val.empty for val in results.values())
