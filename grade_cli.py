from grade_manager import GradeBook


def run_menu():
    book = GradeBook()


    while True:
        print("\n===STUDENT GRADE BOOK ===")
        print("1. Add Student")
        print("2. Add Subjects")
        print("3. Give Mark")
        print("4. Show Ranking")
        print("5. Delete Student")
        print("6. Exit")

        opt = input("Option (1-6). ").strip()

        if opt =="1":
            sid = input("ID: ") 
            nm = input("Name: ")
            em = input("Email: ")
            sb = input("Subjects (comma separated): ")
            done, msg = book.add_new_students(sid, nm, em, sb)
            print(msg)

        elif opt == "2":
            sid = input("ID: ") 
            sb = input("Subjects (comma separated): ") 
            done, msg = book.add_more_subs(sid,sb)
            print(msg)

        elif opt == "3":
            sid = input("ID: ")
            sb = input("Subject: ")
            val = input("Mark (0-100): ")
            done, msg = book.give_mark(sid, sb, val)
            print(msg) 

        elif opt == "4":
            q = input("Search (or press Enter): ")
            ordered = book.search_and_rank(q)
            print("\n--- RANKING ---")
            if not ordered:
                print("No records found.")
            else:
                pos = 1
                for st in ordered: 
                    print(f"\n{pos}. [{st.st_id}] {st.sname} ({st.mail})")
                    print(f"   Avg: {st.calc_avg()}")
                    for line in st.sub_list_text().split("\n"):
                        print(f"  - {line}")
                    pos = pos + 1

        elif opt == "5":
            sid = input("ID to delete: ")
            done, msg = book.remove_student(sid)
            print(msg)

        elif opt == "6":
            print("Exit.")
            break
        else:
            print("Invalid option.")


if __name__ == "__main__":
    run_menu()