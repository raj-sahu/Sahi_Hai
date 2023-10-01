import os
import re
import whois
import urllib.parse
from datetime import datetime
from bs4 import BeautifulSoup
from dotenv import load_dotenv

load_dotenv()

LOCALHOST_PATH = os.getenv("LOCALHOST_PATH")
DIRECTORY_NAME = os.getenv("DIRECTORY_NAME")

ipv4_pattern = r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b"
ipv6_pattern = r"(([0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}|" \
               "([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|" \
               "([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|" \
               "([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|" \
               "([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|" \
               "([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|" \
               "[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|" \
               ":((:[0-9a-fA-F]{1,4}){1,7}|:)|" \
               "fe80:(:[0-9a-fA-F]{0,4}){0,4}%[0-9a-zA-Z]{1,}|" \
               "::(ffff(:0{1,4}){0,1}:){0,1}" \
               "((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}" \
               "(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])|" \
               "([0-9a-fA-F]{1,4}:){1,4}:" \
               "((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}" \
               "(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9]))"

shortening_services = r"bit\.ly|t\.co|tinyurl\.com|ow\.ly|w\.ly|is\.gd|cli\.gs|" \
                      "shorte\.st|po\.st|post\.pl|bc\.vc|twtr\.com|ht\.ly|ad\.f ly|" \
                      "bit-do\.com|viralurl\.com|t2m\.io|x\.co|goo\.gl|tr\.im|" \
                      "su\.pr|ity\.im|q\.gs|po\.st|vur\.me|s2r\.co|lnk\.co|ity\.im|" \
                      "vzturl\.com|qr\.net|t\.co|1url\.com|tweez\.me|v\.gd|trb\.li|" \
                      "mcaf\.ee|v\.gd|trb\.li|aka\.gr|to\.ly|tiny\.cc|lnkd\.in|lnkd\.in|sh\.st"

http_https = r"https?://[^\s/$.?#].[^\s]*"


def get_hostname_from_url(url):
    # Extract the hostname from a URL
    parsed_url = urllib.parse.urlparse(url)
    return parsed_url.netloc


def having_ip_address(url):
    ip_address_pattern = ipv4_pattern + "|" + ipv6_pattern
    match = re.search(ip_address_pattern, url)
    return -1 if match else 1


def url_length(url):
    if len(url) < 54:
        return 1
    elif 54 <= len(url) <= 75:
        return 0
    return -1


def shortening_service(url):
    match = re.search(shortening_services, url)
    return -1 if match else 1


def having_at_symbol(url):
    match = re.search('@', url)
    return -1 if match else 1


def double_slash_redirecting(url):
    last_double_slash = url.rfind('//')
    return -1 if last_double_slash > 6 else 1


def prefix_suffix(domain):
    match = re.search('-', domain)
    return -1 if match else 1


def having_sub_domain(url):
    if having_ip_address(url) == -1:
        match = re.search(
            '(([01]?\\d\\d?|2[0-4]\\d|25[0-5])\\.([01]?\\d\\d?|2[0-4]\\d|25[0-5])\\.([01]?\\d\\d?|2[0-4]\\d|25[0-5])\\.'
            '([01]?\\d\\d?|2[0-4]\\d|25[0-5]))|(?:[a-fA-F0-9]{1,4}:){7}[a-fA-F0-9]{1,4}',
            url)
        pos = match.end()
        url = url[pos:]
    num_dots = [x.start() for x in re.finditer(r'\.', url)]
    if len(num_dots) <= 3:
        return 1
    elif len(num_dots) == 4:
        return 0
    else:
        return -1


def domain_registration_length(domain):
    expiration_date = domain.expiration_date
    today = datetime.now()
    registration_length = 0

    if expiration_date:
        registration_length = (expiration_date - today).days

    return -1 if registration_length <= 365 else 1


def favicon(url, soup, domain):
    for head in soup.find_all('head'):
        for head_link in soup.find_all('link', href=True):
            dots = [x.start() for x in re.finditer(r'\.', head_link['href'])]
            return 1 if domain in head_link['href'] or len(dots) == 1 else -1
    return 1


def https_token(url):
    match = re.search(http_https, url)

    if match and match.start() == 0:
        url = url[match.end():]
    match = re.search('http|https', url)
    return -1 if match else 1


def request_url(wiki, soup, domain):
    i = 0
    success = 0
    for img in soup.find_all('img', src=True):
        dots = [x.start() for x in re.finditer(r'\.', img['src'])]
        if wiki in img['src'] or domain in img['src'] or len(dots) == 1:
            success = success + 1
        i = i + 1

    for audio in soup.find_all('audio', src=True):
        dots = [x.start() for x in re.finditer(r'\.', audio['src'])]
        if wiki in audio['src'] or domain in audio['src'] or len(dots) == 1:
            success = success + 1
        i = i + 1

    for embed in soup.find_all('embed', src=True):
        dots = [x.start() for x in re.finditer(r'\.', embed['src'])]
        if wiki in embed['src'] or domain in embed['src'] or len(dots) == 1:
            success = success + 1
        i = i + 1

    for iframe in soup.find_all('iframe', src=True):
        dots = [x.start() for x in re.finditer(r'\.', iframe['src'])]
        if wiki in iframe['src'] or domain in iframe['src'] or len(dots) == 1:
            success = success + 1
        i = i + 1

    try:
        percentage = success / float(i) * 100
    except ZeroDivisionError:
        return 1

    if percentage < 22.0:
        return 1
    elif 22.0 <= percentage < 61.0:
        return 0
    else:
        return -1


