import requests
from dotenv import dotenv_values
mail_configuration = dotenv_values()

def send_message(email, message):
  mail_api_key= mail_configuration["MAILGUN_API_KEY"]
  mail_domain = mail_configuration["MAILGUN_API_DOMAIN"]

  return requests.post(
    "https://api.mailgun.net/v3/{}/messages".format(mail_domain),
      auth=("api", mail_api_key),
      data={"from": "Excited User <mailgun@{mail_domain}>".format(mail_domain),
        "to": [],
        "subject": "Greetings!",
        "text": message})
