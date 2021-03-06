# NeoDeck

# WHAT İS THE NeoDeck ?

![TR](https://github.com/OgulcanKacarr/NeoDeck/blob/main/Images/Türkiye.png)
NeoDeck, yayıncıların vazgeçilmez donanım cihazı olan "[StreamDeck](https://github.com/OgulcanKacarr/NeoDeck/blob/main/Images/streamDeck.jpg "StreamDeck")" cihazının Kali Linux işletim sistemi için tasarlanmış bir kopyasıdır. Bu uygulama ile telefonunuzdan Kali Linux'a (tuş) atayabileceksiniz. Yani telefonunuz ile terminalde kod çalıştırabilirsiniz. Kullanmak için; Önce telefon uygulamasını indirin. Android uygulamasında sadece yerel ip adresinizi girmeniz gerekmektedir. Tabi aşağıda açıklanan ayarları python kodunda yapmayı unutmayınız.
<br>


![US](https://github.com/OgulcanKacarr/NeoDeck/blob/main/Images/ABD.png)
NeoDeck is a replica of the "[StreamDeck](https://github.com/OgulcanKacarr/NeoDeck/blob/main/Images/streamDeck.jpg "StreamDeck")"  device, which is the indispensable hardware device of broadcasters, designed for the Kali Linux operating system. With this application, you will be able to assign tuşfrom your phone to Kali Linux. For use; Download the phone app first. It will be sufficient to use only your local ip address in the Android application. Of course, do not forget to make the settings described below in the python code. <br><br>


# NeoDeck App: [Google Play](https://play.google.com/store/apps/details?id=com.ogulcan.neodeck "NeoDeck App")

==========================================================================<br><br>
## Android APP
![AndroidAPP](https://github.com/OgulcanKacarr/NeoDeck/blob/main/Images/ApMenu.jpg)<br><br>
## Python Code
![pythonCode](https://github.com/OgulcanKacarr/NeoDeck/blob/main/Images/help.png)<br><br>
==========================================================================<br><br>
## 
#Install<br>
```
pip install colorama
apt-get install nautilus -y
apt-get install leafpad -y

```
<br>

```
git clone https://github.com/OgulcanKacarr/NeoDeck.git
cd NeoDeck
python Neodeck.py -C startConsole  (Please read below before operating)

```
# Command and Function Settings or Change Function

- change your local ip address. But don't change the port number<br><br>
![ipSettings](https://github.com/OgulcanKacarr/NeoDeck/blob/main/Images/ipSettings.png)<br><br>
- You can change these default functions or create new ones yourself.<br><br>
![ipSettings](https://github.com/OgulcanKacarr/NeoDeck/blob/main/Images/changeFunc.png)<br><br>
- The data coming from the android application is up to "value1-value12" respectively. You can call the functions you wrote above here.<br><br>
![ipSettings](https://github.com/OgulcanKacarr/NeoDeck/blob/main/Images/getAppValue.png)<br><br>

# work in the background

- To run the application in the background, you can simply run it as: "2> / dev / null &".
![backGround](https://github.com/OgulcanKacarr/NeoDeck/blob/main/Images/background.png)<br><br>
- To turn it off again, "ps" followed by "kill <ps (python) id>
![ps](https://github.com/OgulcanKacarr/NeoDeck/blob/main/Images/psandkill.png)<br><br>

## Android APP

- Enter Kali Local Ip and save.<br>
- So now you will be able to send commands to linux.

![AppIp](https://github.com/OgulcanKacarr/NeoDeck/blob/main/Images/LoginAppIp.png)<br><br><br>


<p float="left">
  <img src="https://github.com/OgulcanKacarr/NeoDeck/blob/main/Images/app.gif" width="500" />
  <img src="https://github.com/OgulcanKacarr/NeoDeck/blob/main/Images/shell.gif" width="500" /> 
</p>

Author
email: oglcnkcr54_kcr@outlook.com
