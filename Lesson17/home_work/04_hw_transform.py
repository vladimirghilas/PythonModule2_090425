# У вас есть список строк, некоторые из которых содержат email-адреса.
# Вам нужно извлечь все email-адреса и привести их к нижнему регистру.
# email-адреса содержат символ '@'.

log_entries = [
    "User logged in: john.doe@example.com",
    "Error occurred",
    "New user registered: Jane_Smith@Example.ORG",
    "Another log",
    "Contact us at support@test.co.uk"
]
import re

all_email = []
email_pattern = r'[a-z,A-Z,0-9,._%+-]+@[a-z,A-Z,0-9.-]+\.[a-z,A-Z]{2,}'

for email in log_entries:
    if re.findall(email_pattern, email):
        all_email.append(re.findall(email_pattern, email)[0].lower())
print(all_email)

all_email =[
            re.findall(email_pattern, email)[0].lower()
            for email in log_entries
            if re.findall(email_pattern,email)]
print(all_email)
