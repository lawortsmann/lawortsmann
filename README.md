# lawortsmann
My website: lawortsmann.com

https://www.digitalocean.com/community/tutorials/how-to-install-the-apache-web-server-on-ubuntu-18-04

https://www.digitalocean.com/community/tutorials/how-to-secure-apache-with-let-s-encrypt-on-ubuntu-18-04

--- BASIC USAGE ---

# WEBSERVER
/etc/apache2/
/var/www/

# UPDATE
sudo apt-get update

# RESTART SERVER
sudo systemctl restart apache2
sudo systemctl reload apache2

# ENABLE/DISABLE SITES
sudo a2ensite ****.conf
sudo a2dissite ****.conf

# CERTBOT
sudo certbot renew

# GIT
# sites symlinked in /home/luke/Web/
sudo ln -s /home/luke/Web/... /var/www/...
# to create new project:
mkdir -p /home/luke/Projects/project_name.git
git init --bare
# on local machine:
git clone luke@34.233.38.17:/home/luke/Projects/project_name.git
