# test login sftp while true
import pysftp
import paramiko
from datetime import datetime


# ""
# ""
# ""

# Break manualy
# all args should be strings (host, usern, passwd, sftp_file_name)

def check_sftp(host, usern, passwd, sftp_file_name):
    with open(sftp_file_name, "a") as sftp_file:
        while True:
            try:
                with pysftp.Connection(host=host, username=usern, password=passwd):
                    sftp_file.write(str(datetime.now()) +
                                    "  Connection succesfully" + "\n")
            except paramiko.AuthenticationException:
                sftp_file.write(str(datetime.now()) +
                                "  Connection refused \"paramiko.AuthenticationException\" " + "\n")
            except ConnectionResetError:
                sftp_file.write(str(datetime.now()) +
                                "  Connection reset error \"ConnectionResetError\" " + "\n")
            except paramiko.SSHException:
                sftp_file.write(str(datetime.now()) +
                                "  Connection reset error \"paramiko.SSHException\" " + "\n")


if __name__ == "__main__":
    print("start logging")
    print("testbranch")
    check_sftp("sftp7-qa.com", "",
               "", "21-04testeu-west4.log")
