# nama: Muhamad fikri
# kelas: XI 2
# nomor absen: 19
# soal: Di sebuah toko online, Anda bertanggung jawab untuk menghitung diskonberdasarkan jumlah total belanjaan pelanggan. 
total_belanjaan = float(input("Total belanjaan Anda:"))

if total_belanjaan > 500000:
    diskon = total_belanjaan * 0.10
elif total_belanjaan >= 300000:
    diskon = total_belanjaan * 0.05
else:
    diskon = 0

total_pembayaran = total_belanjaan - diskon
print(f"Total pembayaran setelah diskon: {total_pembayaran}")



