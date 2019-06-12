class Link_info:
    def __init__(self, info_line):
        self.remote_host = ''
        self.remote_port = 0
        self.local_virt_ip = ''
        self.remote_virt_ip = ''
        self.active=True
        self.parse_info(info_line)

    def parse_info(self, info_line):
        self.remote_host, self.remote_port, self.local_virt_ip, self.remote_virt_ip = info_line.split(' ')
        self.remote_port = int(self.remote_port)


    def show(self):
        print(self.remote_host, ' ', self.remote_port, ' ', self.local_virt_ip, ' ', self.remote_virt_ip)

class Node_info:
    def __init__(self, filepath):
        self.lhost = ''
        self.lport = 0
        self.remotes = []
        self.parse_info(filepath)

    def parse_info(self, filepath):
        lnx_lines = []

        with open(filepath) as lnx_file:
            for line in lnx_file:
                lnx_lines.append(line[:-1])

        self.lhost, self.lport = lnx_lines[0].split(' ')
        self.lport = int(self.lport)
        for remote in lnx_lines[1:]:
            self.remotes.append(Link_info(remote))

    def show(self):
        print(self.lhost, ' ', self.lport)
        print(len(self.remotes))
        for remote in self.remotes:
            remote.show()

# filepath = input('Enter filepath: ')
# node_info = Node_info(filepath)
# node_info.show()
