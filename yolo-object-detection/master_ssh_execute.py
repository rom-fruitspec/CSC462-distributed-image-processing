#   1. Install the paramikio module for python.
#       pip install paramiko
#   2. Edit the SSH details below.

import paramiko
import sys

def ssh_connect(ip_address, username, password, command):
	## EDIT SSH DETAILS ##

	# SSH_ADDRESS = "192.168.0.1"
	# SSH_USERNAME = "username"
	# SSH_PASSWORD = "password"
	# SSH_COMMAND = "echo 'Hello World!'"

	SSH_ADDRESS = ip_address
	SSH_USERNAME = username
	SSH_PASSWORD = password
	SSH_COMMAND = command

	print(ip_address, username, password, command)
	## CODE BELOW ##

	ssh = paramiko.SSHClient()
	ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

	ssh_stdin = ssh_stdout = ssh_stderr = None

	try:
		# ssh.connect(SSH_ADDRESS, username=SSH_USERNAME, password=SSH_PASSWORD)
		ssh.connect(ip_address, username, password, key_filename='<path/to/openssh-private-key-file>')
		ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command(SSH_COMMAND)
	except Exception as e:
		sys.stderr.write("SSH connection error: {0}".format(e))

	if ssh_stdout:
		sys.stdout.write(ssh_stdout.read())
	if ssh_stderr:
		sys.stderr.write(ssh_stderr.read())

def main(argv):

	# Call the ssh_connect 4 times sequntially to connect to the 4 worker nodes.
	ssh_connect("18.236.88.192", "ec2-user", "", "echo fuck")
	ssh_connect("34.212.13.86", "ec2-user", "", "echo fuck")
	ssh_connect("52.13.28.68", "ec2-user", "", "echo fuck")
	ssh_connect("34.220.148.16", "ec2-user", "", "echo fuck")




if __name__ == "__main__":
	main(sys.argv)
