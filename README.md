# LeetCode Contest Question Scraper

## Overview
This script fetches contest questions from LeetCode based on the latest contest numbers provided by the user. It allows users to extract questions of a specific mark value and saves the data in an Excel file.

## Features
- Fetches recent Weekly and Biweekly LeetCode contest questions.
- Filters questions based on the provided mark value.
- Saves the extracted questions in an Excel file.

## Requirements
- Python 3.x
- Required libraries:
  - `requests`
  - `pandas`

You can install the required dependencies using:
```sh
pip install requests pandas
```

## Usage
Run the script and provide inputs when prompted:
```sh
python script.py
```

### Inputs:
1. **Latest Weekly Contest Number** (e.g., 436)
2. **Latest Biweekly Contest Number** (e.g., 122)
3. **Mark Value of Questions** (e.g., 6)

You can choose to provide only Weekly or Biweekly contest numbers. If no input is given for a contest type, it will be skipped.

### Output:
- The script generates an Excel file named `leetcode_<mark>_mark_questions.xlsx` containing contest name, question title, and question ID.

## Example Run
```
Enter the latest Weekly Contest number: 436
Enter the latest Biweekly Contest number: 122
Enter the mark of the questions to extract: 6
Saved to leetcode_6_mark_questions.xlsx
```

## Error Handling
- If LeetCode fails to respond, the script prints an error message but continues execution.
- If no contest numbers or mark value is provided, the script exits gracefully.
- If no questions match the specified mark value, an appropriate message is displayed.

## Notes
- The script retrieves the last 20 Weekly and 10 Biweekly contests based on the given inputs.
- The User-Agent header is set to avoid request blocking by LeetCode.
- Ensure a stable internet connection while running the script.


