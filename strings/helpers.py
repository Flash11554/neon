HELP_1 = """<b><u>ᴀᴅᴍɪɴ ᴄᴏᴍᴍᴀɴᴅs :</b></u>

Sadəcə əmrlərin əvvəlində <b>ᴄ</b> hərfini əlavə edin ki, bu əmrlərdən kanal üçün istifadə edə biləsiniz.

/pause : Hazırda çalan yayımlamayı dayandırır.

/resume : Dayandırılmış yayımı davam etdirir.

/skip : Hazırda çalan yayımlamayı keçərək növbəti mahnıya keçir.

/end və ya /stop : Növbəti yayımlamayı başlatmadan əvvəl hazırda çalan yayımlamayı dayandırır və sıfırlayır.

/player : İnteraktiv oyunçu panelini açır.

/queue : Yaradılmış növbəni göstərir.

/lyrics [mahnı adı] : Sorğulanan mahnının sözlərini axtarır və nəticələri göndərir.
"""

HELP_2 = """
<b><u>ʙᴜʟᴀɴᴅ ᴏᴍᴜᴢʟᴀʀ :</b></u>

Bütün əmrlərə sahib olan istifadəçilər botda admin hüquqları olmadan da kanalda admin hüquqları əldə edə bilərlər.

/auth [istifadəçi adı/istifadəçi id] : İstifadəçini botun autentifikasiya siyahısına əlavə edir.
/unauth [istifadəçi adı/istifadəçi id] : İstifadəçini autentifikasiya siyahısından silir.
/authusers : Qrupda autentifikasiya olunmuş istifadəçilərin siyahısını göstərir.
"""

HELP_3 = """
<u><b>ᴀᴅᴍɪɴ ʙʀᴏᴀᴅᴄᴀsᴛ ᴇmʀlᴇr</b></u> [ᴏɴʟʏ ғᴏʀ sᴜᴅᴏᴇʀs] :

/broadcast [mesaj və ya cavab mesajına yazın] : Botun xidmət etdiyi bütün kanallara mesaj göndərir.

<u>ʙʀᴏᴀᴅᴄᴀsᴛɪɴɢ ᴍᴏᴅᴇs :</u>
<b>-pin</b> : Mesajı kanallarda pinləyir.
<b>-pinloud</b> : Mesajı pinləyir və kanal üzvlərinə bildiriş göndərir.
<b>-user</b> : Botu başlatmış istifadəçilərə mesajı göndərir.
<b>-assistant</b> : Mesajı botun yardım hesabından göndərir.
<b>-nobot</b> : Botu mesaj göndərməkdən məhrum edir.

<b>Misal:</b> <code>/broadcast -user -assistant -pin test mesajı</code>
"""

HELP_4 = """<u><b>ᴄʜᴀᴛ ʙʟᴀᴄᴋʟɪsᴛ ᴇmʀlᴇr :</b></u> [ᴏɴʟʏ ғᴏʀ sᴜᴅᴏᴇʀs]

Chatlarımıza daxil olan botun xidmətindən istifadəni məhdudlaşdırın.

/blacklistchat [chat id] : Chatı botdan istifadə etməkdən qadağan edir.
/whitelistchat [chat id] : Qara siyahıdan çıxarır və bu chatın botdan istifadəsinə icazə verir.
/blacklistedchat : Qara siyahıya alınan chatların siyahısını göstərir.
"""

HELP_5 = """
<u><b>ʙʟᴏᴄᴋ ᴜsᴇʀs:</b></u> [ᴏɴʟʏ ғᴏʀ sᴜᴅᴏᴇʀs]

Bloklanmış istifadəçiləri bot əmrlərini istifadə etməməsi üçün ignora edir.

/block [istifadəçi adı və ya cavab] : İstifadəçini bloklayır.
/unblock [istifadəçi adı və ya cavab] : Bloklanmış istifadəçini açır.
/blockedusers : Bloklanmış istifadəçilərin siyahısını göstərir.
"""

HELP_6 = """
<u><b>ᴄʜᴀɴɴᴇʟ ᴘʟᴀʏ ᴇmʀlᴇr :</b></u>

Kanallar üçün musiqi və ya video yayımı edirsiniz.

/cplay : Seçilən audio tracki kanalın videomüzik hissəsində yayımlamağa başlayır.
/cvplay : Seçilən video tracki kanalın videomüzik hissəsində yayımlamağa başlayır.
/cplayforce və ya /cvplayforce : Hazırda yayımlanan tracki dayandırır və yeni trackə keçir.

/channelplay [chat istifadəçi adı və ya id] və ya [disable] : Kanalı qrupa bağlayır və track yayımlamağa başlayır.
"""

HELP_7 = """
<u><b>ɢʟᴏʙᴀʟ ʙᴀɴ ᴇmʀlᴇr :</b></u> [ᴏɴʟʏ ғᴏʀ sᴜᴅᴏᴇʀs] :

/gban [istifadəçi adı və ya cavab] : İstifadəçini bütün serverlərdən qadağan edir və botun istifadə edilməsinə qadağa qoyur.
/ungban [istifadəçi adı və ya cavab] : Qlobal qadağanı açır və istifadəçini geri qaytarır.
/gbannedusers : Qlobal şəkildə qadağan edilmiş istifadəçilərin siyahısını göstərir.
"""

HELP_8 = """
<b><u>ʟᴏᴏᴘ sᴛʀᴇᴀᴍ :</b></u>

<b>Yayımlamağı dövrə salır</b>

/loop [enable/disable] : Yayımlamağı dövrə salır.
/loop [1, 2, 3, ...] : Yayımlamağı dövrə salır və verilmiş dəyəri təyin edir.
"""

HELP_9 = """
<u><b>ᴍᴀɪɴᴛᴇɴᴀɴᴄᴇ ᴍᴏᴅᴇ</b></u> [ᴏɴʟʏ ғᴏʀ sᴜᴅᴏᴇʀs] :

/logs : Botun əməliyyatlarını göstərir.

/logger [enable/disable] : Botun əməliyyatlarının qeyd edilməsini açır və ya bağlayır.

/maintenance [enable/disable] : Botun xidmətinin dayandırılmasını və ya aktiv edilməsini təmin edir.
"""

HELP_10 = """
<b><u>ᴘɪɴɢ & sᴛᴀᴛs :</b></u>

/start : Musiqi botunu başlatır.
/help : Əmrlər üçün kömək menyusunu göstərir.

/ping : Botun cavab müddətini göstərir.
"""
