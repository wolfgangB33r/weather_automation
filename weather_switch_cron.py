"""
Tiny script that automatically switches a Silvercrest WLAN power plug to state off in case of predicted rain,
otherwise power is on.

"""
import requests, time, sched, random, datetime, json, socket

#API to weather API
WEATHER_API_KEY = 'YOUR_OWN_WEATHER_MAP_API_KEY'
WEATHER_API_URL = 'http://api.openweathermap.org/data/2.5/forecast?q=Steyr,AT&appid=' + WEATHER_API_KEY + '&units=metric';

# WLAN power plug:
# https://wiki.fhem.de/wiki/Silvercrest_SWS_A1_Wifi
# Silvercrest WLAN power plug communicates with EC2 server 52.24.113.48:7533 TCP
# "Silvercrest Power On" means sending a UDP package with following payload
# 01 42 MAC 10 4CF75F5A28A181574AC1B563CD51A78D
# "Silvercrest Power Off" means sending a UDP package with following payload
# 01 42 MAC 10 F7B4E74B970D96F3CA2BB5D3CD1C19D0

UDP_PORT = 8530
SWITCH_IP = '192.168.0.107'

def SwitchOff():
	print('shit rain is coming switch off')
	sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
	sock.sendto(bytearray.fromhex('01 42 AC CF 23 39 36 58 10 F7 B4 E7 4B 97 0D 96 F3 CA 2B B5 D3 CD 1C 19 D0'), (SWITCH_IP, UDP_PORT))

def SwitchOn():
	print('No problem switch on')
	sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
	sock.sendto(bytearray.fromhex('01 42 AC CF 23 39 36 58 10 4C F7 5F 5A 28 A1 81 57 4A C1 B5 63 CD 51 A7 8D'), (SWITCH_IP, UDP_PORT))

def main():
	r = requests.get(WEATHER_API_URL);
	if r.status_code == 200:
		json_data = json.loads(r.text)
		#print(json_data)
		# check for rain in next 3 hours forecast
		entries = json_data['list']
		switch = True
		for i in range(0, 5):
			if 'rain' in entries[i]:
				switch = False
		if switch:
			SwitchOn()
		else:
			SwitchOff()
	else:
		print("Shit")


if __name__ == '__main__':
	main()
	
