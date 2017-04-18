import argparse
import smtplib
parser = argparse.ArgumentParser()
parser.add_argument('-t', help = 'Torrent Name')
args = parser.parse_args()
if args.t:
  gmail_user = 'user@gmail.com' # Your Email
  gmail_pwd = 'usergmail' # Your Password
  FROM = 'user@gmail.com'
  TO = FROM
  message = 'Torrent Downloaded Successfully' + ' ' + str(args.t)
  server_ssl = smtplib.SMTP_SSL("smtp.gmail.com", 465)
  server_ssl.ehlo() # optional, called by login()
  server_ssl.login(gmail_user, gmail_pwd)  
  # ssl server doesn't support or need tls, so don't call server_ssl.starttls() 
  server_ssl.sendmail(FROM, TO, message)
  #server_ssl.quit()
  server_ssl.close()
  print 'successfully sent the mail'
else:
  print 'fail'
