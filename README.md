this is fast api application
setup on ubuntu server
environment variables need to be specified for it to work

Example:
DATABASE_HOSTNAME=test-ashish
DATABASE_PORT=5432
DATABASE_PASSWORD=postgres
DATABASE_NAME=fastapi
DATABASE_USERNAME=postgres
SECRET_KEY=818aad4c3e764b858c5b87af7f6ffa33231220544c0b31458a995959e6150537
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30

# fastapi_ubuntu_oci_vm

# deploying on ubuntu server

https://notes.kodekloud.com/docs/Python-API-Development-with-FastAPI/Deployment/Deploy-Ubuntu-VM/page

-- deploying on oci ubuntu server

sudo apt update && sudo apt upgrade -y
sudo apt install python3-pip
sudo pip3 install virtualenv
sudo apt install postgresql postgresql-contrib -y
pg_ctlcluster 12 main start
su - postgres
psql -U postgres

Next, modify the PostgreSQL configuration files located in /etc/postgresql/12/main:
In pg_hba.conf, change:
local   all             postgres        peer
to:
local   all             postgres        md5
To enable remote connections (if needed), edit postgresql.conf and set:
listen_addresses = '*'
Now, restart PostgreSQL:
sudo systemctl restart postgresql
Test the connection:
psql -U postgres
You should now be prompted for the password.

create user

adduser ashish
Follow the prompts to set a password and enter the user details. Next, add this user to the sudo group:
usermod -aG sudo ashish



    3  mkdir app
    4  cd app
    5  mkdir src
    6  pwd
    7  python3 -m venv venv
    8  ls
    9  source venv/bin/activate
   10  cd src
   11  git clone https://github.com/ashkave/fastapi_app_alembic.git
   12  ls
   13  rm -rf fastapi_app_alembic/
   14  git clone https://github.com/ashkave/fastapi_app_alembic.git .
   15  ls
   16  vi requirements.txt
   17  pip install -r requirements.txt
   
   ubuntu@test-ashish:~$ nc -zv 130.210.23.125 5432
Connection to 130.210.23.125 5432 port [tcp/postgresql] succeeded!


ubuntu@test-ashish:~$ sudo iptables -I INPUT 1 -p tcp --dport 5432 -j ACCEPT

sudo iptables -I INPUT 1 -p tcp --dport 8000 -j ACCEPT
sudo iptables -I INPUT 1 -p tcp --dport 443 -j ACCEPT
sudo iptables -I INPUT 1 -p tcp --dport 80 -j ACCEPT


(venv) ashish@test-ashish:~/app/src$ uvicorn app_orm_alembic.main:app --host 0.0.0.0
INFO:     Started server process [17498]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)



(venv) ashish@test-ashish:~/app/src$ gunicorn -w 2 -k uvicorn.workers.UvicornWorker app_orm_alembic.main:app --bind 0.0.0.0:8000
[2026-10-02 14:32:34 +0000] [17639] [INFO] Starting gunicorn 26.2.0
[2026-10-02 14:32:34 +0000] [17639] [INFO] Listening at: http://0.0.0.0:8000 (17639)
[2026-10-02 14:32:34 +0000] [17639] [INFO] Using worker: uvicorn.workers.UvicornWorker
[2026-10-02 14:32:34 +0000] [17640] [INFO] Booting worker with pid: 17640
[2026-10-02 14:32:34 +0000] [17641] [INFO] Booting worker with pid: 17641
[2026-10-02 14:32:34 +0000] [17639] [INFO] Control socket listening at /home/ashish/.gunicorn/gunicorn.ctl
[2026-10-02 14:32:35 +0000] [17640] [INFO] Started server process [17640]
[2026-10-02 14:32:35 +0000] [17640] [INFO] Waiting for application startup.
[2026-10-02 14:32:35 +0000] [17640] [INFO] Application startup complete.
[2026-10-02 14:32:35 +0000] [17641] [INFO] Started server process [17641]
[2026-10-02 14:32:35 +0000] [17641] [INFO] Waiting for application startup.
[2026-10-02 14:32:35 +0000] [17641] [INFO] Application startup complete.

