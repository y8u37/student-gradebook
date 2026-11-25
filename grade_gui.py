import tkinter as tk
from tkinter import ttk, messagebox
from grade_manager import GradeBook


class MyGradeApp:
    def __init__(self, win):
        self.win = win
        self.win.title("Student Grade Book")
        self.win.geometry("1040x680")
        self.win.minsize(920, 620)
        self.win.configure(bg="#F4F6F9")

        self.book = GradeBook()
        self.setup_style()
        self.make_screen()
        self.show_rows()

    def setup_style(self):
        st = ttk.Style()
        if "clam" in st.theme_names():
            st.theme_use("clam")

        st.configure(
            "Treeview",
            font=("Segoe UI", 9),
            rowheight=68,
            background="#E3E8EF",
            foreground="#1F2937",
        )
        st.map(
            "Treeview",
            background=[("selected", "#DBEAFE")],
            foreground=[("selected", "#1E3A8A")],
        )

    def make_box(self, parent, width=28):
        return tk.Entry(
            parent,
            width=width,
            font=("Segoe UI", 9),
            bg="#FFFFFF",
            fg="#111827",
            relief="solid",
            bd=1,
        )

    def make_screen(self):
        status_bar = tk.Frame(self.win, bg="#E5E7EB", padx=14, pady=6)
        status_bar.pack(fill="x", side="bottom")

        self.msg_lbl = tk.Label(
            status_bar,
            text="Ready.",
            bg="#374151",
            fg="#FFFFFF",
            font=("Segoe UI", 9),
        )
        self.msg_lbl.pack(side="left")

        top_bar = tk.Frame(self.win, bg="#1E293B", padx=16, pady=12)
        top_bar.pack(fill="x")

        tk.Label(
            top_bar,
            text="Student Grade Book & Ranking",
            font=("Segoe UI", 15, "bold"),
            bg="#1E293B",
            fg="#FFFFFF",
        ).pack(side="left")

        self.count_lbl = tk.Label(
            top_bar,
            text="0 students",
            font=("Segoe UI", 9),
            bg="#1E293B",
            fg="#FFFFFF",
        )
        self.count_lbl.pack(side="right")

        forms_row = tk.Frame(self.win, bg="#F4F6F9", padx=14, pady=8)
        forms_row.pack(fill="x")

        st_box = tk.LabelFrame(
            forms_row,
            text="Register student",
            font=("Segoe UI", 9, "bold"),
            bg="#FFFFFF",
            fg="#1F2937",
            padx=12,
            pady=8,
        )
        st_box.pack(side="left", fill="both", expand=True, pady=(0, 7))

        reg_fields = [
            (0, "Student ID", "e_id"),
            (1, "Full Name", "e_name"),
            (2, "Email", "e_mail"),
            (3, "Subjects", "e_subjects"),
        ]
        for row, label_text, attr_name in reg_fields:
            tk.Label(
                st_box,
                text=label_text,
                bg="#FFFFFF",
                fg="#374151",
                font=("Segoe UI", 9),
            ).grid(row=row, column=0, sticky="w", pady=4)

            entry = self.make_box(st_box)
            entry.grid(row=row, column=1, pady=4, padx=(8, 0), sticky="ew", ipady=2)
            setattr(self, attr_name, entry)

        st_box.columnconfigure(1, weight=1)

        st_btns = tk.Frame(st_box, bg="#FFFFFF")
        st_btns.grid(row=4, column=0, columnspan=2, pady=(8, 0), sticky="ew")

        tk.Button(
            st_btns,
            text="Add Student",
            bg="#15803D",
            fg="#FFFFFF",
            font=("Segoe UI", 9, "bold"),
            relief="flat",
            padx=10,
            pady=5,
            cursor="hand2",
            command=self.on_add_student,
        ).pack(side="left", fill="x", expand=True, padx=(0, 4))

        tk.Button(
            st_btns,
            text="Clear",
            bg="#E5E7EB",
            fg="#1F2937",
            font=("Segoe UI", 9, "bold"),
            relief="flat",
            padx=10,
            pady=5,
            cursor="hand2",
            command=self.clear_reg_fields,
        ).pack(side="left", padx=(4, 0))

        mk_box = tk.LabelFrame(
            forms_row,
            text="Subjects & Marks",
            font= ("Segoe UI", 9, "bold"),
            bg="#FFFFFF",
                        fg="#1F2937",
                        padx=12,
                        pady=8,
        )

        mk_box.pack(side="left", fill="both", expand=True, padx=(7, 0))

        tk.Label(mk_box, text="Student ID", bg="#FFFFFF", fg="#374151", font=("Segoe UI", 9)).grid(
            row=0, column=0, sticky="w", pady=4)

        self.m_id = self.make_box(mk_box)
        self.m_id.grid(row=0, column=1, pady=4, padx=(8, 0), sticky="ew", ipady=2)

        tk.Label(mk_box, text="Subject", bg="#FFFFFF", fg="#374151", font=("Segoe UI", 9)).grid(
            row=1, column=0, sticky="w", pady=4)
        self.m_sub = self.make_box(mk_box)
        self.m_sub.grid(row=1, column=1, pady=4, padx=(8, 0), sticky="ew", ipady=2)

        tk.Label(mk_box, text="Mark (0-100)", bg="#FFFFFF", fg="#374151", font=("Segoe UI", 9)).grid(
            row=2, column=0, sticky="w", pady=4)
        self.m_val = self.make_box(mk_box)
        self.m_val.grid(row=2, column=1, pady=4, padx=(8, 0), sticky="ew", ipady=2)
        self.m_val.bind("<Return>", lambda event: self.on_save_mark())

        mk_box.columnconfigure(1, weight=1)

        mk_btns = tk.Frame(mk_box, bg="#FFFFFF")
        mk_btns.grid(row=3, column=0, columnspan=2, pady=(8, 0), sticky="ew")


        tk.Button(
            mk_btns,
            text="Save Mark",
            bg="#1D4ED8",
            fg="#FFFFFF",
            font=("Segoe UI", 9, "bold"),
            relief="flat",
            padx=10,
            pady=5,
            cursor="hand2",
            command=self.on_save_mark,
        ).pack(side="left", fill="x", expand=True, padx=(0, 4))

        tk.Button(
            mk_btns,
            text="Add Subject",
            bg="#475569",
            fg="#FFFFFF",
            font=("Segoe UI", 9, "bold"),
            relief="flat",
            padx=10,
            pady=5,
            cursor="hand2",
            command=self.on_add_sub,
        ).pack(side="left", fill="x", expand=True, padx=(4, 0))
    
        tool_row = tk.Frame(self.win, bg="#F4F6F9", padx=14, pady=4)
        tool_row.pack(fill="x")


        tk.Label(
            tool_row,
            text="Search:",
            bg="#F4F6F9",
            fg="#1F2937",
            font=("Segoe UI", 9, "bold"),
        ).pack(side="left")
        self.find_var = tk.StringVar()
        self.find_var.trace_add("write", lambda *args: self.show_row())
        search_box = self.make_box(tool_row, width=34)
        search_box.configure(textvariable=self.find_var)
        search_box.pack(side="left", padx=8, ipady=2)

        tk.Button(
            tool_row,
            text="Delete Student",
            bg="#B91C1C",
            fg="#FFFFFF",
            font=("Segoe UI", 9, "bold"),
            relief="flat",
            padx=12,
            pady=5,
            cursor="hand2",
            command=self.on_delete,
        ).pack(side="right")

        grid_wrap = tk.Frame(self.win, bg="#F4F6F9", padx=14, pady=6)
        grid_wrap.pack(fill="both", expand=True)

        my_cols = ("pos", "id", "name", "email", "subjects", "avg" "status")
        self.grid = ttk.Treeview(grid_wrap, column=my_cols, show="headings")

        self.grid.heading("pos", text="Rank")
        self.grid.heading("id", text="ID")
        self.grid.heading("name", text="Name")
        self.grid.heading("email", text="Email")
        self.grid.heading("subjects", text="Subjects & Marks")
        self.grid.heading("avg", text="average")
        self.grid.heading("status", text="Status")

        self.grid.column("pos", width=55, anchor="center")
        self.grid.column("id", width=85, anchor="center")
        self.grid.column("name", width=140)
        self.grid.column("email", width=185)
        self.grid.column("subjects", width=310)
        self.grid.column("avg", width=80, anchor="center")
        self.grid.column("status", width=115, anchor="center")

        bar = ttk.Scrollbar(grid_wrap, orient="vertical", command=self.grid.yview)
        self.grid.configure(yscrollcommand=bar.set)

        self.grid.pack(side="left", fill="both", expand=True)
        bar.pack(side="right", fill="y")
        self.grid.bind("<<,TreeviewSelect>>", self.pick_student)


    def set_msg(self, text):
        self.msg_lbl.config(text=text)

    def clear_reg_fields(self): 
        self.e_id.delete(0, tk.END)
        self.e_name.delete(0, tk.END)
        self.e_mail.delete(0, tk.END)
        self.e_subs.delete(0, tk.END)
        self.set_msg("Fields cleared.")

    def pick_student(self, event):
        sel = self.grid.selection()
        if sel:
            data = self.grid.item(sel[0], "Values")
            if data:
                self.m_id.delete(0, tk.END)
                self.m_id.insert(0, data[1])
                self.set_msg(f"Selected: {data[2]} ({data[1]})")

    def on_add_student(self):
        sid = self.e_id.get()
        nm = self.e_name.get()
        em = self.e_mail.get()
        sb = self.e_subs.get()

        done, msg = self.book.add_new_student(sid, nm, em, sb)
        if not done:
            messagebox.showerror("Error", msg)
            return

        self.m_id.delete(0, tk.END)
        self.m_id.insert(0, sid.strip().upper())
        self.clear_reg_fields()
        self.set_msg(msg)
        self.show_rows()

    def on_add_sub(self):
        sid = self.m_id.get()
        sb = self.m_sub.get()
        done, msg = self.book.add_more_subs(sid, sb)
        if not done:
            messagebox.showerror("Error", msg)
            return

        self.m_sub.delete(0, tk.END)
        self.set_msg(msg)
        self.show_rows()

    def on_save_mark(self):
        sid = self.m_id.get()
        sb = self.m_sub.get()
        val = self.m_val.get()

        done, msg = self.book.give_mark(sid, sb, val)
        if not done:
            messagebox.showerror("Error", msg)
            return

        self.m_sub.delete(0, tk.END)
        self.m_val.delete(0, tk.END)
        self.set_msg(msg)
        self.show_rows()

    def on_delete(self):
        sel = self.grid.selection()
        if not sel:
            messagebox.showwarning("Alert", "Select a student first.")
            return

        data = self.grid.item(sel[0], "values")
        sid, nm = data[1], data[2]
        if messagebox.askyesno("Confirm", f"Delete {nm} ({sid})?"):
            done, msg = self.book.remove_student(sid)
            if done:
                self.set_msg(msg)
                self.show_rows()

    def show_rows(self):
        for r in self.grid_children():
            self.grid.delete(r)

        ordered = self.book.search_and_rank(self.find_var.get())
        self.count_lbl.config(text=f"Students: {len(self.book.records)}")

        for idx, st in enumerate(ordered, start=1):
            self.grid.insert("", "end",
                             values=(
                                 idx,
                                 st.st_id,
                                 st.sname,
                                 st.mail,
                                 st.sub_list_text(),
                                 st.calc_avg(),
                                 st.my_status(),
                             ))

if __name__ =="__main__":
    root = tk.TK()
    app = MyGradeApp(root)
    root.mainloop()
