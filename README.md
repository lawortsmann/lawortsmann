# lawortsmann
My website: lawortsmann.com

https://www.digitalocean.com/community/tutorials/how-to-install-the-apache-web-server-on-ubuntu-18-04

https://www.digitalocean.com/community/tutorials/how-to-secure-apache-with-let-s-encrypt-on-ubuntu-18-04

--- BASIC USAGE ---

## WEBSERVER
/etc/apache2/
/var/www/

## UPDATE
sudo apt-get update

## RESTART SERVER
sudo systemctl restart apache2
sudo systemctl reload apache2

## ENABLE/DISABLE SITES
sudo a2ensite ****.conf
sudo a2dissite ****.conf

## CERTBOT
sudo certbot renew

Congratulations! You have successfully enabled https://lawortsmann.com and
https://www.lawortsmann.com

You should test your configuration at:
https://www.ssllabs.com/ssltest/analyze.html?d=lawortsmann.com
https://www.ssllabs.com/ssltest/analyze.html?d=www.lawortsmann.com
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

IMPORTANT NOTES:
 - Congratulations! Your certificate and chain have been saved at:
   /etc/letsencrypt/live/lawortsmann.com/fullchain.pem
   Your key file has been saved at:
   /etc/letsencrypt/live/lawortsmann.com/privkey.pem
   Your cert will expire on 2019-12-19. To obtain a new or tweaked
   version of this certificate in the future, simply run certbot again
   with the "certonly" option. To non-interactively renew *all* of
   your certificates, run "certbot renew"
 - Your account credentials have been saved in your Certbot
   configuration directory at /etc/letsencrypt. You should make a
   secure backup of this folder now. This configuration directory will
   also contain certificates and private keys obtained by Certbot so
   making regular backups of this folder is ideal.
