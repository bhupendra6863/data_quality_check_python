import pytest
import pandas as pd
from dq_checker.engine import DQEngine
from dq_checker.rules import NullCheckRule, DuplicateCheckRule, RangeCheckRule, StartsWithRule, RegexCheckEmailRule, RegexCheckSignupDateRule

# Sample DataFrame for testing
def sample_df():
    return pd.DataFrame({
        'id': [1, 2, 2, 4],
        'name': ['Alice', None, 'Bob', 'Charlie'],
        'age': [25, 30, 30, 40],
        'email': ['alice@example.com', 'bob@example.com', 'bob@example.com', 'notanemail'],
        'signup_date': ['2021-01-01', '2021-02-01', '2021-02-01', '2021/03/01']
    })

def test_null_check():
    df = sample_df()
    rule = NullCheckRule({'type': 'null_check', 'columns': ['name']})
    result = rule.validate(df)
    assert not result.empty
    assert result.iloc[0]['id'] == 2

def test_duplicate_check():
    df = sample_df()
    rule = DuplicateCheckRule({'type': 'duplicate_check', 'columns': ['id']})
    result = rule.validate(df)
    assert not result.empty
    assert 2 in result['id'].values

def test_range_check():
    df = sample_df()
    rule = RangeCheckRule({'type': 'range_check', 'columns': 'age', 'min': 20, 'max': 35})
    result = rule.validate(df)
    # Only Charlie (age 40) should be out of range
    assert not result.empty
    assert 40 in result['age'].values
    rule2 = RangeCheckRule({'type': 'range_check', 'columns': 'age', 'min': 26, 'max': 35})
    result2 = rule2.validate(df)
    assert not result2.empty

def test_starts_with():
    df = sample_df()
    rule = StartsWithRule({'type': 'starts_with', 'columns': 'email', 'prefix': 'alice'})
    result = rule.validate(df)
    assert not result.empty
    # All emails in result should NOT start with 'alice'
    assert all(not email.startswith('alice') for email in result['email'])

def test_regex_check_email():
    df = sample_df()
    # Use a simple email regex pattern for the test
    pattern = r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"
    rule = RegexCheckEmailRule({'type': 'regex_check_email', 'column': 'email', 'pattern': pattern})
    result = rule.validate(df)
    assert not result.empty
    assert 'notanemail' in result['email'].values

def test_regex_check_signup_date():
    df = sample_df()
    # Use a simple date regex pattern for the test (YYYY-MM-DD)
    pattern = r"^\\d{4}-\\d{2}-\\d{2}$"
    rule = RegexCheckSignupDateRule({'type': 'regex_check_signup_date', 'column': 'signup_date', 'pattern': pattern})
    result = rule.validate(df)
    assert not result.empty
    assert '2021/03/01' in result['signup_date'].values
