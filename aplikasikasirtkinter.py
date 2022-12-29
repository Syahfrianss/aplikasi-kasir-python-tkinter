from tkinter import* #Module Tkinter


window = Tk()
window.title("Aplikasi Kasir Kadalz Coffee")
window.geometry("500x500")
window.resizable(0,0)
window.configure(bg='#7a7cc9')


def button_clicked():
    iceamericano_total = int(iceamericano_sb.get()) * 14000
    eskopisusu_total = int(eskopisusu_sb.get()) * 11000
    eskopicoklat_total= int(eskopicoklat_sb.get()) * 12000
    eskopihitam_total= int(eskopihitam_sb.get()) * 11000
    kentang_total = int(kentang_sb.get()) * 5000
    donat_total = int(donat_sb.get()) * 2500
    roti_total = int(roti_sb.get()) * 20000
    total_bayar = iceamericano_total + eskopisusu_total + eskopicoklat_total + eskopihitam_total + kentang_total + donat_total + roti_total
    bayar = Label(text=f"Jumlah Bayar Rp{total_bayar}", font=("arial 12 bold"),bg='#7a7cc9')
    bayar.place(x=160, y=400)

#Judul Kasir
nama_tempat = Label(text='Selamat Datang di\n Kadalz Coffee', font=("Times New Roman", 20, "bold"),bg='#7a7cc9')
nama_tempat.place(x=135, y=0)

#Menu Kopi
pilih_menu = Label(text="Pilih Menu Kopi", font=("arial 12 bold"),bg='#7a7cc9')
pilih_menu.place(x=20, y=120)

#Menu Camilan
pilih_menucamilan = Label(text="Pilih Menu Camilan", font=("arial 12 bold"),bg='#7a7cc9')
pilih_menucamilan.place(x=300, y=120)

#Roti Toast
roti_label = Label(text="Roti Toast\nRP20.000",bg='#7a7cc9')
roti_label.place(x=310, y=250)
roti_sb = Spinbox(from_=0, to=10, width=5)
roti_sb.place(x=410, y=260)

#French Fries
kentang_label = Label(text="Kentang Goreng\nRP5.000",bg='#7a7cc9')
kentang_label.place(x=300, y=150)
kentang_sb = Spinbox(from_=0, to=10, width=5)
kentang_sb.place(x=410, y=155)

#Donat Kentang
donat_label = Label(text="Donat Kentang\nRP2.500",bg='#7a7cc9')
donat_label.place(x=300, y=200)
donat_sb = Spinbox(from_=0, to=10, width=5,)
donat_sb.place(x=410, y=205)


#ICE Americano
iceamericano_label = Label(text="Ice Americano\nRp14.000  ",bg='#7a7cc9')
iceamericano_label.place(x=20, y=150)
iceamericano_sb = Spinbox(from_=0, to=10, width=5)
iceamericano_sb.place(x=110, y=155)

#ES KOPI SUSU
eskopisusu_label = Label(text="Es Kopi Susu\nRp11.000  ",bg='#7a7cc9')
eskopisusu_label.place(x=20, y=200)
eskopisusu_sb = Spinbox(from_=0, to=10, width=5)
eskopisusu_sb.place(x=110, y=205)

#ES KOPI COKLAT
eskopicoklat_label = Label(text="Es Kopi Coklat\nRp12.000  ",bg='#7a7cc9')
eskopicoklat_label.place(x=20, y=250)
eskopicoklat_sb = Spinbox(from_=0, to=10, width=5)
eskopicoklat_sb.place(x=110, y=255)

#ES KOPI Hitam
eskopihitam_label = Label(text="Es Kopi Hitam\nRp11.000  ",bg='#7a7cc9')
eskopihitam_label.place(x=20, y=300)
eskopihitam_sb = Spinbox(from_=0, to=10, width=5)
eskopihitam_sb.place(x=110, y=305)

#pesan Button
pesan = Button(text="Pesan", command=button_clicked, bg='#4b4c7c', width=10 )
pesan.place(x=200, y=360)

window.mainloop()