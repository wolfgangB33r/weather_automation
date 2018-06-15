# weather automation
A simple Python script that switches a Silvercrest WLAN power plug to off when weather forecast predicts rain.

Script was written for a low cost Silvercrest WLAN power plug that receives UDP packages to switch power on and off.

Kudos to https://wiki.fhem.de/wiki/Silvercrest_SWS_A1_Wifi
for providing the infos on Silvercrest UDP protocol!

Silvercrest Power switch also communicates with EC2 server on IP 52.24.113.48:7533 TCP

In general UDP packages are used within Silvercrest WLAN power switches to turn power on and off. 

To turn on, send following UDP package, where you replace MAC with your own devices MAC address:

01 42 MAC 10 4CF75F5A28A181574AC1B563CD51A78D

To turn off send following UDP payload:

01 42 MAC 10 F7B4E74B970D96F3CA2BB5D3CD1C19D0


The mobile app communicates with a central authority:
http://smart2connect.yunext.com/api/device/wifi/list/?
