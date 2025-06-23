from dq_checker.checker import DataQualityChecker

if __name__ == "__main__":
    data_path = "data/test_data.csv"
    rules_path = "rules/rules.yaml"
    dq = DataQualityChecker(data_path, rules_path)
    results = dq.check()
    for check, df in results.items():
        print(f"\n{check.upper()}:")
        print(df if not df.empty else "No issues found.")
