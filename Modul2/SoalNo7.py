import TugasMhs            # Atau apapun file-nya yang kamu buat tadi

class MhsTIF(TugasMhs.Mahasiswa):    # perhatikan class induknya : Mahasiswa
    """Class MhsTIF yang dibangun dari class Mahasiswa"""
    def kataKanPy(self):
        print('Hallo Python.....')

print('Cara menjalankan namavar.MhsTIF(.....)')

# Apakah metode / state itu berasal dari class Manusia, Mahasiswa, atau MhsTIF?

# Jawab :

# Metoode atau state yang muncul berasal dari semua class yang telah dibuat sebelumnya
# Ini karena MhsTIF yang merupakan anak class dari Mahasiswa, dan itu membuat MhsTIF mewarisi
# semua properties dari Mahasiswa dan Manusia.
