#!/usr/bin/env bash
# a Bash script that sets up your web servers for the deployment of web_static

# Update package list
sudo apt-get update

# Install Nginx if it not already installed
if ! command -v nginx &> /dev/null; then
    sudo apt-get install -y nginx
fi

# Create directories for web_static deployment
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/

# Create a fake HTML file for testing
echo "<html>
<head></head>
<body>Holberton School</body>
</html>" | sudo tee /data/web_static/releases/test/index.html

# Create a symbolic link to test folder
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

# Give ownership of the /data/ folder to the ubuntu user AND group
sudo chown -R ubuntu:ubuntu /data/

# Update the Nginx configuration to serve the content of /data/web_static/current/ to hbnb_static
sudo sed -i "/server_name _/a \
\n\tlocation /hbnb_static { \
\n\t\talias /data/web_static/current/; \
\n\t}" /etc/nginx/sites-available/default

# Restart Nginx to apply changes
sudo service nginx restart
