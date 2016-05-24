import paramiko
import io
import time


#Generates the SSH exchange, for debugging.
paramiko.common.logging.basicConfig(level=paramiko.common.DEBUG)

#http://stackoverflow.com/questions/17316669/python-class-and-ssh-connections-does-not-work-well

class sshConnect():
	def getConnection(self, IP, USN, PSW):
		try:
			self.client = paramiko.SSHClient()
			#print self.client
			self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
			#print self.client
			self.client.connect(IP, username=USN, password=PSW)
			#print self.client
			channel = self.client.invoke_shell()
			self.stdin = channel.makefile('wb')
			self.stdout = channel.makefile('rb')
			self.stderr = channel.makefile_stderr('er')
			print 'self.stdin ', self.stdin
			return 0
		except Exception as e:
			print e
			return 1

conn = sshConnect()
print conn.getConnection("172.22.1.1","admin","password")


recv_data = conn.stdout.channel.recv(10640)
print "recv_data 1", recv_data
#Returns MOTD


recv_data = conn.stdout.channel.recv(10640)
print recv_data
#Returns Prompt

send_me = conn.stdin.channel.send_ready()
print "send_me2", send_me
#Returns True

conn.stdin.channel.send('show arp\n')
recv_data = conn.stdout.channel.recv(10640)


conn.stdin.channel.send('en\n')
recv_data = conn.stdout.channel.recv(10640)
print recv_data
#Returns arp table

time.sleep(1)

conn.stdin.channel.send('password\n')
recv_data = conn.stdout.channel.recv(10640)

time.sleep(1)

conn.stdin.channel.send('show ver\n')
recv_data = conn.stdout.channel.recv(10640)


conn.stdin.channel.send('exit\n')
recv_data = conn.stdout.channel.recv(10640)

conn.stdin.channel.send('exit\n')
recv_data = conn.stdout.channel.recv(10640)
print recv_data
#Returns show ver

