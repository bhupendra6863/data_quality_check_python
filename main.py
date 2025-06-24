import logging
from dq_checker.checker import DataQualityChecker

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('dq_checker.log', mode='a'),
        logging.StreamHandler()
    ]
)

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
            logging.info(f"\n{check_name}:")
            if not df.empty:
                logging.info(f"{df}")
            else:
                logging.info("No issues found.")
            logging.info("\n" + "-"*40 + "\n")  # Add a line break and separator after each rule
    except Exception as e:
        logging.error(f"An error occurred: {e}", exc_info=True)
