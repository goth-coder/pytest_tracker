import re
import os
import sys

def extract_passed_tests(filename):
    """Extracts passed test names from a pytest -rp output file."""
    with open(filename, "r", encoding="UTF-16") as file:
        passed_tests = [
            re.sub(r"\[.*\]", "", line.strip().replace("PASSED ", ""))
            for line in file if line.startswith("PASSED ")
        ]
    return list(dict.fromkeys(passed_tests))  # Preserve order and remove duplicates

def compare_test_results(directory):
    """Compares two pytest output files in a given directory to find tests that stopped passing."""
    before_file = os.path.join(directory, "pytest_output_before.txt")
    after_file = os.path.join(directory, "pytest_output_after.txt")

    if not os.path.exists(before_file) or not os.path.exists(after_file):
        print("Error: One or both pytest output files are missing in the specified directory.")
        sys.exit(1)

    before_tests = set(extract_passed_tests(before_file))
    after_tests = set(extract_passed_tests(after_file))

    missing_tests = before_tests - after_tests

    if missing_tests:
        print("Tests that passed before but not after the golden patch:")
        for test in sorted(missing_tests):
            print(test)
    else:
        print("All tests that passed before still pass after the golden patch.")

    return missing_tests, extract_passed_tests(after_file)

def main():
    if len(sys.argv) != 2:
        print("Usage: python -m tests_selector <directory>")
        sys.exit(1)

    directory = sys.argv[1]
    missing_tests, passed_tests_after = compare_test_results(directory)

    # Save missing tests to a file
    with open(os.path.join(directory, "broken_tests.txt"), "w", encoding="utf-8") as output_file:
        output_file.write("\n".join(missing_tests))

    # Save all passed tests after golden patch
    with open(os.path.join(directory, "passed_tests.txt"), "w", encoding="utf-8") as output_file:
        output_file.write("\n".join(passed_tests_after))

    print("\nResults have been written to broken_tests.txt and passed_tests.txt in", directory)

if __name__ == "__main__":
    main()
