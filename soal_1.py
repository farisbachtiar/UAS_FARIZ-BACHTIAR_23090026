def tambah_mahasiswa():
    mahasiswa = []
    
    while True:
        nim = input("Masukkan NIM: ")
        nama = input("Masukkan Nama: ")
        mahasiswa.append({'NIM': nim, 'Nama': nama})
        
        lagi = input("Ingin tambah lagi? (ya/tidak): ").lower()
        if lagi != 'ya':
            break
    
    print("\nData Mahasiswa:")
    for data in mahasiswa:
        print(f"NIM: {data['NIM']}, Nama: {data['Nama']}")
    
    print("End")

tambah_mahasiswa()
