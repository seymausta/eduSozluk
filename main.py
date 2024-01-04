from flask import Flask, render_template #render_template html şablonlarını render etmek için kullanılır

app = Flask('app') #flask uygulaması oluşturuluyor, app parametresi uygulamanın adı

#veri kısmı
basliklar = [{
  "id": 1,
  "baslik": "Yılbaşı film önerileri",
  "icerikler": ["icerik1", "icerik2", "icerik3"]},
  {
    "id": 2,
    "baslik": "2024 yılbaşı mesajları",
    "icerikler": ["icerik4", "icerik5", "icerik6"]},
  {
    "id": 3,
    "baslik": "2024'te ücretelere gelecek zamlar",
    "icerikler": ["icerik7", "icerik8", "icerik9"]},
  {
    "id": 4,
    "baslik": "python ne işe yarar",
    "icerikler": ["icerik10", "icerik11", "icerik12"]},
  {
    "id": 5,
    "baslik": "bye bye 2023",
    "icerikler": ["icerik13", "icerik14", "icerik15"]},
]

@app.route('/')  #anasayfa için bir root tanımlar
def home_page():
  return render_template("home_page.html",basliklar=basliklar) #belirli bir başlığın içeriği görüntülenir

@app.route('/baslik/<baslik_id>') #baslik_id parametresi ile belirlenen bir başlık sayfası için bir route tanımlar
def baslik_goster(baslik_id):
  baslik=""
  icerikler=[]
  for b in basliklar:
    if b["id"]==int(baslik_id):
      baslik=b["baslik"]
      icerikler=b["icerikler"]

  return render_template("baslik_icerik.html",baslik=baslik,icerikler=icerikler)


app.run(debug=True, host='0.0.0.0', port=5000)