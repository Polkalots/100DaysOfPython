import re

def main():
    email_addresses = extract_email_addresses(r'[file path]')
    for email in email_addresses:
        print(email)


def extract_email_addresses(file):
    with open(file, 'r') as f:
        text = f.read().replace('=\n', '').replace('=20', ' ').replace('&nbsp;', '')
        email_addresses = re.findall(r'(?:[A-Za-z0-9!#$%&*+-/?^_.`{|}~]+@[A-Za-z0-9-_]+\.)(?:[A-Za-z]{2,})', text)
    return email_addresses


if __name__ == '__main__':
    main()

