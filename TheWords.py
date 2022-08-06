#!/usr/bin/env python3


import os
import sys
if sys.platform=="win32" or sys.platform=="win64":
	os.system("cls")
	os.system("pip install tk")
	os.system("pip install pyfiglet")
	os.system("cls")
elif sys.platform=="linux" or sys.platform=="linux2" or sys.platform=="linux3":
	os.system("clear")
	os.system("sudo apt-get update && sudo apt-get upgrade")
	os.system("pip install tk")
	os.system("pip install pyfiglet")
	os.system("clear")
import random
import tkinter
import pyfiglet
# source: https://pypi.org/project/pyfiglet/, https://pypi.org/project/tk/
# written on Friday, August 5, 2022, at 21:47 PM.
# This program or tool was created by Indonesia language.
# https://www.tutorialspoint.com/python/tk_cursors.htm


Python_Tkinter_Cursors=["arrow","circle","clock","cross","dotbox","exchange","fleur","heart","heart","man","mouse","pirate","plus","shuttle","sizing","spider","spraycan","star","target","tcross","trek","watch"]
Python_Tkinter_Cursors.append("crosshair")

def The_Words_I_Wish_I_Said(code_by="ruben leonardo sigalingging"):
	Fungsi_Utama_Kata_Kata_Yang_Ingin_Saya_Ucapkan=tkinter.Tk()
	Fungsi_Utama_Kata_Kata_Yang_Ingin_Saya_Ucapkan.title("The Words I Wish I Said")
	Fungsi_Utama_Kata_Kata_Yang_Ingin_Saya_Ucapkan.geometry("800x500")
	Fungsi_Utama_Kata_Kata_Yang_Ingin_Saya_Ucapkan.resizable(width=False,height=False)
	Fungsi_Utama_Kata_Kata_Yang_Ingin_Saya_Ucapkan.configure(bg="#000000",cursor="crosshair")


	Navbar=tkinter.Label(Fungsi_Utama_Kata_Kata_Yang_Ingin_Saya_Ucapkan,text="The Words",anchor=tkinter.CENTER,bg="#008000",cursor="arrow",font=("Ubuntu Condensed",35),fg="#ffffff",justify=tkinter.CENTER,relief=tkinter.FLAT)
	Navbar.pack(expand=False,fill=tkinter.BOTH,side=tkinter.TOP)


	Frame_Code=tkinter.Frame(Fungsi_Utama_Kata_Kata_Yang_Ingin_Saya_Ucapkan,bg="#ffffff")
	Frame_Code.pack(expand=False,fill=tkinter.BOTH)


	def Home_Function(created_by="Ruben Leonardo Sigalingging"):
		quit()


	Home_NavBar=tkinter.Button(Frame_Code,text="Home",activebackground="#ffffff",activeforeground="#008b8b",bg="#008b8b",fg="#ffffff",font=("Ubuntu Condensed",22),justify=tkinter.CENTER,cursor="arrow",width=15,command=Home_Function)
	Home_NavBar.pack(expand=False,side=tkinter.LEFT,padx=0,pady=0)


	def GitHub_Function():
		import webbrowser
		webbrowser.open("https://github.com/RubenLeonardoSigalingging",new=0,autoraise=True)


	GitHub=tkinter.Button(Frame_Code,text="GitHub",activebackground="#ffffff",activeforeground="#008b8b",bg="#008b8b",fg="#ffffff",font=("Ubuntu Condensed",22),justify=tkinter.CENTER,cursor="arrow",width=15,command=GitHub_Function)
	GitHub.pack(expand=False,side=tkinter.LEFT,padx=0,pady=0)


	def Loneliness_Quotes():
		from tkinter import messagebox
		List_Of_Words=["Let me tell you this: if you meet a loner, no matter what they tell you, it's not because they enjoy solitude. It's because they have tried to blend into the world before, and people continue to disappoint them.","Biarkan saya memberi tahu Anda ini: jika Anda bertemu seorang penyendiri, tidak peduli apa yang mereka katakan, itu bukan karena mereka menikmati kesendirian. Itu karena mereka telah mencoba berbaur dengan dunia sebelumnya, dan orang-orang terus mengecewakan mereka.","The loneliest moment in someone’s life is when they are watching their whole world fall apart, and all they can do is stare blankly.","Saat paling kesepian dalam hidup seseorang adalah ketika mereka melihat seluruh dunia mereka berantakan, dan yang bisa mereka lakukan hanyalah menatap kosong.","Two possibilities exist: either we are alone in the Universe or we are not. Both are equally terrifying.","Ada dua kemungkinan: apakah kita sendirian di Semesta atau tidak. Keduanya sama-sama menakutkan.","Remember: the time you feel lonely is the time you most need to be by yourself. Life's cruelest irony.","Ingat: saat Anda merasa kesepian adalah saat yang paling Anda butuhkan untuk menyendiri. Ironi hidup yang paling kejam.",
		"Why do people have to be this lonely? What's the point of it all? Millions of people in this world, all of them yearning, looking to others to satisfy them, yet isolating themselves. Why? Was the earth put here just to nourish human loneliness?","Mengapa orang harus kesepian ini? Apa gunanya semua itu? Jutaan orang di dunia ini, semuanya mendambakan, mencari orang lain untuk memuaskan mereka, namun mengisolasi diri mereka sendiri. Mengapa? Apakah bumi diletakkan di sini hanya untuk memelihara kesepian manusia?","The worst part of holding the memories is not the pain. It's the loneliness of it. Memories need to be shared.","Bagian terburuk dari menyimpan kenangan bukanlah rasa sakitnya. Ini adalah kesepiannya. Kenangan perlu dibagikan.","Nobody likes being alone that much. I don't go out of my way to make friends, that's all. It just leads to disappointment.","Tidak ada yang suka sendirian sebanyak itu. Saya tidak berusaha keras untuk mencari teman, itu saja. Itu hanya mengarah pada kekecewaan.","Music was my refuge. I could crawl into the space between the notes and curl my back to loneliness.","Musik adalah tempat perlindungan saya. Aku bisa merangkak ke ruang di antara nada dan meringkuk dalam kesepian.","I’m here. I love you. I don’t care if you need to stay up crying all night long, I will stay with you. If you need the medication again, go ahead and take it—I will love you through that, as well. If you don’t need the medication, I will love you, too. There’s nothing you can ever do to lose my love. I will protect you until you die, and after your death I will still protect you. I am stronger than Depression and I am braver than Loneliness and nothing will ever exhaust me.",
		"Aku disini. Aku mencintaimu. Aku tidak peduli jika kamu harus begadang menangis sepanjang malam, aku akan tinggal bersamamu. Jika Anda membutuhkan obat itu lagi, silakan dan minumlah — saya juga akan mencintaimu melalui itu. Jika kamu tidak membutuhkan obatnya, aku juga akan mencintaimu. Tidak ada yang bisa kamu lakukan untuk kehilangan cintaku. Aku akan melindungimu sampai kamu mati, dan setelah kematianmu aku akan tetap melindungimu. Saya lebih kuat dari Depresi dan saya lebih berani dari Kesepian dan tidak ada yang akan melelahkan saya.","All I ever wanted was to reach out and touch another human being not just with my hands but with my heart.","Yang saya inginkan hanyalah menjangkau dan menyentuh manusia lain tidak hanya dengan tangan saya tetapi dengan hati saya.","If you're lonely when you're alone, you're in bad company.","Jika Anda kesepian saat sendirian, Anda berada di lingkungan yang buruk.","Solitude is fine but you need someone to tell that solitude is fine.","Kesendirian itu baik-baik saja tetapi Anda membutuhkan seseorang untuk memberi tahu bahwa kesendirian itu baik-baik saja.","Maybe ever’body in the whole damn world is scared of each other.","Mungkin semua orang di seluruh dunia takut satu sama lain.",
		"All great and precious things are lonely.","Semua hal yang besar dan berharga adalah kesepian.","I have absolutely no pleasure in the stimulants in which I sometimes so madly indulge. It has not been in the pursuit of pleasure that I have periled life and reputation and reason. It has been the desperate attempt to escape from torturing memories, from a sense of insupportable loneliness and a dread of some strange impending doom.","Saya sama sekali tidak menikmati stimulan yang kadang-kadang saya nikmati dengan sangat gila. Bukan dalam mengejar kesenangan saya telah membahayakan kehidupan, reputasi, dan akal sehat. Ini adalah upaya putus asa untuk melarikan diri dari kenangan yang menyiksa, dari rasa kesepian yang tak tertahankan, dan ketakutan akan malapetaka aneh yang akan datang.","Being alone never felt right. sometimes it felt good, but it never felt right.","Sendirian tidak pernah terasa benar. kadang terasa enak, tapi tidak pernah terasa benar.","When I get lonely these days, I think: So BE lonely, Liz. Learn your way around loneliness. Make a map of it. Sit with it, for once in your life. Welcome to the human experience. But never again use another person's body or emotions as a scratching post for your own unfulfilled yearnings.","Ketika saya kesepian akhir-akhir ini, saya berpikir: Jadi, jadilah kesepian, Liz. Pelajari cara Anda mengatasi kesepian. Buatlah petanya. Duduklah dengannya, sekali dalam hidupmu. Selamat datang di pengalaman manusia. Tetapi jangan pernah lagi menggunakan tubuh atau emosi orang lain sebagai tiang goresan untuk kerinduan Anda yang tidak terpenuhi.",
		"Where you used to be, there is a hole in the world, which I find myself constantly walking around in the daytime, and falling in at night. I miss you like hell.","Di tempat Anda dulu, ada sebuah lubang di dunia, di mana saya menemukan diri saya terus-menerus berjalan di siang hari, dan jatuh di malam hari. Aku merindukanmu seperti neraka.","The trouble is not that I am single and likely to stay single, but that I am lonely and likely to stay lonely.","Masalahnya bukan karena saya lajang dan cenderung tetap melajang, tetapi karena saya kesepian dan cenderung tetap kesepian.","Loneliness is the human condition. Cultivate it. The way it tunnels into you allows your soul room to grow. Never expect to outgrow loneliness. Never hope to find people who will understand you, someone to fill that space. An intelligent, sensitive person is the exception, the very great exception. If you expect to find people who will understand you, you will grow murderous with disappointment. The best you'll ever do is to understand yourself, know what it is that you want, and not let the cattle stand in your way.","Kesepian adalah kondisi manusia. Budidaya itu. Cara itu masuk ke dalam diri Anda memungkinkan ruang jiwa Anda tumbuh. Jangan pernah berharap untuk mengatasi kesepian. Jangan pernah berharap untuk menemukan orang yang akan memahami Anda, seseorang untuk mengisi ruang itu. Orang yang cerdas dan sensitif adalah pengecualian, pengecualian yang sangat besar. Jika Anda berharap menemukan orang yang akan memahami Anda, Anda akan menjadi pembunuh dengan kekecewaan. Hal terbaik yang pernah Anda lakukan adalah memahami diri sendiri, mengetahui apa yang Anda inginkan, dan tidak membiarkan ternak menghalangi jalan Anda.",
		"God, but life is loneliness, despite all the opiates, despite the shrill tinsel gaiety of 'parties' with no purpose, despite the false grinning faces we all wear. And when at last you find someone to whom you feel you can pour out your soul, you stop in shock at the words you utter - they are so rusty, so ugly, so meaningless and feeble from being kept in the small cramped dark inside you so long. Yes, there is joy, fulfillment and companionship - but the loneliness of the soul in its appalling self-consciousness is horrible and overpowering.","Tuhan, tetapi hidup adalah kesepian, terlepas dari semua candu, meskipun keriangan 'pesta' tanpa tujuan, meskipun wajah seringai palsu yang kita semua kenakan. Dan ketika akhirnya Anda menemukan seseorang yang Anda rasa dapat mencurahkan jiwa Anda, Anda berhenti kaget pada kata-kata yang Anda ucapkan - kata-kata itu sangat berkarat, sangat jelek, sangat tidak berarti dan lemah karena disimpan dalam kegelapan kecil yang sempit di dalam diri Anda. begitu lama. Ya, ada kegembiraan, kepuasan, dan persahabatan - tetapi kesepian jiwa dalam kesadaran diri yang mengerikan itu mengerikan dan kuat.","The most terrible poverty is loneliness, and the feeling of being unloved.","Kemiskinan yang paling mengerikan adalah kesepian, dan perasaan tidak dicintai.",
		"Control can sometimes be an illusion. But sometimes you need illusions to gain control. Fantasy is an easy way to give meaning to world. To cloak our harsh reality with escapist comfort. After all, isn't that why we surround ourselves with so many screens? So we can avoid seeing? So we can avoid each other? So we can avoid truth.","Kontrol terkadang bisa menjadi ilusi. Tetapi terkadang Anda membutuhkan ilusi untuk mendapatkan kendali. Fantasi adalah cara mudah untuk memberi makna pada dunia. Untuk menyelubungi kenyataan pahit kita dengan kenyamanan pelarian. Lagi pula, bukankah itu sebabnya kita mengelilingi diri kita dengan begitu banyak layar? Jadi kita bisa menghindari melihat? Jadi kita bisa saling menghindari? Jadi kita bisa menghindari kebenaran."]

		Random_Function="".join(random.choice(List_Of_Words))


		messagebox.showinfo(title="Random Loneliness Quotes",message=Random_Function)


	Var_Loneliness_Quotes=tkinter.Button(Frame_Code,text="Loneliness Quotes",activebackground="#ffffff",activeforeground="#008b8b",bg="#008b8b",fg="#ffffff",font=("Ubuntu Condensed",22),justify=tkinter.CENTER,cursor="arrow",width=15,command=Loneliness_Quotes)
	Var_Loneliness_Quotes.pack(expand=False,side=tkinter.LEFT,padx=0,pady=0)


	Label_Pyfiglet=tkinter.Label(Fungsi_Utama_Kata_Kata_Yang_Ingin_Saya_Ucapkan,anchor=tkinter.CENTER,bg="#000000",bd=2,cursor="pirate",font=("Ubuntu Condensed",18),fg="#ffffff",justify=tkinter.CENTER,height=13,width=18)
	Text=pyfiglet.Figlet(font="rounded")
	Label_Pyfiglet.configure(text="cyber vandalism:\n"+str(Text.renderText("vandalism")))
	Label_Pyfiglet.pack(expand=False,fill=tkinter.BOTH,side=tkinter.TOP,pady=12)


	Fungsi_Utama_Kata_Kata_Yang_Ingin_Saya_Ucapkan.mainloop()
The_Words_I_Wish_I_Said()