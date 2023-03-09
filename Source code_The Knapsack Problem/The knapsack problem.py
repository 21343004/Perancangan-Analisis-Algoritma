def knapSack(W, wt, val): # sebuah Deklarasi fungsi
    n=len(val)
    table = [[0 for x in range(W + 1)] for x in range(n + 1)]  # disini menggunakan loopbersarang untuk melintasi tabel dan mengisi seluruh setiap sel
 
    for i in range(n + 1): 
        for j in range(W + 1): 
            if i == 0 or j == 0: #Untuk menyetel baris dan kolom ke-0 menjadi 0
                table[i][j] = 0
            elif wt[i-1] <= j: # baris kode ini memeriksa bahwa bobot objek ke-i kurang dari bobot total yang diziinkan untuk sel j
                table[i][j] = max(val[i-1] #baris kode ini untuk memilih maksimal dari dua opsi yang tersedia 
+ table[i-1][j-wt[i-1]],  table[i-1][j]) #menyatakan bahwa item ke-i disertakan
            else: 
                table[i][j] = table[i-1][j]#Bagian loop ini diakses ketika bobot objek ke-i lebih besar dari batas yang diizinkan
   
    return table[n][W] 
 
val = [50,100,150,200] # Disini kita memasukan beberapa item 1, 2, dan 4
wt = [8,16,32,40]
W = 64
 
print(knapSack(W, wt, val))