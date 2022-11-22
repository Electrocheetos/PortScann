




import nmap



print()
print("  ____            _   ____                         ")
print(" |  _ \ ___  _ __| |_/ ___|  ___ __ _ _ __  _ __   ")
print(" | |_) / _ \| '__| __\___ \ / __/ _` | '_ \| '_ \  ")
print(" |  __/ (_) | |  | |_ ___) | (_| (_| | | | | | | | ")
print(" |_|   \___/|_|   \__|____/ \___\__,_|_| |_|_| |_| ")




print("[Info] Herramienta para escanear los puertos abiertos de una dirección IP de tu red local")
print(" [!] Script hecho por Electrocheetos uwu")


ip=input("[+] Introduzca la IP >>> ")
nm = nmap.PortScanner()
puertos_abiertos="-p "
results = nm.scan(hosts=ip,arguments="-sT -n -Pn -T4")
count=0
#print (results)
print("\nHost : %s" % ip)
print("State : %s" % nm[ip].state())
for proto in nm[ip].all_protocols():
	print("Protocol : %s" % proto)
	print()
	lport = nm[ip][proto].keys()
	sorted(lport)
	for port in lport:
		print ("port : %s\tstate : %s" % (port, nm[ip][proto][port]["state"]))
		if count==0:
			puertos_abiertos=puertos_abiertos+str(port)
			count=1
		else:
			puertos_abiertos=puertos_abiertos+","+str(port)

print("\nPuertos abiertos: "+ puertos_abiertos +" "+str(ip))
print("para verificar si es vulnerable use el comando nmap --script vuln <IP objetivo>")
