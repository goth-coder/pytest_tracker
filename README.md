# Pytest Test Comparison Script

This script compares the results of two pytest runs before and after applying a patch. It identifies tests that passed before but failed after the patch.

## Usage

### Step 1: Run pytest before applying the patch
Execute the following command to store the test results before applying the patch:

```sh
pytest -rp --continue-on-collection-errors > pytest_output_before.txt
```

### Step 2: Apply the patch
Apply your changes to the codebase.

### Step 3: Run pytest again after the patch
Run the following command to store the test results after applying the patch:

```sh
pytest -rp --continue-on-collection-errors > pytest_output_after.txt
```

### Step 4: Run the test comparison script
Execute the script by specifying the directory where the test result files are located:

```sh
python tests_selector.py <directory>
```

For example:

```sh
python tests_selector.py seaborn
```

## Output

- `broken_tests.txt`: Lists tests that passed before but failed after applying the patch.
- `passed_tests.txt`: Lists tests that passed after applying the patch.

## Requirements
- Python 3
- `pytest`

## License
This project is licensed under the MIT License.

