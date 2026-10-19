# FL-07: Internship Assignment Assistant — Build Log

## 1. Project Overview
**Project:** Internship Assignment Assistant  
**Language:** Python  
**Editor:** Visual Studio Code  
**Data source:** Local text file (`assignment.txt`)

## 2. Development Progress
- Created the project folder.
- Created `main.py` to implement the assistant.
- Created `assignment.txt` as the local assignment data source.
- Implemented file-existence checking.
- Implemented assignment display.
- Added a checklist of required deliverables.
- Added a recommended next action.

## 3. Initial Test
**Test:** Run the assistant with `assignment.txt` available.  
**Expected result:** Assignment details and deliverables checklist appear in the terminal.  
**Observed result:** The assignment details were displayed successfully.

## 4. Pending Tests
- Verify the deliverables checklist output.
- Test behavior when `assignment.txt` is missing.
- Record the final test results after testing.

## 5. Limitations
- The current version reads a local text file.
- The checklist is predefined and does not yet automatically extract deliverables from arbitrary assignment text.
- The official FL-07 requirements must be checked before final submission.

## ## 6. Test Results

### Test 1: Assignment File Available
- **Expected:** Assignment details and checklist should appear.
- **Result:** Passed. Assignment details were displayed in the terminal.

### Test 2: Assignment File Missing
- **Expected:** The program should show an error message without crashing.
- **Result:** Passed. The program displayed `ERROR: assignment.txt was not found.`

### Test 3: File Restored
- **Expected:** The program should read the assignment file again.
- **Result:** Run `py main.py` after restoring `assignment.txt` and update this result after verifying.

## 7. Final Status
**Status:** Initial implementation and missing-file test completed.  
**Pending:** Verify the restored-file run, compare the project with the official FL-07 requirements, and prepare the final submission.
