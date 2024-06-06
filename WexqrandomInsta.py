import string
import random
import time
import pyfiglet

x = """\x1b[1;31m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━⠀⠀⠀⠀
							⠀
⠀⠀⠀⠀⠀⠀⢀⡠⠖⠚⠋⠉⠉⠉⠙⠒⢦⡀⠀⠀⠀⠀
⠀⠀⠀⠀⢠⠞⠉⠀⠀⠀⢠⣾⣿⡦⡀⠀⣴⣾⣧.⣀ ⠀⠀
⠀⠀⠀⢠⡏⠀⠀⠀⠀⠀⠀⣉⣁⣀⣀⣤⣿⣿⣿⣿⣦..⠀ 
⠀⠀⠀⡞⠀⠀⠀⠀⠀⠀⠀⠙⠋⠉⠙⢻⣿⣿⣿⣿⣿ ...⠀
⠀⢀⡞⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡞⠉⠉⠙⡟ ..⠀
⠀⢸⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢳⡀⠀⠀⠀⠀
⠀⢈⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣤⡀⡀⠳⡄⠀⠀⠀
⠀⣸⡴⠀⠀⠀⠀⠀⠀⡀⢠⡄⣄⣷⣿⣷⣷⣠⡘⣆⠀⠀
⢠⣿⣧⡞⣠⡄⣰⣇⣼⣷⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡀
⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⣧
⠋⠁⣿⡿⠟⣿⣿⣿⡿⣿⣿⣿⠋⠻⣿⣿⠏⠉⠻⣿⠀⠉
⠀⠀⠈⠀⠀⠙⣿⡿⠁⠈⣿⠏⠀⠀⠈⠉⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠈⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀


		                    𝐑𝐚𝐧𝐝𝐨𝐦 𝐢𝐧𝐬𝐭𝐚 𝐇𝐞𝐬𝐚𝐛 𝐂𝐞𝐤𝐦𝐞\n                     	𝐩𝐫𝐨𝐠𝐫𝐚𝐦𝐞𝐫:      @𝐖𝐞𝐱𝐪0\n			𝐂𝐡𝐚𝐧𝐞𝐥:            @𝐖𝐞𝐱𝐪𝐏𝐲𝐭𝐡𝐨𝐧
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━⠀⠀⠀⠀⠀ ⠀⠀"""

print(x)
time.sleep(0.1)

def random_string(length=19):
    letters = string.ascii_lowercase + string.digits
    return ''.join(random.choice(letters) for _ in range(length))

def generate_email(provider):
    if provider == "gmail":
        return random_string() + "@gmail.com"
    elif provider == "hotmail":
        return random_string() + "@hotmail.com"
    elif provider == "outlook":
        return random_string() + "@outlook.com"
    elif provider == "yahoo":
        return random_string() + "@yahoo.com"
    elif provider == "protonmail":
        return random_string() + "@protonmail.com"
    elif provider == "zoho":
        return random_string() + "@zoho.com"
    elif provider == "aol":
        return random_string() + "@aol.com"
    elif provider == "yandex":
        return random_string() + "@yandex.com"
    else:
        return None


def generate_accounts(provider):
    while True:
        email = generate_email(provider)
        password = random_string()

        if email:
            with open("wexqRandominsta.txt", "a") as f:
                f.write(email + "\n" + password + "\n")

            print(f"\x1b[1;36m𝐑𝐚𝐧𝐝𝐨𝐦 𝐢𝐧𝐬𝐭𝐚𝐠𝐫𝐚𝐦 𝐡𝐞𝐬𝐚𝐛ı\n𝐦𝐚𝐢𝐥:  {email}")
            print(f"\x1b[1;36m𝐒𝐢𝐟𝐫𝐞:  {password}\n")
            time.sleep(0.1)

def main():
    while True:
        provider = input("""\x1b[1;31⬇️ 𝐒𝐞𝐜𝐞𝐧𝐞𝐤𝐥𝐞𝐫 ⬇️

➡️ 𝐠𝐦𝐚𝐢𝐥
➡️ 𝐡𝐨𝐭𝐦𝐚𝐢𝐥
➡️ 𝐳𝐨𝐡𝐨
➡️ 𝐲𝐚𝐧𝐝𝐞𝐱
➡️ 𝐚𝐨𝐥
➡️ 𝐩𝐫𝐨𝐭𝐨𝐧𝐦𝐚𝐢𝐥
➡️ 𝐨𝐮𝐭𝐥𝐨𝐨𝐤
➡️ 𝐲𝐚𝐡𝐨𝐨\n\n𝐇𝐚𝐧𝐠𝐢𝐬𝐢𝐧 𝐬𝐞𝐜𝐦𝐞𝐤 𝐢𝐬𝐭𝐢𝐲𝐨𝐫𝐬𝐮𝐧 ➡️              """).strip().lower()
        if provider in ["gmail", "hotmail","outlook","yahoo","zoho","yopmail","yandex","aol","protonmail"]:
            generate_accounts(provider)
        else:
            print("𝐘𝐚𝐧𝐥ış 𝐬𝐞𝐜𝐞𝐧𝐞𝐤 𝐒𝐚𝐝𝐞𝐜𝐞 𝐠𝐦𝐚𝐢𝐥, 𝐡𝐨𝐭𝐦𝐚𝐢𝐥,𝐳𝐨𝐡𝐨,𝐲𝐚𝐧𝐱𝐞𝐱,𝐚𝐨𝐥,𝐩𝐫𝐨𝐭𝐨𝐧𝐦𝐚𝐢𝐥,𝐨𝐮𝐭𝐥𝐨𝐨𝐤,𝐲𝐚𝐡𝐨𝐨 𝐒𝐚𝐝𝐞𝐜𝐞 𝐁𝐮 𝐬𝐞𝐜𝐞𝐧𝐞𝐤𝐥𝐞𝐫𝐢 𝐤𝐮𝐥𝐚𝐧𝐚𝐛𝐢𝐥𝐢𝐫𝐬𝐢𝐧")

if __name__ == "__main__":
    main()