def url_of_anchor(wiki, soup, domain):
    i = 0
    unsafe = 0
    for a in soup.find_all('a', href=True):
        if "#" in a['href'] or "javascript" in a['href'].lower() or "mailto" in a['href'].lower() or not (
                wiki in a['href'] or domain in a['href']):
            unsafe = unsafe + 1
        i = i + 1

    try:
        percentage = unsafe / float(i) * 100
    except ZeroDivisionError:
        return 1

    if percentage < 31.0:
        return 1
    elif 31.0 <= percentage < 67.0:
        return 0
    else:
        return -1


def links_in_tags(wiki, soup, domain):
    i = 0
    success = 0
    for link in soup.find_all('link', href=True):
        dots = [x.start() for x in re.finditer(r'\.', link['href'])]
        if wiki in link['href'] or domain in link['href'] or len(dots) == 1:
            success = success + 1
        i = i + 1

    for script in soup.find_all('script', src=True):
        dots = [x.start() for x in re.finditer(r'\.', script['src'])]
        if wiki in script['src'] or domain in script['src'] or len(dots) == 1:
            success = success + 1
        i = i + 1

    try:
        percentage = success / float(i) * 100
    except ZeroDivisionError:
        return 1

    if percentage < 17.0:
        return 1
    elif 17.0 <= percentage < 81.0:
        return 0
    else:
        return -1


def sfh(wiki, soup, domain):
    for form in soup.find_all('form', action=True):
        if form['action'] == "" or form['action'] == "about:blank":
            return -1
        elif wiki not in form['action'] and domain not in form['action']:
            return 0
        else:
            return 1
    return 1


def submitting_to_email(soup):
    for form in soup.find_all('form', action=True):
        return -1 if "mailto:" in form['action'] else 1
    return 1


def abnormal_url(domain, url):
    hostname = domain.name
    match = re.search(hostname, url)
    return 1 if match else -1


def i_frame(soup):
    for iframe in soup.find_all('iframe', width=True, height=True, frameborder=True):
        if iframe['width'] == "0" and iframe['height'] == "0" and iframe['frameborder'] == "0":
            return -1
        if iframe['width'] == "0" or iframe['height'] == "0" or iframe['frameborder'] == "0":
            return 0
    return 1


def age_of_domain(domain):
    creation_date = domain.creation_date
    expiration_date = domain.expiration_date
    age_of_domain = 0
    if expiration_date and creation_date:
        age_of_domain = abs((expiration_date - creation_date).days)
    return -1 if age_of_domain < 182 else 1


def web_traffic(url):

    return 1


def google_index(url):
 
    return 1


def statistical_report(url, domain):

    return 1


def main(url):
    with open(LOCALHOST_PATH + DIRECTORY_NAME + '/markup.txt', 'rb') as file:
        soup_string = file.read()

    soup = BeautifulSoup(soup_string, 'html.parser')

    status = []
    hostname = get_hostname_from_url(url)

    status.append(having_ip_address(url))
    status.append(url_length(url))
    status.append(shortening_service(url))
    status.append(having_at_symbol(url))
    status.append(double_slash_redirecting(url))
    status.append(prefix_suffix(hostname))
    status.append(having_sub_domain(url))

    dns = 1
    try:
        domain = whois.whois(hostname)
    except:
        dns = -1

    status.append(-1 if dns == -1 else domain_registration_length(domain))

    status.append(favicon(url, soup, hostname))
    status.append(https_token(url))
    status.append(request_url(url, soup, hostname))
    status.append(url_of_anchor(url, soup, hostname))
    status.append(links_in_tags(url, soup, hostname))
    status.append(sfh(url, soup, hostname))
    status.append(submitting_to_email(soup))

    status.append(-1 if dns == -1 else abnormal_url(domain, url))

    status.append(i_frame(soup))

    status.append(-1 if dns == -1 else age_of_domain(domain))

    status.append(dns)

    status.append(web_traffic(url))
    status.append(google_index(url))
    status.append(statistical_report(url, hostname))

    print('\n1. Having IP address\n2. URL Length\n3. URL Shortening service\n4. Having @ symbol\n'
          '5. Having double slash\n6. Having dash symbol (Prefix Suffix)\n7. Having multiple subdomains\n'
          '8. SSL Final State\n9. Domain Registration Length\n10. Favicon\n11. HTTP or HTTPS token in domain name\n'
          '12. Request URL\n13. URL of Anchor\n14. Links in tags\n15. SFH (Server Form Handler)\n16. Submitting to email\n'
          '17. Abnormal URL\n18. IFrame\n19. Age of Domain\n20. DNS Record\n21. Web Traffic\n22. Google Index\n23. Statistical Reports\n')
    print(status)
    return status


if __name__ == "__main__":
    main("https://breakingcode.wordpress.com/2010/06/29/google-search-python/")
