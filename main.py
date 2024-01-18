from flask import Flask, render_template, request,redirect  # render_template html şablonlarını render etmek için kullanılır
import pymongo

app = Flask('app')  # flask uygulaması oluşturuluyor, app parametresi uygulamanın adı

# veri kısmı
basliklar = []

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["eduSozlukDB"]

@app.route('/')  # anasayfa için bir root tanımlar
def home_page():
   # dosya = open("./sozluk_dosyalar/basliklar.txt", "r", encoding="utf-8")
   # dosyadan_basliklar = dosya.readlines()
   # basliklar.clear()
    mycol = mydb["basliklar"]
    basliklar = list(mycol.find({}))
    return render_template('home_page.html', basliklar=basliklar, baslik="Anasayfa")  # belirli bir başlığın içeriği görüntülenir


@app.route('/baslik/<baslik_id>')
def baslik_goster(baslik_id):
    mycol = mydb["yazilar"]
    veritabanından_yazilar = list(mycol.find({"baslik_id":int(baslik_id)}))
    baslik_tablosu=mydb["basliklar"]
    baslik_kaydi=baslik_tablosu.find_one({"_id":int(baslik_id)})
    baslik_metin=baslik_kaydi["baslik"]
    return render_template("baslik_icerik.html", baslik=baslik_metin, yazilar=veritabanından_yazilar, baslik_id=baslik_id)

@app.route('/yazi-ekle', methods=['POST'])
def yazi_ekle():
    baslik_id=request.form.get('txtBaslikId')
    yazi=request.form.get('txtYazi')

    mycol = mydb["yazilar"]
    yeni_yazi={"baslik_id":int(baslik_id),"yazi":yazi}
    x=mycol.insert_one(yeni_yazi)

    #dosya = open(f"./sozluk_dosyalar/{baslik_id}.txt", "a", encoding="utf-8")
    #dosya.write("\n" + yazi)
    return redirect("/baslik/"+baslik_id,302)

app.run(debug=True, host='0.0.0.0', port=5000)
