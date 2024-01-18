from flask import Flask, render_template  # render_template html şablonlarını render etmek için kullanılır

app = Flask('app')  # flask uygulaması oluşturuluyor, app parametresi uygulamanın adı

# veri kısmı
basliklar = []


@app.route('/')  # anasayfa için bir root tanımlar
def home_page():
    dosya = open("./sozluk_dosyalar/basliklar.txt", "r", encoding="utf-8")
    dosyadan_basliklar = dosya.readlines()
    basliklar.clear()

    for b in dosyadan_basliklar:
        parcalar = b.split("|")
        basliklar.append({
            "id": parcalar[0],
            "baslik": parcalar[1]}
        )
    return render_template('home_page.html', basliklar=basliklar, baslik="Anasayfa")  # belirli bir başlığın içeriği görüntülenir


@app.route('/baslik/<baslik_id>/<baslik_metin>')
def baslik_goster(baslik_id, baslik_metin):
    dosya_adi = baslik_id + ".txt"
    dosya = open(f"./sozluk_dosyalar/{dosya_adi}", "r", encoding="utf-8")
    dosyadan_yazilar = dosya.readlines()
    return render_template("baslik_icerik.html", baslik=baslik_metin, icerikler=dosyadan_yazilar, baslik_id=baslik_id)


app.run(debug=True, host='0.0.0.0', port=5000)
