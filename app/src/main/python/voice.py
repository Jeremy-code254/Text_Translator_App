# from gtts import gTTS
# from io import BytesIO
# import pygame
# import os
#
# def to_voice(mytext, language):
#
#     my_dictionary = {
#     'afrikaans':	'af',
#     'albanian':	'sq',
#     'amharic':	'am',
#     'arabic'	: 'ar',
#     'armenian':	'hy',
#     'assamese':	'as',
#     'aymara' : 'ay',
#     'azerbaijani'	: 'az',
#     'bambara' :	'bm',
#     'basque'	: 'eu',
#     'belarusian' :	'be',
#     'bengali'	: 'bn',
#     'bhojpuri' :	'bho',
#     'bosnian'	: 'bs',
#     'bulgarian' :	'bg',
#     'catalan'	: 'ca',
#     'cebuano'	: 'ceb',
#     'chinese' :	'zh-CN',
#     'chinese' :	'zh-TW',
#     'corsican' : 'co',
#     'croatian'	: 'hr',
#     'czech'	: 'cs',
#     'danish'	: 'da',
#     'dhivehi' :	'dv',
#     'dogri' : 'doi',
#     'dutch'	: 'nl',
#     'english'	: 'en',
#     'esperanto' :	'eo',
#     'estonian'	: 'et',
#     'ewe' : 'ee',
#     'filipino' :	'fil',
#     'finnish'	: 'fi',
#     'french'	:'fr',
#     'frisian'	:'fy',
#     'galician' :'gl',
#     'georgian': 	'ka',
#     'german'	:'de',
#     'greek'	:'el',
#     'guarani'	:'gn',
#     'gujarati':'	gu',
#     'haitian Creole':	'ht',
#     'hausa'	:'ha',
#     'hawaiian':	'haw',
#     'hebrew'	:'he',
#     'hindi':'hi',
#     'hmong'	:'hmn',
#     'hungarian' :	'hu',
#     'icelandic'	:'is',
#     'igbo'	:'ig',
#     'ilocano':	'ilo',
#     'indonesian':	'id',
#     'irish'	:'ga',
#     'italian'	:'it',
#     'japanese'	:'ja',
#     'javanese':	'jv',
#     'kannada'	:'kn',
#     'kazakh'	:'kk',
#     'khmer'	:'km',
#     'kinyarwanda' :	'rw',
#     'konkani' :	'gom',
#     'korean':	'ko',
#     'krio'	:'kri',
#     'kurdish'	:'ku',
#     'kurdish':	'ckb',
#     'kyrgyz'	:'ky',
#     'lao'	:'lo',
#     'latin'	:'la',
#     'latvian':	'lv',
#     'lingala'	:'ln',
#     'lithuanian'	:'lt',
#     'luganda':	'lg',
#     'luxembourgish'	:'lb',
#     'macedonian':	'mk',
#     'maithili'	:'mai',
#     'malagasy'	:'mg',
#     'malay'	:'ms',
#     'malayalam'	:'ml',
#     'maltese'	:'mt',
#     'maori':	'mi',
#     'marathi':	'mr',
#     'meiteilon' :	'mni-Mtei',
#     'mizo':'lus',
#     'mongolian'	:'mn',
#     'myanmar' :	'my',
#     'nepali'	:'ne',
#     'norwegian':	'no',
#     'nyanja' :	'ny',
#     'odia' :'or',
#     'oromo'	:'om',
#     'pashto'	:'ps',
#     'persian':	'fa',
#     'polish'	:'pl',
#     'portuguese' :	'pt',
#     'punjabi' :	'pa',
#     'quechua' :	'qu',
#     'romanian'	:'ro',
#     'russian'	:'ru',
#     'samoan'	:'sm',
#     'sanskrit':	'sa',
#     'scots gaelic'	:'gd',
#     'sepedi':'	nso',
#     'serbian'	:'sr',
#     'sesotho'	:'st',
#     'shona'	:'sn',
#     'sindhi'	:'sd',
#     'sinhala' :	'si',
#     'slovak':	'sk',
#     'slovenian'	:'sl',
#     'somali'	:'so',
#     'spanish'	:'es',
#     'sundanese'	:'su',
#     'swahili':	'sw',
#     'swedish'	:'sv',
#     'tagalog' :	'tl',
#     'tajik'	:'tg',
#     'tamil'	:'ta',
#     'tatar'	:'tt',
#     'telugu'	:'te',
#     'thai':	'th',
#     'tigrinya'	:'ti',
#     'tsonga'	:'ts',
#     'turkish'	:'tr',
#     'turkmen'	:'tk',
#     'twi':	'ak',
#     'ukrainian'	:'uk',
#     'urdu' : 'ur',
#     'uyghur'	: 'ug',
#     'uzbek' :	'uz',
#     'vietnamese' :	'vi',
#     'welsh' :	'cy',
#     'xhosa' :	'xh',
#     'yiddish' :	'yi',
#     'yoruba'	: 'yo',
#     "zulu"	: 'zu'
#     }
#
#     for key, value in my_dictionary.items():
#     	if key == language:
#     	    language = value
#     mp3_fo = BytesIO()
#     myobj = gTTS(text=mytext, lang=language, slow=False)
#     tts.write_to_fp(mp3_fo)
# #     myobj.save("welcome.mp3")
#     pygame.init()
#     pygame.mixer.init()
#     pygame.mixer.music.load(mp3_fo, 'mp3')
#     sound = pygame.mixer.music.play()
#     return sound