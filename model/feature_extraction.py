from urllib.parse import urlparse
import re

PHISHING_KEYWORDS = [
    "login","verify","secure","account","update",
    "bank","confirm","password","paypal","signin"
]

def has_ip(url):
    return 1 if re.search(r'(?:\d{1,3}\.){3}\d{1,3}', url) else 0


def extract_features(url):
    parsed = urlparse(url)

    suspicious_tlds = ['.tk', '.ml', '.ga', '.cf', '.gq']
    tld_flag = 1 if any(tld in parsed.netloc for tld in suspicious_tlds) else 0

    shorteners = ['bit.ly', 'tinyurl.com', 'goo.gl', 'ow.ly', 't.co']
    shortener_flag = 1 if any(shortener in url for shortener in shorteners) else 0

    long_url = 1 if len(url) > 75 else 0

    keyword_count = sum(url.lower().count(word) for word in PHISHING_KEYWORDS)

    features = [
        len(url),                        # 1
        len(parsed.netloc),              # 2
        len(parsed.path),                # 3
        url.count("."),                 # 4
        url.count("-"),                 # 5
        url.count("@"),                 # 6
        url.count("?"),                 # 7
        url.count("="),                 # 8
        sum(c.isdigit() for c in url),  # 9
        sum(c.isalpha() for c in url),  # 10
        sum(not c.isalnum() for c in url), # 11
        1 if parsed.scheme == "https" else 0, # 12
        has_ip(url),                    # 13
        parsed.netloc.count("."),       # 14
        keyword_count,                  # 15
        tld_flag,                       # 16
        shortener_flag,                 # 17
        long_url                        # 18
    ]

    return features