from dq_checker.checker import DataQualityChecker

if __name__ == "__main__":
    data_path = "data/test_data.csv"
    rules_path = "rules/rules.yaml"
    try:
        dq = DataQualityChecker(data_path, rules_path)
        results = dq.check()
        for check, df in results.items():
            if isinstance(check, tuple):
                check_name = f"{check[0].upper()} ({check[1]})"
            else:
                check_name = check.upper()
            print(f"\n{check_name}:")
            print(df if not df.empty else "No issues found.")
    except Exception as e:
        print(f"An error occurred: {e}")
