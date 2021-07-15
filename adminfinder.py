
from colorama import Fore, init
import requests

# colors
red = Fore.RED
green = Fore.GREEN
blue = Fore.CYAN
yellow = Fore.YELLOW
reset = Fore.RESET

# color init
init(autoreset=True)

def auto(nig,url,l,time):
    try:
        obj2 = requests.get(url+"/"+nig, timeout=time, allow_redirects=False)
        # bytes
        by = len(obj2.text)
        if l == 20:
            print(f"{blue}[{yellow}?{blue}] - ({yellow}{l}{blue}) REQS, this might take awhile ")
        if obj2.status_code == 302:
            print(
                f"{blue}[{green}+{blue}] Code ({yellow}{obj2.status_code}{blue}) | REQS ({yellow}{l}{blue}) | BYTES ({yellow}{by}{blue}) - " + obj2.url + f" {green}>> {yellow}{obj2.headers['location']}")
            return
        if l == 100 and obj2.status_code == 302:
            print(f"{blue}[{red}!{blue}] - 404, might just be just going back to home ")
        if obj2.status_code == 404:
            pass
        else:
            if "admin portal" in obj2.text:
                print(
                    f"{blue}[{green}+{blue}] Code ({yellow}{obj2.status_code}{blue}) | REQS ({yellow}{l}{blue}) | BYTES ({yellow}{by}{blue}) - " + obj2.url + f" ({green}FOUND admin panel{blue})")
                return
            elif "admin" in obj2.text:
                print(
                    f"{blue}[{green}+{blue}] Code ({yellow}{obj2.status_code}{blue}) | REQS ({yellow}{l}{blue}) | BYTES ({yellow}{by}{blue}) - " + obj2.url + f" ({green}FOUND admin panel{blue})")
                return
            elif "admin login" in obj2.text:
                print(
                    f"{blue}[{green}+{blue}] Code ({yellow}{obj2.status_code}{blue}) | REQS ({yellow}{l}{blue}) | BYTES ({yellow}{by}{blue}) - " + obj2.url + f" ({green}FOUND admin panel{blue})")
                return
            elif "portal manager" in obj2.text:
                print(
                    f"{blue}[{green}+{blue}] Code ({yellow}{obj2.status_code}{blue}) | REQS ({yellow}{l}{blue}) | BYTES ({yellow}{by}{blue}) - " + obj2.url + f" ({green}FOUND admin panel{blue})")
                return

            elif "admin manager" in obj2.text:
                print(
                    f"{blue}[{green}+{blue}] Code ({yellow}{obj2.status_code}{blue}) | REQS ({yellow}{l}{blue}) | BYTES ({yellow}{by}{blue}) - " + obj2.url + f" ({green}FOUND admin panel{blue})")
                return
            print(f"{blue}[{green}+{blue}] Code ({yellow}{obj2.status_code}{blue}) | REQS ({yellow}{l}{blue}) | BYTES ({yellow}{by}{blue}) - "+obj2.url+"/")
    except requests.exceptions.ReadTimeout:
        # request timeout
        print(f"{blue}[{red}!{blue}] - Connection timeout ")
        return

def status(url):
    # checks the status of input url
    try:
        obj = requests.get(url, timeout=5)
        if obj.status_code == 404:
            print(f"{blue}[{red}!{blue}] - Look's like site is responding with a 404? ")
            exit(0)
        return
    except requests.exceptions.ReadTimeout:
        # request timeout
        print(f"{blue}[{red}!{blue}] - Look's like site is not responding ")
        return




def searcher(url, time):
    # checks if it is a valid url
    if "https://" in url or "http://" in url:
        pass
    else:
        print(f"{blue}[{red}!{blue}] - Not a valid url")
        return

    # checks if site responds with a valid status code
    status(url)
    print(f"{blue}[{green}+{blue}] Site - seems to be online")
    with open("paths.txt", 'r') as f:
        buf = f.readlines()
        if buf[-1] == '\n':
            buf = buf[:-1]
        urls = [x[:-1] for x in buf]
        l = 0
        for nig in urls:
            l += 1
            by = len(f.read())
            auto(nig,url,l, time)
        print(f"{blue}[{green}+{blue}] Total Requests - "+ str(l))



if __name__ == '__main__':
    # main thread

    url = input(f"url -> ")
    time = int(input("timeouts -> "))

    searcher(url, time)