# nessus-html-report-parser
This is a simple tool written in pyhon3. The objective the tool is to parse and scan vulnerabilities report provided by nessus scan and then fetch the list of recommende packages with versions that need  to be upgraded to fix the vulnerabilities.

# Dependencies
pip3 install bs4
pip3 install requests

# Config Requirement
In file `nessus-html-report-parser.py` you need to modify 2/3 constants from the tool source to make it work.
1. Copy the `nessus-report.html` file on your system in local directory. Change the name of `NESSUS_SCAN_HTML` constant as per the file name of your report.
2. Provide the `BASE_OS_NAME` for which you're looking to fix the vulnerabilities.
3. [OPTIONAL]: Provide the `Severity tags` list under `SEVERITY_TAGS_LIST` constant from the script.


# Sample Output
```
(virtual-env) virtual@baremetal-vm:~$ python3 nessus-html-report-parser.py
Ubuntu 20.04 not found for Critical => https://www.tenable.com/plugins/nessus/164287 => https://ubuntu.com/security/notices/USN-5573-1 => 13179
Ubuntu 20.04 not found for Critical => https://www.tenable.com/plugins/nessus/182769 => https://ubuntu.com/security/notices/USN-6420-1 => 13865
Ubuntu 20.04 not found for Critical => https://www.tenable.com/plugins/nessus/169583 => https://ubuntu.com/security/notices/USN-5787-1 => 13094
Ubuntu 20.04 not found for Critical => https://www.tenable.com/plugins/nessus/182907 => https://ubuntu.com/security/notices/USN-6429-1 => 13257
Critical List
1 => https://www.tenable.com/plugins/nessus/166264 => {'libksba8': '1.3.5-2ubuntu0.20.04.1'}
2 => https://www.tenable.com/plugins/nessus/171011 => {'libpam-modules': '1.3.1-5ubuntu4.6'}
3 => https://www.tenable.com/plugins/nessus/170644 => {'libpam-modules': '1.3.1-5ubuntu4.4'}
4 => https://www.tenable.com/plugins/nessus/170001 => {'libgssapi3-heimdal': '7.7.0+dfsg-1ubuntu1.3', 'libhdb9-heimdal': '7.7.0+dfsg-1ubuntu1.3', 'libasn1-8-heimdal': '7.7.0+dfsg-1ubuntu1.3', 'libkrb5-26-heimdal': '7.7.0+dfsg-1ubuntu1.3', 'libhx509-5-heimdal': '7.7.0+dfsg-1ubuntu1.3'}
5 => https://www.tenable.com/plugins/nessus/166262 => {'git': '1:2.25.1-1ubuntu3.6'}
6 => https://www.tenable.com/plugins/nessus/170111 => {'git': '1:2.25.1-1ubuntu3.7'}
7 => https://www.tenable.com/plugins/nessus/160502 => {'libssl1.1': '1.1.1f-1ubuntu2.13'}
8 => https://www.tenable.com/plugins/nessus/162424 => {'openssl': '1.1.1f-1ubuntu2.15'}
9 => https://www.tenable.com/plugins/nessus/166561 => {'libcurl3-gnutls': '7.68.0-1ubuntu2.14', 'libcurl3-nss': '7.68.0-1ubuntu2.14', 'libcurl4': '7.68.0-1ubuntu2.14', 'curl': '7.68.0-1ubuntu2.14'}
10 => https://www.tenable.com/plugins/nessus/173037 => {'libcurl3-gnutls': '7.68.0-1ubuntu2.18', 'libcurl3-nss': '7.68.0-1ubuntu2.18', 'libcurl4': '7.68.0-1ubuntu2.18', 'curl': '7.68.0-1ubuntu2.18'}
11 => https://www.tenable.com/plugins/nessus/165204 => {'sqlite3': '3.31.1-4ubuntu0.4'}
12 => https://www.tenable.com/plugins/nessus/178755 => {'openssh-client': '1:8.2p1-4ubuntu0.8'}
13 => https://www.tenable.com/plugins/nessus/149417 => {'python-yaml': '5.3.1-1ubuntu0.1', 'python3-yaml': '5.3.1-1ubuntu0.1'}
High List
14 => https://www.tenable.com/plugins/nessus/171942 => {'libcurl3-gnutls': '7.68.0-1ubuntu2.16', 'libcurl3-nss': '7.68.0-1ubuntu2.16', 'libcurl4': '7.68.0-1ubuntu2.16', 'curl': '7.68.0-1ubuntu2.16'}
15 => https://www.tenable.com/plugins/nessus/157143 => {'vim': '2:8.1.2269-1ubuntu5.6'}
16 => https://www.tenable.com/plugins/nessus/159711 => {'gzip': '1.10-0ubuntu4.1'}
18 => https://www.tenable.com/plugins/nessus/159714 => {'xz-utils': '5.2.4-1ubuntu1.1'}
19 => https://www.tenable.com/plugins/nessus/185342 => {'python3-urllib3': '1.25.8-2ubuntu0.3'}
20 => https://www.tenable.com/plugins/nessus/165290 => {'bind9': '1:9.16.1-0ubuntu2.11'}
25 => https://www.tenable.com/plugins/nessus/183537 => {'iperf3': 'Ubuntu Pro', 'libiperf0': 'Ubuntu Pro'}
26 => https://www.tenable.com/plugins/nessus/171483 => {'git': '1:2.25.1-1ubuntu3.10'}
27 => https://www.tenable.com/plugins/nessus/174458 => {'libxml2-utils': '2.9.10+dfsg-5ubuntu0.20.04.6', 'libxml2': '2.9.10+dfsg-5ubuntu0.20.04.6'}
28 => https://www.tenable.com/plugins/nessus/171212 => {'libgssapi3-heimdal': '7.7.0+dfsg-1ubuntu1.4'}
29 => https://www.tenable.com/plugins/nessus/168489 => {'libwind0-heimdal': '7.7.0+dfsg-1ubuntu1.2'}
30 => https://www.tenable.com/plugins/nessus/174961 => {'git': '1:2.25.1-1ubuntu3.11'}
31 => https://www.tenable.com/plugins/nessus/176491 => {'libssl1.1': '1.1.1f-1ubuntu2.19'}
32 => https://www.tenable.com/plugins/nessus/163872 => {'libgnutls30': '3.6.13-2ubuntu1.7'}
33 => https://www.tenable.com/plugins/nessus/167061 => {'libsqlite3-0': '3.31.1-4ubuntu0.5'}
34 => https://www.tenable.com/plugins/nessus/169585 => {'libcurl3-gnutls': '7.68.0-1ubuntu2.15', 'libcurl3-nss': '7.68.0-1ubuntu2.15', 'libcurl4': '7.68.0-1ubuntu2.15', 'curl': '7.68.0-1ubuntu2.15'}

```
# Errors
The line in the #sample output above, suggest that the tool was unable to fetch package list for plugin `164287`. 

`Ubuntu 20.04 not found for Critical => https://www.tenable.com/plugins/nessus/164287 => https://ubuntu.com/security/notices/USN-5573-1 => 13179`
