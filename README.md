# Chromium_extensions_resolver
Give Text file with chromium extension IDs and it will produce results.txt file with extension ids and extension names. 
This can parse any chromium based extensions I think brave, chrome, edge etc. I have only tried on Chrome and Brave. 
 
### Usage
1. create a text file with name "extensions.txt" and add all extension ids - one extension per line
like:
```
ifclboecfhkjbpmhgehodcjpciihhmif
dmkamcknogkgcdfhhbddcghachkejeap
ookjlbkiijinhpmnjffcofjonbfbgaoc
oafedfoadhdjjcipmcbecikgokpaphjk
```
2. keep it in the same directory where you will download this python script

3. run `python3.exe chromium_extensions_resolver.py`

4. it will create results.txt in the same file 
![image](https://github.com/user-attachments/assets/5a7c8fa8-fe1a-467d-870a-66fe3a846da5)


### Note:
you might need to install some modules, install like below
`python3.exe -m pip install requests beautifulsoup4 selenium`

python3.exe = could be any python3 version you are using. python3.6.exe, etc...

