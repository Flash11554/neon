HELP_1 = """<b><u>ᴀᴅᴍɪɴ ᴋᴏᴍᴀɴᴅʟᴀʀı :</b></u>

Yalnız <b>c</b> əmrini komandanın başlanğıcına əlavə edərək onları kanal üçün istifadə edə bilərsiniz.

/pause : Cari oynayan yayımlamanı dayandırır.

/resume : Dayandırılmış yayını davam etdirir.

/skip : Cari oynayan yayını keçirir və növbəti parçanı sıraya əlavə edir.

/end və ya /stop : Növbəni təmizləyir və cari yayını dayandırır.

/player : İnteraktiv bir oyunçu paneli alırsınız.

/queue : Növbəyə əlavə olunan parçaların siyahısını göstərir.

/lyrics [mahnı adı] : Sorğu olunan mahnının sözlərini axtarır və nəticəni göndərir.
"""

HELP_2 = """
<b><u>ᴀᴜᴛʜ ᴋᴏᴍᴜt istifadəçiləri:</b></u>

Auth istifadəçiləri, botda admin hüquqlarına sahib olmadan botda admin hüquqlarına sahib ola bilərlər.

/auth [istifadəçi adı/istifadəçi id] : İstifadəçini botun auth istifadəçilər siyahısına əlavə edir.
/unauth [istifadəçi adı/istifadəçi id] : İstifadəçini auth istifadəçilər siyahısından çıxarır.
/authusers : Qrupun auth istifadəçilər siyahısını göstərir.
"""

HELP_3 = """
<u><b>Yayımlama Xüsusiyyəti</b></u> [Yalnız Sudolar üçün]:

/broadcast [mesaj və ya mesaja cavab] : Botun xidmət etdiyi qruplara mesaj yayımlayır.

<u>Yayımlama Modları:</u>
<b>-pin</b> : Yayımlanan mesajları xidmət olunan qruplarda yapışdırır.
<b>-pinloud</b> : Yayımlanan mesajı qruplarda yapışdırır və üzvlərə bildiriş göndərir.
<b>-user</b> : Yayımlanan mesajı botu istifadə etməyə başlamış istifadəçilərə göndərir.
<b>-assistant</b> : Mesajı botun köməkçi hesabından yayımlayır.
<b>-nobot</b> : Botu yayımlanan mesajı yayımlamamağa məcbur edir.

<b>Nümunə:</b> <code>/broadcast -user -assistant -pin test mesajı</code>
"""

HELP_4 = """
<u><b>Çat Qara Siyahı Xüsusiyyəti:</b></u> [Yalnız Sudolar üçün]

Botu yalnız seçilmiş çatlarda istifadə etməyə məhdudlaşdırır.

/blacklistchat [çat id] : Çatı botu istifadə etməkdən qadağan edir.

/whitelistchat [çat id] : Qara siyahıdan çıxarılmış çatı botu istifadə etməyə icazə verir.

/blacklistedchat : Qara siyahıya alınmış çatların siyahısını göstərir.
"""

HELP_5 = """
<u><b>İstifadəçi Bloklama:</b></u> [Yalnız Sudolar üçün]

Qara siyahıya alınmış istifadəçini görməməzliyə vurur, beləliklə o, botun əmrlərini istifadə edə bilməz.

/block [istifadəçi adı və ya istifadəçiyə cavab] : İstifadəçini botdan bloklayır.
/unblock [istifadəçi adı və ya istifadəçiyə cavab] : Bloklanmış istifadəçini unblock edir.
/blockedusers : Bloklanmış istifadəçilərin siyahısını göstərir.
"""

HELP_6 = """
<u><b>Kanal Əmrləri:</b></u>

Siz kanalda audio/video yayımı edə bilərsiniz.

/cplay : İstənilən audio mahnısının kanalda video çatında yayımlanmasına başlayır.
/cvplay : İstənilən video mahnısının kanalda video çatında yayımlanmasına başlayır.
/cplayforce və ya /cvplayforce : Mövcud yayını dayandırır və tələb olunan track-i yayına başlatır.

/channelplay [çat istifadəçi adı və ya id] və ya [deaktivləşdir] : Kanalı qrupa bağlayır və qrupa göndərilən əmrlərlə track-ləri yayımlamağa başlayır.
"""

HELP_7 = """
<u><b>Qlobal Ban Xüsusiyyəti</b></u> [Yalnız Sudolar üçün]:

/gban [istifadəçi adı və ya istifadəçiyə cavab] : İstifadəçini bütün xidmət olunan çatlardan qlobal şəkildə banlayır və botu istifadə etməyə qadağan edir.
/ungban [istifadəçi adı və ya istifadəçiyə cavab] : Qlobal banlanmış istifadəçini unblock edir.
/gbannedusers : Qlobal olaraq banlanmış istifadəçilərin siyahısını göstərir.
"""

HELP_8 = """
<b><u>Yayım Dövrü Əmirləri:</b></u>

<b>Yayımın davamlı olmasını təmin edir</b>

/loop [enable/disable] : Yayımı davamlı şəkildə dövrə salır və ya ləğv edir.
/loop [1, 2, 3, ...] : Verilən dəyər üçün dövrü aktivləşdirir.
"""

HELP_9 = """
<u><b>Giriş Vəziyyətləri</b></u> [Yalnız Sudolar üçün]:

/logs : Botun loglarını əldə etmək.

/logger [enable/disable] : Bot fəaliyyətlərini qeyd etməyə başlayır.

/maintenance [enable/disable] : Botun baxım rejimini aktivləşdirir və ya deaktivləşdirir.
"""
HELP_10 = """
<b><u>Ping & Statistika:</b></u>

/start : Musiqi botunu işə salır.
/help : Əmrlərin açıqlamaları ilə yardım menyusunu göstərir.

/ping : Botun ping və sistem statistikalarını göstərir.

/stats : Botun ümumi statistikalarını göstərir.
"""

HELP_11 = """
<u><b>Oynatma Əmrləri:</b></u>

<b>v :</b> Video oynatma üçün istifadə olunur.
<b>force :</b> Güclü oynatma üçün istifadə olunur.

/play və ya /vplay : Tələb olunan mahnının videoçatda yayımını başlatır.

/playforce və ya /vplayforce : Mövcud yayını dayandırır və tələb olunan track-i yayımına başlayır.
"""

HELP_12 = """
<b><u>Sıranı Qarışdırma Əmirləri:</b></u>

/shuffle : Sıranı qarışdırır.
/queue : Qarışdırılmış sıranı göstərir.
"""

HELP_13 = """
<b><u>Axtarış Yayımı Əmirləri:</b></u>

/seek [vaxt saniyə ilə] : Yayımı verilən müddətə qədər axtarır.
/seekback [vaxt saniyə ilə] : Yayımı verilən müddətə qədər geri axtarır.
"""

HELP_14 = """
<b><u>Mahnı Yükləmə Əmirləri:</b></u>

/song [mahnı adı/yt url] : YouTube-dan hər hansı bir track-i mp3 və ya mp4 formatında yükləyir.
"""

HELP_15 = """
<b><u>Sürət Əmrləri:</b></u>

Siz davam edən yayımın audio playback sürətini tənzimləyə bilərsiniz. [Yalnız Adminlər üçün]

/speed və ya /playback : Qrupda audio playback sürətini tənzimləmək üçün.
/cspeed və ya /cplayback : Kanalda audio playback sürətini tənzimləmək üçün.
"""  
