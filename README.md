# urlfind
urlfind é um script que busca por urls e subdomínios

# Instalação da Ferramenta
```sh
git clone https://github.com/yHunterDep/urlfind/
cd urlfind/
pip3 install -r requirements.txt
```

# Help da Ferrameta
```sh
python3 urlfind.py -h

usage: urlfind.py [-h] -d DOMAIN [-p] [-gs] [-o OUTPUT] [-s]

options:
  -h, --help            show this help message and exit
  -d DOMAIN, --domain DOMAIN
                        scaniar um domínio, exemplo: python3 urlfind.py -d
                        vulnweb.com
  -p, --params          pega apenas parâmetros
  -gs, --get_subs       este comando filtra os subdomínios
  -o OUTPUT, --output OUTPUT
                        salvar resultado em um arquivo de texto
  -s, --silent          não mostrar o banner
```

# Encontrando urls com urlfind
```sh
python3 urlfind.py -d vulnweb.com
```

# Salvar resultados em arquivos de texto
```sh
python3 urlfind.py -d vulnweb.com --output arquivo.txt
python3 urlfind.py -d vulnweb.com -o arquivo.txt
```

# Pegando só os parâmetros e salvando
```sh
python3 urlfind.py -d vulnweb.com --params
python3 urlfind.py -d vulnweb.com -p
python3 urlfind.py -d vulnweb.com --params --output parametros.txt
```

# Pegando subdomínios com Urlfind e salvando
```sh
python3 urlfind.py -d vulnweb.com --get_subs
python3 urlfind.py -d vulnweb.com -gs
python3 urlfind.py -d vulnweb.com --get_subs --output subdominios.txt 
```

# OneLine => urlfind + httpX + nuclei
```sh
python3 urlfind.py -d vulnweb.com --get_subs --silent | httpx --silent | nuclei
```

# Não mostrar o Banner
```sh
python3 urlfind.py -d vulnweb.com --silent
python3 urlfind.py -d vulnweb.com -s
```
