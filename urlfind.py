import requests
import argparse
import re

vermelho = "\033[31m"
verde = "\033[32m"
reset = "\033[0;0m"

banner = verde + """
                      ████     ██████   ███                 █████
                     ░░███    ███░░███ ░░░                 ░░███
 █████ ████ ████████  ░███   ░███ ░░░  ████  ████████    ███████
░░███ ░███ ░░███░░███ ░███  ███████   ░░███ ░░███░░███  ███░░███
 ░███ ░███  ░███ ░░░  ░███ ░░░███░     ░███  ░███ ░███ ░███ ░███
 ░███ ░███  ░███      ░███   ░███      ░███  ░███ ░███ ░███ ░███
 ░░████████ █████     █████  █████     █████ ████ █████░░████████
\n\t[+] Creator: HunterDep\n\t[>] Github: https://github.com/yHunterDep\n\t[*] Version: v0.1
""" + reset

def get_subs(urls):
	regex = "^https?://[a-z0-9\.-]+\.[a-z0-9\.-]+"
	urls = urls.split("\n")
	coletados = []
	for url in urls:
		subs = re.findall(regex, url)
		subs = "".join(subs)
		if not subs in coletados:
			coletados.append(subs)
			if output:
				arqv.write(subs+"\n")
	print(verde + "\n".join(coletados) + reset)

parser = argparse.ArgumentParser()
parser.add_argument("-d", "--domain", help="scaniar um domínio, exemplo: python3 urlfind.py -d vulnweb.com", required=True)
parser.add_argument("-p", "--params", help="pega apenas parâmetros", action="store_true")
parser.add_argument("-gs", "--get_subs", help="este comando filtra os subdomínios", action="store_true")
parser.add_argument("-o", "--output", help="salvar resultado em um arquivo de texto")
parser.add_argument("-s", "--silent", help="não mostrar o banner", action="store_true")
args = parser.parse_args()

dominio = args.domain
params_arg = args.params
gs = args.get_subs
output = args.output

if output:
	arqv = open(output, "w+")

if not args.silent:
	print(banner)

try:
	req = requests.get(f"https://web.archive.org/cdx/search/cdx?url=*.{dominio}/*&output=txt&collapse=urlkey&page=/&fl=original")
except Exception as z:
	print(f"{vermelho}[!]{reset} Erro na requisição!");quit()
urls = req.text

if gs:
	get_subs(urls)
	quit()

if not params_arg:
	print(verde + urls + reset)
	if output:
		arqv.write(urls)
else:
	urls = urls.split("\n")
	for url in urls:
		if "?" in url:
			print(verde + url + reset)
			if output:
				arqv.write(url+"\n")
