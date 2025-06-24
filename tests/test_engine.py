import pandas as pd
import pytest
from dq_checker.engine import DQEngine

# Sample rules config for engine
RULES_CONFIG = [
    {'type': 'null_check', 'columns': ['name']},
    {'type': 'duplicate_check', 'columns': ['id']},
    {'type': 'range_check', 'columns': 'age', 'min': 20, 'max': 35},
    {'type': 'starts_with', 'columns': 'email', 'prefix': 'alice'},
    {'type': 'regex_check_email', 'column': 'email', 'pattern': r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\\.[A-Za-z]{2,}$'},
    {'type': 'regex_check_signup_date', 'column': 'signup_date', 'pattern': r'^\\d{4}-\\d{2}-\\d{2}$'}
]

def sample_df():
    return pd.DataFrame({
        'id': [1, 2, 2, 4],
        'name': ['Alice', None, 'Bob', 'Charlie'],
        'age': [25, 30, 30, 40],
        'email': ['alice@example.com', 'bob@example.com', 'bob@example.com', 'notanemail'],
        'signup_date': ['2021-01-01', '2021-02-01', '2021-02-01', '2021/03/01']
    })

def test_engine_applies_all_rules():
    df = sample_df()
    engine = DQEngine(df=df, rules=RULES_CONFIG)
    results = engine.run()
    # Check that all expected checks are present in results (use lowercase keys)
    assert 'null_check' in results
    assert 'duplicate_check' in results
    assert 'range_check' in results
    assert 'starts_with' in results
    assert 'regex_check_email' in results
    assert 'regex_check_signup_date' in results
    # Check that at least one result is not empty (indicating a failed check)
    assert any(isinstance(val, pd.DataFrame) and not val.empty for val in results.values())