http://130.210.23.125:8000/docs


# nginx configuration

sudo apt install nginx -y

sudo systemctl start nginx
sudo systemctl restart nginx

vi /etc/nginx/sites-available/default


   proxy_pass http://localhost:8000;
        proxy_http_version 1.1;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "upgrade";
        proxy_set_header Host $http_host;
        proxy_set_header X-NginX-Proxy true;
        proxy_redirect off;
		
		
# purchase domain from namecheap -- ashkave.xyz

# create an OCI public DNS zone with ashkave.xyz

# add dns servers for oci pub zone in the namecheap domain that was purchased
ns1.p202.dns.oraclecloud.net.
ns2.p202.dns.oraclecloud.net.
ns3.p202.dns.oraclecloud.net.
ns4.p202.dns.oraclecloud.net.

# Add A record in OCI Public zone for the public ip of the ubuntu vm


# ssl

https://certbot.eff.org/

sudo snap install core; sudo snap refresh core
sudo snap install --classic certbot
sudo ln -s /snap/bin/certbot /usr/bin/certbot


ashish@test-ashish:~$ sudo certbot --nginx
Saving debug log to /var/log/letsencrypt/letsencrypt.log
Please enter the domain name(s) you would like on your certificate (comma and/or
space separated) (Enter 'c' to cancel): ashkave.xyz www.ashkave.xyz
Requesting a certificate for ashkave.xyz and www.ashkave.xyz

Certbot failed to authenticate some domains (authenticator: nginx). The Certificate Authority reported these problems:
  Identifier: ashkave.xyz
  Type:   connection
  Detail: 130.210.23.125: Fetching http://ashkave.xyz/.well-known/acme-challenge/Nm17ETWsSfjB3dCVrrL0TDKFZdsY3bfhyVoHzjYSOiU: Error getting validation data

  Identifier: www.ashkave.xyz
  Type:   connection
  Detail: 130.210.23.125: Fetching http://www.ashkave.xyz/.well-known/acme-challenge/M4GmuSJN5DMiKYwXGyFCuaUY18QpvnUCmNO7mvN24GM: Error getting validation data

Hint: The Certificate Authority failed to verify the temporary nginx configuration changes made by Certbot. Ensure the listed domains point to this nginx server and that it is accessible from the internet.

Some challenges have failed.
Ask for help or search for solutions at https://community.letsencrypt.org. See the logfile /var/log/letsencrypt/letsencrypt.log or re-run Certbot with -v for more details.
ashish@test-ashish:~$ sudo iptables -I INPUT 1 -p tcp --dport 443 -j ACCEPT
sudo iptables -I INPUT 1 -p tcp --dport 80 -j ACCEPT
ashish@test-ashish:~$ sudo certbot --nginx
Saving debug log to /var/log/letsencrypt/letsencrypt.log
Please enter the domain name(s) you would like on your certificate (comma and/or
space separated) (Enter 'c' to cancel): ashkave.xyz
Requesting a certificate for ashkave.xyz

Successfully received certificate.
Certificate is saved at: /etc/letsencrypt/live/ashkave.xyz/fullchain.pem
Key is saved at:         /etc/letsencrypt/live/ashkave.xyz/privkey.pem
This certificate expires on 2027-01-03.
These files will be updated when the certificate renews.
Certbot has set up a scheduled task to automatically renew this certificate in the background.

Deploying certificate
Successfully deployed certificate for ashkave.xyz to /etc/nginx/sites-enabled/default
Congratulations! You have successfully enabled HTTPS on https://ashkave.xyz

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
If you like Certbot, please consider supporting our work by:
 * Donating to ISRG / Let's Encrypt:   https://letsencrypt.org/donate
 * Donating to EFF:                    https://eff.org/donate-le
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
ashish@test-ashish:~$
