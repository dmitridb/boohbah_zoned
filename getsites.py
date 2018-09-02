import itertools, operator
import requests
import sys
import time

def get_hosts(hosts):
    print("Downloading list " + hosts)
    response = requests.get(hosts)
    return returnhostonly(response.text)

def returnhostonly(text):
    returnval = []
    for host in text.splitlines():
        if "#" in host:
            continue
        else:
            print(host)
            split = host.split()
            if len(split) < 2:
                continue
            returnval.append(split[1])
    return returnval


pornhosts = get_hosts("https://raw.githubusercontent.com/Clefspeare13/pornhosts/master/0.0.0.0/hosts")
sinofetta = get_hosts("https://raw.githubusercontent.com/Sinfonietta/hostfiles/master/pornography-hosts")
# This section of code is disabled, uncomment it if you want it to block non-porn too
#combined = get_hosts("https://raw.githubusercontent.com/StevenBlack/hosts/master/hosts")

print("Combining and filtering porn lists for duplicate entries...")
porndupsort = [ x for x in pornhosts if x not in sinofetta ]

#print("Combining and filtering regular blocklist to nullroute...")
#nullsort = [x for x in combined if x not in porndupsort]

porndupsort = [ "209.250.255.198 " + domain for domain in porndupsort]
#nullsort = ["0.0.0.0 " + domain for domain in nullsort]

print(porndupsort)
print("^^^PORNDUPSORT^^^")
time.sleep(5)
#print(nullsort)
#print("^^^NULLSORT^^^")

#sorted_combined = nullsort + porndupsort

hostsfile_win = open('hosts_win', 'w+')
hostsfile_linux = open('hosts_linux', 'w+')

print("Writing hosts file for windows...")
#for line in sorted_combined:
for line in porndupsort:
    hostsfile_win.write(line + "\r\n")
hostsfile_win.close()

print("Writing hosts file for linux...")
#for line in sorted_combined:
for line in porndupsort:
    hostsfile_linux.write(line + "\n")
hostsfile_linux.close()

print("""\n
Done!

You may now use the files created here to fuck with people!

Feel free to install it on your employee's workstations, your sibling's laptop, on public
computers where some idiot has absolutely no discretion to figure its rude as fuck to look
at porn on a public computer like I had originally written it for -- pretty muchwherever
it may be hilarious to hear someone in an adjacent room rage over the fact that the only
porn they can now get is the boohbah zone. Pop the file on a usb stick, mail it to yourself
or whatever you think would be easiest, and do the following:

For windows, save the file hosts_win into the following directory with the following filename
(Be sure to rename it from "hosts_win" to just "hosts"!):
C:\Windows\System32\drivers\etc\hosts

For linux/mac, save the file hosts_linux into here (same advice applies, makes sure it's just
named /etc/hosts and not /etc/hosts_linux or anything):
/etc/hosts

Enjoy! If the provided IP address doesn't work anymore, feel free to set it to something else.
""")
