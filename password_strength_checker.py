import re
import os

def load_common_passwords(folder: str) -> set[str]:
    all_passwords = set()

    # Check Folder Existance
    if not os.path.exists(folder):
        print(f"⚠️  '{folder}' folder not exists.")
        return set()

    # List of All Text File
    txt_files = [f for f in os.listdir(folder) if f.endswith(".txt")]

    if not txt_files:
        print(f"⚠️  '{folder}' no txt file exists in this folder!")
        return set()
    
    # Load  All Password
    for filename in txt_files:
        filepath = os.path.join(folder, filename)
        try:
            with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
                words = {line.strip().lower() for line in f if line.strip()}
                all_passwords.update(words)  
            print(f"✅  Loaded: {filename} ({len(words):,} passwords)")
        except Exception as e:
            print(f"❌  '{filename}' problem to read the file: {e}")

    print(f"\n Total {len(all_passwords):,} unique password loaded\n")
    return all_passwords

def check_password_strength(password: str,common_passwords: set[str]) -> tuple[int , str, list[str]]:
    
    score=0
    feedback=[]

    # Rule-1: Length Check
    length = len(password)
    if length < 8:
        feedback.append("❌  Use at least 8 characters")
    else:
        score += 1
        if length >= 12:
            score += 1
        if length >= 16:
            score += 1
        feedback.append(f"✅  Length is good ({length} characters)")
    
    # Rule-2: Check UpperCase Letters
    if re.search(r"[A-Z]",password):
        score += 1
        feedback.append("✅  Contains uppercase letters")
    else:
        feedback.append("❌  Add at least one uppercase letter")
    
    # Rule-3: Check LowerCase Letters
    if re.search(r"[a-z]",password):
        score += 1
        feedback.append("✅  Contains lowercase letters")
    else:
        feedback.append("❌  Add at least one lowercase letter")

    # Rule-4: Check Digits
    if re.search(r"\d",password):
        score += 1
        feedback.append("✅  Contains numbers")
    else:
        feedback.append("❌  Add at least one digit")
    
    # Rule-5: Check Special Characters
    if re.search(r"[!@#$%^&*()\-_=+\[\]{};:'\",.<>?/\\|`~]",password):
        score += 1
        feedback.append("✅  Contains special characters")
    else:
        feedback.append("❌  Add a special character")
    
    # Rule-6: Check Repeated Characters
    if re.search(r"(.)\1\1",password):
        score = max(0,score - 1)
        feedback.append("⚠️   Avoid repeating characters")
     # Rule-7: Check Common Password 
    if password.lower() in common_passwords:
        score = max(0, score - 1)
        feedback.append("⚠️ This Password Already Used")


    # Strength-Level Check 
    if score <= 2:
        label = "Weak 🔴"
    elif score <= 4:
        label = "Moderate 🟡"
    elif score <= 6:
        label = "Strong 🟢"
    else:
        label = "Very Strong 💪"
    return score, label, feedback

def display_result(password: str, score:int, label: str, feedback:list[str]) -> None:
    bar_filled = min(score, 7)
    bar = "█" * bar_filled + "░" * (7 - bar_filled)

    print("\n"+"=" * 50)
    print(f"  Password : {'*' * len(password)}")
    print(f"  Length   : {len(password)} characters")
    print(f"  Score    : [{bar}] {score}/7")
    print(f"  Strength : {label}")
    print("-" * 50)
    print("  Feedback:")
    for tip in feedback:
        print(f"    {tip}")
    print("=" * 50 + "\n")


    # Input Function
def main() -> None:
    common_passwords = load_common_passwords("password_list")
    while True:
        try:
            password = input("Enter Your Password: ")
        except(EOFError,KeyboardInterrupt):
            print("\nGoodbye !!👋")
            break
        
        if password.lower() == "quit":
            print("Goodbye !!👋")
            break

        if not password:
            print("⚠ Please Enter Your Password")
            continue
        score, label,feedback = check_password_strength(password,common_passwords)
        display_result(password,score,label,feedback)

if __name__ == "__main__":
    main()    
