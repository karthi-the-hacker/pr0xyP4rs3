# pr0xyP4rs3

# Load any recon data into burp in just Single click  


![alt text](https://raw.githubusercontent.com/karthi-the-hacker/pr0xyP4rs3/main/logo.gif)

im Happy to say this you dont need to install any third party service to run my tool 😃
its pure Python ❤️️

Steps to install :



0. mkdir ~/recon &>/dev/null
1. mkdir ~/tools &>/dev/null
2. cd ~/tools/
3. git clone https://github.com/karthi-the-hacker/pr0xyP4rs3.git
4. cd pr0xyP4rs3
5. chmod +x *
6. chmod +x install.sh
7. Now Open burp 
8. Got to proxy and select option
9. Now click add 
10. use this proxy host = 127.0.0.1 port = 7777

# Syntax :

# For Single Domain or url 
      python pr0xyP4rs3.py -p http://yourserver.com/
       
# For multiple domain or Url 
      cat live-domain.txt | xargs -n1 -p50 python pr0xyP4rs3.py --parse
      
# Happy hacking 💀
# Jai Hind 🇮🇳
