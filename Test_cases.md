# Test Cases

## 1. Load CSV and Duplicate Student ID Check
- **Action:** Run the CLI or GUI with `student_gradebook.csv` loaded and try existing student ID(`S102`)
- **Expected Result:** Existing records load propperly, and adding a duplicate ID is blocked with a message that the ID already exists.

## 2. Add Students, Marks, and Ranking Order
- **Action:** Add a new student (`S103`), add his subject, enter his marks(0, 100), and view his ranking.
- **Expected Results:** As expected student name, id, subject and marks saved, average is calculated accurately, and student is ordered from highest to lowest. 

## 3. Invalid or Out-of-Range Input Check 
-**Action:** Enter marks outside the 0 and 100, for example, -67 or 110 or invalid input. 
-**Expected Results:** invalid input is rejected.

## 4. GUI Table and Status Display
- **Action:** Open grade_gui.py with student records present. Put students name, ID, email, subjects and marks(0, 100). 
- **Expected Result:** Shows students IDs, name, email, subjects/marks, averages, and statuses (Distinction, Pass, Fail) clearly in ranking order.

## 5. Delete Student and Keep CSV Clean
- **Action:** Delete temporary test students after testing.
- **Expected Result:** The temporary record is removed cleanly so student_gradebook.csv stays clean.