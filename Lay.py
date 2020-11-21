import os,time,sys,shutil

class Main:
	def __init__(self):
		self.detekos()
		def menu(self):
			print("""1. SMS Gratis 
			         2. Matahari
			         3. Halo Dokter
			         4. OLX
			         5. Sociolla """)
		
		pilih=int(input('Type Key/> '))
		if pilih == 1:
			import src.payu
		elif pilih == 2:
			import src.matahari
		elif pilih == 3:
			import src.alodok
		elif pilih == 4:
			import src.olx
		elif pilih == 5:
			import src.socil
		else: print("[!] Salah Ketik Goblok(o)");self.menu()
		
		def detekos(self):
			#remove cache
			try:
				shutil.rmtree("src/__pycache__")
				except: pass
				if os.name in ['nt','win32']:
					os.system('cls')
					else: os.system('clear')
					self.menu()
					try:
						Main()
						except KeyboardInterrupt:
							exit('[Exit] Key interrupt')
							except Exception as F:
								print('Error Anjing: %s'%(F))
