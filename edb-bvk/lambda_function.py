import requests, re, os
import smtplib
from email.mime.text import MIMEText

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
sender = "ognjen.it@gmail.com"
recipients = ["ognjen.it@gmail.com"]
password = os.environ['SMTP_PASSWORD']
ulice = "(БИХАЋК|БОЈЧИНСК|ОЛГЕ ЈОВИЧИЋ)"

def send_email(subject, body, sender, recipients, password):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = ', '.join(recipients)
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp_server:
       smtp_server.login(sender, password)
       smtp_server.sendmail(sender, recipients, msg.as_string())

def check_sites():
    for i in [0, 1, 2, 3]:
        r = requests.get(f"https://elektrodistribucija.rs/planirana-iskljucenja-beograd/Dan_{i}_Iskljucenja.htm", headers=headers)
        r.encoding = r.apparent_encoding
        result = re.search(ulice, r.text)
        if result:
            subject = "Alerting - EDB"
            body = f"Bice ugasena struja za {i} dana. Patern {ulice}"
            send_email(subject, body, sender, recipients, password)
            print("EDB - Message sent!")
        else:
            print("EDB - The message wasn't sent.")
    r = requests.get("https://www.bvk.rs/planirani-radovi/", headers=headers)
    r.encoding = r.apparent_encoding
    result = re.search(ulice, r.text)
    if result:
            subject = "Alerting - BVK - planirani-radovi"
            body = f"Bice ugasena vode za {i} dana. Patern {ulice}"
            send_email(subject, body, sender, recipients, password)
            print("BVK - Message sent!")
    else:
        print("BVK - The message wasn't sent.")
    r = requests.get("https://www.bvk.rs/kvarovi-na-mrezi/", headers=headers)
    r.encoding = r.apparent_encoding
    result = re.search(ulice, r.text)
    if result:
            subject = "Alerting - BVK - kvarovi-na-mrezi"
            body = f"Bice ugasena vode za {i} dana. Patern {ulice}"
            send_email(subject, body, sender, recipients, password)
            print("BVK - Message sent!")
    else:
        print("BVK - The message wasn't sent.")

check_sites()

# def lambda_handler(event, context):
#     return check_sites()
