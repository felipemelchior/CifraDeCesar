try:
	import colorama
	from colorama import Fore, Back, Style
except ImportError:
	print("ERRO! - Necessario biblioteca COLORAMA \n Instale com - easy_install colorama")

colorama.init()

def desenhaBanner():
	banner = """
 ██████╗██╗███████╗██████╗  █████╗     ██████╗ ███████╗     ██████╗███████╗███████╗ █████╗ ██████╗ 
██╔════╝██║██╔════╝██╔══██╗██╔══██╗    ██╔══██╗██╔════╝    ██╔════╝██╔════╝██╔════╝██╔══██╗██╔══██╗
██║     ██║█████╗  ██████╔╝███████║    ██║  ██║█████╗      ██║     █████╗  ███████╗███████║██████╔╝
██║     ██║██╔══╝  ██╔══██╗██╔══██║    ██║  ██║██╔══╝      ██║     ██╔══╝  ╚════██║██╔══██║██╔══██╗
╚██████╗██║██║     ██║  ██║██║  ██║    ██████╔╝███████╗    ╚██████╗███████╗███████║██║  ██║██║  ██║
 ╚═════╝╚═╝╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝    ╚═════╝ ╚══════╝     ╚═════╝╚══════╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝
 			Criado por Felipe Homrich Melchior - UNIPAMPA
 	        		www.homdreen.github.io
 			caesarcipher.py --help para mais funções

 			- [1] - CRIPTOGRAFAR
 			- [2] - DESCRIPTOGRAFAR SEM CHAVE
 			- [3] - DESCRIPTOGRAFAR COM CHAVE

 			"""

	print(Fore.WHITE+banner)

def desenhaCript():
	banner = """ 
 ██████╗██████╗ ██╗██████╗ ████████╗ ██████╗  ██████╗ ██████╗  █████╗ ███████╗ █████╗ 
██╔════╝██╔══██╗██║██╔══██╗╚══██╔══╝██╔═══██╗██╔════╝ ██╔══██╗██╔══██╗██╔════╝██╔══██╗
██║     ██████╔╝██║██████╔╝   ██║   ██║   ██║██║  ███╗██████╔╝███████║█████╗  ███████║
██║     ██╔══██╗██║██╔═══╝    ██║   ██║   ██║██║   ██║██╔══██╗██╔══██║██╔══╝  ██╔══██║
╚██████╗██║  ██║██║██║        ██║   ╚██████╔╝╚██████╔╝██║  ██║██║  ██║██║     ██║  ██║
 ╚═════╝╚═╝  ╚═╝╚═╝╚═╝        ╚═╝    ╚═════╝  ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚═╝  ╚═╝


 """

	print(Fore.YELLOW+banner)

def desenhaDecript():
	banner = """
██████╗ ███████╗███████╗ ██████╗██████╗ ██╗██████╗ ████████╗ ██████╗  ██████╗ ██████╗  █████╗ ███████╗ █████╗ 
██╔══██╗██╔════╝██╔════╝██╔════╝██╔══██╗██║██╔══██╗╚══██╔══╝██╔═══██╗██╔════╝ ██╔══██╗██╔══██╗██╔════╝██╔══██╗
██║  ██║█████╗  ███████╗██║     ██████╔╝██║██████╔╝   ██║   ██║   ██║██║  ███╗██████╔╝███████║█████╗  ███████║
██║  ██║██╔══╝  ╚════██║██║     ██╔══██╗██║██╔═══╝    ██║   ██║   ██║██║   ██║██╔══██╗██╔══██║██╔══╝  ██╔══██║
██████╔╝███████╗███████║╚██████╗██║  ██║██║██║        ██║   ╚██████╔╝╚██████╔╝██║  ██║██║  ██║██║     ██║  ██║
╚═════╝ ╚══════╝╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝╚═╝        ╚═╝    ╚═════╝  ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚═╝  ╚═╝
							                      SEM CHAVE


							                      """
	
	print(Fore.YELLOW+banner)

def desenhaDecriptKey():
	banner = """
██████╗ ███████╗███████╗ ██████╗██████╗ ██╗██████╗ ████████╗ ██████╗  ██████╗ ██████╗  █████╗ ███████╗ █████╗ 
██╔══██╗██╔════╝██╔════╝██╔════╝██╔══██╗██║██╔══██╗╚══██╔══╝██╔═══██╗██╔════╝ ██╔══██╗██╔══██╗██╔════╝██╔══██╗
██║  ██║█████╗  ███████╗██║     ██████╔╝██║██████╔╝   ██║   ██║   ██║██║  ███╗██████╔╝███████║█████╗  ███████║
██║  ██║██╔══╝  ╚════██║██║     ██╔══██╗██║██╔═══╝    ██║   ██║   ██║██║   ██║██╔══██╗██╔══██║██╔══╝  ██╔══██║
██████╔╝███████╗███████║╚██████╗██║  ██║██║██║        ██║   ╚██████╔╝╚██████╔╝██║  ██║██║  ██║██║     ██║  ██║
╚═════╝ ╚══════╝╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝╚═╝        ╚═╝    ╚═════╝  ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚═╝  ╚═╝
							                      COM CHAVE


							                      """
	
	print(Fore.YELLOW+banner)