import paramiko


def ssh_comand(ip, port, user, passwd, cmd):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(ip, port, username=user, password=passwd)
    server_response = ''
    _, stdout, stderr = client.exec_command(cmd)
    output = stdout.readline() + stderr.readline()
    if output:
        print('---Output ---')
        for line in output:
            server_response += (line.strip())
    print(server_response)


if __name__ == '__main__':
    user = input('Username: ')
    password = '04051970'
    ip = input('Enter server ip: ') or '192.168.0.1'
    port = input('Enter port or <CR>: ') or 22
    cmd = input('Enter command or <CR>: ') or 'id'
    ssh_comand(ip, port, user, password, cmd)
