from requests import get

RAM = [
    "UDAH GAK GUNA",
    "DI TAMBAH HINA",
    "MERANA PULA, LENGKAP KALI KEHIDUPAN KAU MACAM SINETRON DI INDOSIAR YANG SERING DI GUNA GUNA.",
    "MINIMAL NIH YA LU MANDI DULU",
    "TERUS LU MINTA BEDAKIN SAMA EMAK LU",
    "ABIS ITU BARU DAH LU NGAKU NGAKU KALO LU TUH PANJAHAT KELAMIN",
    "YAELAHH DONGOO KALI KAU DEKKUH",
    "BABU ALIANSI BANYAK KALII GAYANYA,UDAH GAK KERAS MASIH AJA BANYAK BACOTT",
    "CANTIKK SII TAPI SAYANGNYA BABU ALIANSI",
    "LAGI NYARI KOSAKATA YA DEKKUH DI GC LAINN, BHAKSSS",
    "EH BABU,KALO DI BILANGIN AMA YANG LEBIH TUA TUH JANGAN BATU NGENTOT,OTAK LU TUH LEMAH GOBLOK, DI KASIH TAU MALAH BATU NGENTOT KOSAKATA MASIH CARI DI GC LAEN BLAGUNYA BUKAN MAEN DEKKUHH !",
    "MENDING LU BUKA YOUTUBE CARI TUTORIAL KIYOMASA, DARI PADA TYPINGAN SAMPAH KAYA LU TOLOL, GAK BIKIN GEMETER",
    "GAK JELASS KONTOL MASIH KECIL,BIJINYA SEUKURAN KERIKIL",
    "HABIS COLI YA DEKKUH, PANTESSSS NAMBAH DONGO !",
    "ITU KAN KOSAKATANYA NGAMBIL !",
    "JANGAN KERAS-KERAS DEK, KERASNYA LU TUH CUMA DI DEPAN CEWE DOANG JADI JATOHNYA CAPER NGENTOT !",
    "KALO CUMA LU DOANG MAH IBARAT KATA KAYA GW LAWAN ANAK TK !",
    "Wa'alaikumsalam, ada apa?",
    "MUKA LU NGAMBIL DI PINTEREST KAN??GAK BERANI PAKE MUKA HINA LU YA TOLOL",
    "NIH DIA YANG GW TUNGGUIN DARI KEMAREN, DATENG JUGA SI BABU WUAHAHAHA",
    "ORANG MAH KALO GAK GUNA MINIMAL MAH MIKIRR DEKKUH, UDAH GAK GUNA BEBAN PULA MENDING MAEN POU AJA BERSIHIN TAI YANG KAYA MUKA LU, BHAKSS",
    "Assalamu'alaikum",
    "QUNYUKKKK BANYAK KALI LAGANYA, TAPI JATOHHNYA CAPER SIHH, CUIHH!",
    "RASANYA KOK KAYA GAK ADA APA APA YA, PADAHAL LU MAH UDAH BACOT PANJANG KALI LEBAR TAPI BELOM KERASA HADEHH",
    "SAYANG-SAYANG MENTAL LU NANTI DOWN KALO LAWAN GUA, BHAKSSS",
    "TERIMA KASIH KEK MINIMAL NGENTOT,UDAH GW KASIH TEMPAT LU UNTUK CAPER SANA SINI TOD",
    "UDAH HINA,BANYAK GAYA NGENTOT MASIH MENDING GW LADENIN",
    "NORAK ANJING MAENIN BOT TERUS KONTOL, NANTI DELLAY YANG DI SALAHIN BOT NYA MEMEK",
    "WAR-WAR TAI ANJING BABI,CUMA DATENG MODAL MENTAL TEMPE AJA BELAGU",
    "HAPENYA KENTANG,SOK MENANTANG",
    "MUKA LU TUH UDAH HINA, JADI JANGAN DIBUAT NAMBAH HINA NANTI HIDUP LU JADI GAK GUNA TOLOLL",
    "BANYAK GAYA TAPI BUKAN ORANG KAYA,BAPAK LU MASIH PAKE BAJU PARTAI DAPET DARI SOGOKAN NYOBLOS AJA UDAH GEDE LAGANYA",
]
GRP = "@GeezSupport|@ramsupportt"

Owners = "@jasadeak"

