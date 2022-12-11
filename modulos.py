from osint import QBDns, QBScan
objetivo = QBDns().convert_to_ips(["https://uide.edu.ec"] )
objetivo = QBScan().run(targets,[80,443])
print(objetivo)