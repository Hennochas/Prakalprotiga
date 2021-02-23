#Hennoch Azarya Saragih
#71200636
#Universita Kristen Duta Wacana
#Sumber : Buat sendiri 

'''
seorang wartawan mempunyai data skala ritcher gempa dari terkecil yaitu 4.5 sampai 8
tetapi ia tidak tau jika skala ricther 4.5 dan seterusnya bentuk bangunan yang terjadi itu bagaimana,
sebagai programmer kami membantunya jika wartawan memasukan skala ricther dari terkecil 4.5 
dan seterusnya maka ia dapat mengetahui bentuk bangunan yang terjadi seperti apa

'''

'''
input : 
a = 4.5
b = 6
c = 7
d = 8
 
proses : 
jika skala < 6 maka kondisi bangun rusak ringan 


output :
Kondisi bangunan 

'''
sr = float(input('Masukan Skalar :'))
if(sr >= 4.5 and sr < 6):
    print("Beberapa Bangunan Rusak Ringan" )
elif(sr >= 6 and sr < 7) :
    print('Beberapa Bangunan Rusak Parah')
elif(sr >= 7 and sr <8):
    print('Banyak Bangunan Rusak Parah')
elif(sr >=8):
    print('Semua Bangunan Rata Dengan Tanah')
else:
    print('tak terdefinisi')