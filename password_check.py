import math

def upper_check(ch:str):
    if ch.isupper():
        return True
    else: 
        return False

def lower_check(ch:str):
    if ch.islower():
        return True
    else: 
        return False

def len_check(pwd:str) -> bool:
    return len(pwd) > 10

def spc_check(pwd:str, special_symb:str):
    counter = 0
    for ch in pwd:
        if ch in special_symb:
            counter += 1
            continue
    if counter > 2:
        return True
    else:
        print("Your password must contain at least 3 special symbols.")
        return False
    
def lower_upper_check(pwd:str, spec_symb:str) ->  bool:
    counter_upp = 0
    counter_low = 0
    for ch in pwd:
        if lower_check(ch) and ch not in spec_symb:
            counter_low += 1
        elif upper_check(ch) and ch not in spec_symb:
            counter_upp += 1
    if counter_upp > 3 and counter_low > 2:
        return True
    else:
        return False

def check_sequences(pwd:str, spec_symb:str, max_len: int = 2) -> bool:
    categories = {}
    categories['current'] = None
    categories['count'] = 0
    categories['max'] = max_len
    def get_category(ch: str) -> str:
        if ch.islower() and ch not in spec_symb:
            return 'lower'
        elif ch.isupper() and ch not in spec_symb:
            return 'upper'
        elif ch.isdigit():
            return 'digit'
        elif ch in spec_symb:
            return 'spec_symbs'
        return 'other'
    for ch in pwd:
        current_category = get_category(ch)
        if current_category == categories['current']:
            categories['count'] += 1
        else:
            categories['current'] = current_category
            categories['count'] = 1
        if categories['count'] > categories['max']:
            return False
        
    return True
        
def check_weaks(pwd:str) -> bool:
    weak_passwords = [
        "123456","123456789","12345678","12345","1234567","1234567890",
        "111111","000000","123123","654321","qwerty","qwerty123",
        "qwertyuiop","1q2w3e4r","1q2w3e","123qwe","password","password1",
        "passw0rd","admin","administrator","root","user","login","guest",
        "test","letmein","welcome","iloveyou","love","dragon","monkey",
        "football","baseball","soccer","basketball","superman","batman",
        "pokemon","starwars","hello","sunshine","flower","princess",
        "qazwsx","zaq12wsx","1qaz2wsx","abc123","abcd1234","abc123456",
        "qwe123","qweasd","asdfgh","zxcvbn","1q2w3e4r5t","q1w2e3r4",
        "q1w2e3","1234qwer","qwer1234","11111111","222222","333333",
        "444444","555555","666666","777777","888888","999999","121212",
        "112233","123321","13579","246810","asdf1234","pass123",
        "mypassword","default","computer","internet","secure",
        "password123","admin123","user123","login123","qwerty1",
        "qwerty12","qwerty1234","1qazxsw2","1qazxsw","qazxsw","qaz123",
        "qweqwe","asdfasdf","zxcvzxcv","1234abcd","abcd123",
        "abcde12345","letmein123","welcome1","welcome123"
    ]
    if pwd in weak_passwords:
        print("This password is in the list of the weakest passwords.")
        return False
    return True

def password_entropy(pwd: str, special_symb: str) -> float:
    alphabet = 0
    for ch in pwd:
        if ch.islower():
            alphabet += 26
            break
    for ch in pwd:
        if ch.isupper():
            alphabet += 26
            break
    for ch in pwd:
        if ch.isdigit():
            alphabet += 10
            break
    for ch in pwd:
        if ch in special_symb:
            alphabet += len(special_symb)
            break
    if alphabet == 0:
        alphabet = 1
    entropy = len(pwd) * math.log2(alphabet)
    return entropy

def similar_passwords(old_pwd: str, new_pwd: str) -> bool:
    min_len = min(len(old_pwd), len(new_pwd))
    same = 0
    for i in range(min_len):
        if old_pwd[i] == new_pwd[i]:
            same += 1
    equality = same / min_len
    if equality > 0.7:
        return True
    return False

password_memory = {}

def memorize_password(func):
    def wrapper(pwd, *args, **kwargs):
        if pwd in password_memory:
            print("This password has already been used before.")
        else:
            password_memory[pwd] = True
            print("Password saved to memory.")
        return func(pwd, *args, **kwargs)
    return wrapper

@memorize_password
def password_memorize(pwd: str):
    print("password_memorize function executed.")
    return True

def password_checker(pwd: str):
    special_symbs = "~!@#$%^&*()_+/|"
    entropy = password_entropy(pwd, special_symbs)
    print("Password entropy:", entropy)
    if entropy < 40:
        print("Entropy is too low.")
        return False
    elif entropy < 60:
        print("Entropy is acceptable.")
    else:
        print("Entropy is strong.")
    if not len_check(pwd):
        print("Password is too short.")
        return False
    if not spc_check(pwd, special_symbs):
        return False
    if not lower_upper_check(pwd, special_symbs):
        print("Not enough upper and/or lower case letters.")
        return False
    if not check_sequences(pwd, special_symbs):
        print("Too many repeating characters of the same category.")
        return False
    if not check_weaks(pwd):
        print("Password is too weak.")
        return False

    password_memorize(pwd)
    print("Password is strong.")
    return True

def enterer_password() -> str:
    print("Enter your password:")
    return input()

def change_password():
    print("Enter your old password:")
    old_pwd = input()
    if old_pwd not in password_memory:
        print("This password is not found in memory. Cannot change.")
        return False
    print("Enter your new password:")
    new_pwd = input()
    if new_pwd in password_memory:
        print("This password has already been used before. Choose another one.")
        return False
    if similar_passwords(old_pwd, new_pwd):
        print("New password is too similar to the old one.")
        return False
    if not password_checker(new_pwd):
        print("New password did not pass validation.")
        return False
    print("Password successfully changed.")
    return True

def print_password_rules():
    print("\n=== Password Requirements ===")
    print("1. Length must be more than 10 characters.")
    print("2. Password must contain at least 3 special symbols:")
    print("   ~!@#$%^&*()_+/|")
    print("3. Must contain at least 4 uppercase letters (A–Z).")
    print("4. Must contain at least 3 lowercase letters (a–z).")
    print("5. No more than 2 consecutive characters of the same category:")
    print("   - lowercase letters")
    print("   - uppercase letters")
    print("   - digits")
    print("   - special symbols")
    print("6. Password must not be in the list of weak passwords.")
    print("7. Password entropy must be at least 40 bits.")
    print("8. Password must not have been used before.")
    print("9. When changing password, new one must not be more than 70% similar to the old one.")
    print("==============================\n")

def password_menu():
    while True:
        print("\nChoose an action:")
        print("1 — Create a password")
        print("2 — Change password")
        print("3 — Show saved passwords")
        print("4 — Show password rules")
        print("5 — Exit")
        choice = input("Your choice: ")
        if choice == "1":
            pwd = enterer_password()
            password_checker(pwd)
        elif choice == "2":
            change_password()
        elif choice == "3":
            print("Saved passwords:")
            for p in password_memory:
                print(p)
        elif choice == "4":
            print_password_rules()
        elif choice == "5":
            print("Exiting program.")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    password_menu()