PORM = [
        "https://telegra.ph/file/9bcc076fd81dfe3feb291.mp4",
        "https://telegra.ph/file/b7a1a42429a65f64e67af.mp4",
        "https://telegra.ph/file/dc3da5a3eb77ae20fa21d.mp4",
        "https://telegra.ph/file/22b89774a4ba9219d530b.mp4",
        "https://telegra.ph/file/7b15fbca08ae1e73e559c.mp4",
        "https://telegra.ph/file/a9c1dea3f34925bb60686.mp4",
        "https://telegra.ph/file/913b4e567b7f435b7f0db.mp4",
        "https://telegra.ph/file/5a5d1a919a97af2314955.mp4",
        "https://telegra.ph/file/0f8b903669600d304cbe4.mp4",
        "https://telegra.ph/file/f3816b54c9eb7617356b6.mp4",
        "https://telegra.ph/file/516dbaa03fde1aaa70633.mp4",
        "https://telegra.ph/file/07bba6ead0f1e381b1bd1.mp4",
        "https://telegra.ph/file/0a4f7935df9b4ab8d62ed.mp4",
        "https://telegra.ph/file/40966bf68c0e4dbe18058.mp4",
        "https://telegra.ph/file/50637aa9c04d136687523.mp4",
        "https://telegra.ph/file/b81c0b0e491da73e64260.mp4",
        "https://telegra.ph/file/4ddf5f29783d92ae03804.mp4",
        "https://telegra.ph/file/4037dc2517b702cc208b1.mp4",
        "https://telegra.ph/file/33cebe2798c15d52a2547.mp4",
        "https://telegra.ph/file/4dc3c8b03616da516104a.mp4",
        "https://telegra.ph/file/6b148dace4d987fae8f3e.mp4",
        "https://telegra.ph/file/8cb081db4eeed88767635.mp4",
        "https://telegra.ph/file/98d3eb94e6f00ed56ef91.mp4",
        "https://telegra.ph/file/1fb387cf99e057b62d75d.mp4",
        "https://telegra.ph/file/6e1161f63879c07a1f213.mp4",
        "https://telegra.ph/file/0bf4defb9540d2fa6d277.mp4",
        "https://telegra.ph/file/d5f8280754d9aa5dffa6a.mp4",
        "https://telegra.ph/file/0f23807ed1930704e2bef.jpg",
        "https://telegra.ph/file/c49280b8f1dcecaf86c00.jpg",
        "https://telegra.ph/file/f483400ff141de73767ca.jpg",
        "https://telegra.ph/file/1543bbea4e3c1abb6764a.jpg",
        "https://telegra.ph/file/a0d77be0d769c7cd334ab.jpg",
        "https://telegra.ph/file/6c6e93860527d2f577df8.jpg",
        "https://telegra.ph/file/d987b0e72eb3bb4801f01.jpg",
        "https://telegra.ph/file/b434999287d3580250960.jpg",
        "https://telegra.ph/file/0729cc082bf97347988f7.jpg",
        "https://telegra.ph/file/bb96d25df82178a2892e7.jpg",
        "https://telegra.ph/file/be73515791ea33be92a7d.jpg",
        "https://telegra.ph/file/fe234d6273093282d2dcc.jpg",
        "https://telegra.ph/file/66254bb72aa8094d38250.jpg",
        "https://telegra.ph/file/44bdaf37e5f7bdfc53ac6.jpg",
        "https://telegra.ph/file/e561ee1e1ca88db7e8038.jpg",
        "https://telegra.ph/file/f1960ccfc866b29ea5ad2.jpg",
        "https://telegra.ph/file/97622cad291472fb3c4aa.jpg",
        "https://telegra.ph/file/a46e316b413e9dc43e91b.jpg",
        "https://telegra.ph/file/497580fc3bddc21e0e162.jpg",
        "https://telegra.ph/file/3e86cc6cab06a6e2bde82.jpg",
        "https://telegra.ph/file/83140e2c57ddd95f310e6.jpg",
        "https://telegra.ph/file/2b20f8509d9437e94fed5.jpg",
        "https://telegra.ph/file/571960dcee4fce56698a4.jpg",
        "https://telegra.ph/file/25929a0b49452d8946c14.mp4",
        "https://telegra.ph/file/f5c9ceded3ee6e76a5931.jpg",
        "https://telegra.ph/file/a8bf6c6df8a48e4a306ca.jpg",
        "https://telegra.ph/file/af9e3f98da0bd937adf6e.jpg",
]
