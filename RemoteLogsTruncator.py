import paramiko

KEYFILE = 'c:/users/tomer/.ssh/known_hosts'
USER_NAME = input("Please enter remote machine username : ")
USER_IP = input("Please insert the IP address of the remote server : ")
USER_CHOICE: str = input(
    "Please enter the name of the log you'd like to clear, or type -h for help : ")
POSSIBLE_CHOICES = ('maria', 'component1', 'component2', 'httpd')

if USER_CHOICE == '-h':
    print("Please choose one of the following choices : \n"
          "Type component1 to clear component1 logs \n"
          "Type httpd to clear httpd logs \n"
          "Type component2 to clear component2 logs \n"
          "Type maria to clear mariadb logs \n"
          "Type api to clear api logs \n\n")

elif USER_CHOICE == 'component1':
    print("Connecting to remote machine")
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy)
    ssh_client.connect(hostname=USER_IP, username=USER_NAME,
                       key_filename=KEYFILE)
    print("Login Successful!")
    print("Clearing component1 logs")
    stdin, stdout, stdeer = ssh_client.exec_command(
        "truncate -s 0 /var/log/component1.log /var/log/component2.log /var/log/component3.log")
    stdout = stdout.readlines()
    print("Done!")
    ssh_client.close()

elif USER_CHOICE == 'component3':
    print("Connecting to remote machine")
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy)
    ssh_client.connect(hostname=USER_IP, username=USER_NAME,
                       key_filename=KEYFILE)
    print("Login Successful!")
    print("Clearing components logs")
    stdin, stdout, stdeer = ssh_client.exec_command(
        "truncate -s 0 /var/log/component4.log  /var/log/component5.log")
    stdout = stdout.readlines()
    print("Done!")
    ssh_client.close()

elif USER_CHOICE == 'httpd':
    print("Connecting to remote machine")
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy)
    ssh_client.connect(hostname=USER_IP, username=USER_NAME,
                       key_filename=KEYFILE)
    print("Login Successful!")
    print("Clearing httpd logs")
    stdin, stdout, stdeer = ssh_client.exec_command(
        "truncate -s 0 /etc/httpd/logs/error_log /etc/httpd/logs/ssl_error_log /etc/httpd/logs/ssl_access_log /etc/httpd/logs/ssl_request_log")
    stdout = stdout.readlines()
    print("Done!")
    ssh_client.close()

elif USER_CHOICE == 'maria':
    print("Connecting to remote machine")
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy)
    ssh_client.connect(hostname=USER_IP, username=USER_NAME,
                       key_filename=KEYFILE)
    print("Login Successful!")
    print("Clearing mariadb logs")
    stdin, stdout, stdeer = ssh_client.exec_command(
        "truncate -s 0 /var/log/mariadb/mariadb.log")
    stdout = stdout.readlines()
    print("Done!")
    ssh_client.close()
