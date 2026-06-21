import tkinter as tk
import os
import sys

_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, _dir)
os.chdir(_dir)

from password_strength_checker import check_password_strength, load_common_passwords

#Color 
BG         = "#0f0f1a"   # main background
CARD       = "#1a1a2e"   
INPUT_BG   = "#252540"   
ACCENT     = "#7c6af7"   
TEXT       = "#e2e2f0"   
MUTED      = "#6c6c8a"   
GREEN      = "#4ade80"   
RED        = "#f87171"   
YELLOW     = "#fbbf24"   
PURPLE     = "#a78bfa"   
BORDER     = "#2e2e4a"   
WARNING_BG = "#3b1a1a"   


class PasswordCheckerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Strength Checker")
        self.root.geometry("520x680")
        self.root.configure(bg=BG)
        self.root.resizable(False, False)

        # Center on screen
        self.root.update_idletasks()
        x = (self.root.winfo_screenwidth() - 520) // 2
        y = (self.root.winfo_screenheight() - 680) // 2
        self.root.geometry(f"520x680+{x}+{y}")

        self.show_password = False
        self.common_passwords = load_common_passwords("password_list")
        self._build_ui()

    def _build_ui(self):

        # Header 
        header = tk.Frame(self.root, bg=BG)
        header.pack(pady=(35, 5))

        tk.Label(
            header,
            text="🔐",
            font=("Helvetica", 36),
            bg=BG,
            fg=ACCENT,
        ).pack()

        tk.Label(
            header,
            text="Password Strength Checker",
            font=("Helvetica", 17, "bold"),
            bg=BG,
            fg=TEXT,
        ).pack(pady=(4, 0))

        tk.Label(
            header,
            text="Find Out How Strong Your Password",
            font=("Helvetica", 11),
            bg=BG,
            fg=TEXT,
        ).pack(pady=(3, 0))

        # Input Section
        card = tk.Frame(self.root, bg=CARD, bd=0,
                        highlightthickness=1, highlightbackground=BORDER)
        card.pack(padx=35, pady=25, fill="x")

        inner = tk.Frame(card, bg=CARD)
        inner.pack(padx=20, pady=20, fill="x")

        tk.Label(
            inner,
            text="YOUR PASSWORD",
            font=("Helvetica", 10, "bold"),
            bg=CARD,
            fg=TEXT,
        ).pack(anchor="w", pady=(0, 6))

        
        row = tk.Frame(inner, bg=CARD)
        row.pack(fill="x")

        self.password_var = tk.StringVar()

        self.entry = tk.Entry(
            row,
            textvariable=self.password_var,
            show="•",
            font=("Helvetica", 13),
            bg=INPUT_BG,
            fg=TEXT,
            insertbackground=ACCENT,
            relief="flat",
            bd=0,
        )
        self.entry.pack(side="left", fill="x", expand=True,
                        ipady=11, ipadx=12)
        self.entry.bind("<Return>", lambda e: self._check())

        self.eye_btn = tk.Button(
            row,
            text="👁",
            command=self._toggle_eye,
            bg=INPUT_BG,
            fg=MUTED,
            activebackground=INPUT_BG,
            activeforeground=TEXT,
            relief="flat",
            bd=0,
            cursor="hand2",
            font=("Helvetica", 13),
            padx=8,
            pady=11,
        )
        self.eye_btn.pack(side="left")

        # Check button
        self.check_btn = tk.Button(
            row,
            text="Check",
            command=self._check,
            bg=ACCENT,
            fg="white",
            activebackground="#6b5ce7",
            activeforeground="white",
            font=("Helvetica", 11, "bold"),
            relief="flat",
            bd=0,
            cursor="hand2",
            padx=18,
            pady=11,
        )
        self.check_btn.pack(side="left", padx=(6, 0))

        # Result area 
        self.result_frame = tk.Frame(self.root, bg=BG)
        self.result_frame.pack(padx=35, fill="both", expand=True)

    def _toggle_eye(self):
        self.show_password = not self.show_password
        self.entry.config(show="" if self.show_password else "•")
        self.eye_btn.config(fg=TEXT if self.show_password else MUTED)

    def _clear_results(self):
        for w in self.result_frame.winfo_children():
            w.destroy()

    def _check(self):
        password = self.password_var.get()
        self._clear_results()

        if not password:
            self._show_message("⚠️  Please Enter a Password First.", YELLOW)
            return

        score, label, feedback = check_password_strength(password, self.common_passwords)
        is_common = password.lower() in self.common_passwords
        self._render_result(score, label, feedback, is_common)

    def _render_result(self, score, label, feedback, is_common):

        if "Weak" in label:
            color = RED
        elif "Moderate" in label:
            color = YELLOW
        elif "Strong 🟢" in label:
            color = GREEN
        else:
            color = PURPLE

        #  Strength Level Section
        s_card = tk.Frame(self.result_frame, bg=CARD, bd=0,
                          highlightthickness=1, highlightbackground=BORDER)
        s_card.pack(fill="x", pady=(0, 10))

        s_inner = tk.Frame(s_card, bg=CARD)
        s_inner.pack(padx=20, pady=16, fill="x")

        tk.Label(
            s_inner,
            text="STRENGTH",
            font=("Helvetica", 8, "bold"),
            bg=CARD,
            fg=MUTED,
        ).pack(anchor="w")

        tk.Label(
            s_inner,
            text=label,
            font=("Helvetica", 20, "bold"),
            bg=CARD,
            fg=color,
        ).pack(anchor="w", pady=(4, 8))

        # Score bar
        bar_frame = tk.Frame(s_inner, bg=CARD)
        bar_frame.pack(fill="x")

        for i in range(7):
            filled = i < score
            seg = tk.Frame(
                bar_frame,
                bg=color if filled else BORDER,
                height=6,
                width=48,
            )
            seg.pack(side="left", padx=(0, 4))

        tk.Label(
            s_inner,
            text=f"{score} / 7",
            font=("Helvetica", 9),
            bg=CARD,
            fg=MUTED,
        ).pack(anchor="w", pady=(6, 0))

        # Common Password Warning
        if is_common:
            w_card = tk.Frame(self.result_frame, bg=WARNING_BG, bd=0,
                              highlightthickness=1, highlightbackground=RED)
            w_card.pack(fill="x", pady=(0, 10))

            tk.Label(
                w_card,
                text="⛔ This password is already used!",
                font=("Helvetica", 11, "bold"),
                bg=WARNING_BG,
                fg=RED,
                anchor="w",
            ).pack(padx=16, pady=6, anchor="w")

            tk.Label(
                w_card,
                text="It appears in known leaked password lists. Choose something unique.",
                font=("Helvetica", 9),
                bg=WARNING_BG,
                fg="#d16060",
                anchor="w",
                wraplength=440,
                justify="left",
            ).pack(padx=16, pady=(0, 10), anchor="w")

        # Feedback Section
        f_card = tk.Frame(self.result_frame, bg=CARD, bd=0,
                          highlightthickness=1, highlightbackground=BORDER)
        f_card.pack(fill="x", pady=(0, 20))

        f_inner = tk.Frame(f_card, bg=CARD)
        f_inner.pack(padx=20, pady=16, fill="x")

        tk.Label(
            f_inner,
            text="FEEDBACK",
            font=("Helvetica", 8, "bold"),
            bg=CARD,
            fg=MUTED,
        ).pack(anchor="w", pady=(0, 8))

        for tip in feedback:
            if tip.startswith("✅"):
                fg = GREEN
            elif tip.startswith("❌"):
                fg = RED
            else:
                fg = YELLOW

            tk.Label(
                f_inner,
                text=tip,
                font=("Helvetica", 10),
                bg=CARD,
                fg=fg,
                anchor="w",
            ).pack(fill="x", pady=2)

    def _show_message(self, msg, color=YELLOW):
        tk.Label(
            self.result_frame,
            text=msg,
            font=("Helvetica", 11),
            bg=BG,
            fg=color,
        ).pack(pady=10)

def main():
    root = tk.Tk()
    PasswordCheckerApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
