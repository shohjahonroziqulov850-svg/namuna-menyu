import pandas as pd, html

df = pd.read_excel('menyu.xlsx').fillna('')

css = """body{font-family:Arial,sans-serif;max-width:480px;margin:0 auto;padding:16px;background:#faf6f0;color:#222}
h1{text-align:center;color:#8a3b12}
h2{border-bottom:2px solid #8a3b12;padding-bottom:4px;margin-top:28px}
.taom{display:flex;justify-content:space-between;padding:10px 0;border-bottom:1px solid #e5dccf}
.taom>div:first-child{flex:1;min-width:0}
.narx{font-weight:bold;white-space:nowrap;margin-left:12px}
.tavsif{font-size:.85em;color:#666}
.rasm{max-width:100%;height:auto;border-radius:8px;margin-top:8px;display:block}"""

parts = []
for bolim, g in df.groupby('bolim', sort=False):
    parts.append('<h2>' + html.escape(bolim) + '</h2>')
    for r in g.itertuples():
        tavsif = '<div class="tavsif">' + html.escape(r.tavsif) + '</div>' if r.tavsif else ''
        rasm = '<img src="' + html.escape(r.rasm) + '" alt="' + html.escape(r.taom) + '" class="rasm">' if r.rasm else ''
        narx = f'{int(r.narx):,}'.replace(',', ' ')
        parts.append('<div class="taom"><div>' + html.escape(r.taom) + tavsif + rasm + '</div><div class="narx">' + narx + '</div></div>')

head = '<!DOCTYPE html><html lang="uz"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>Namuna Oshxona - Menyu</title><style>' + css + '</style></head><body><h1>Namuna Oshxona</h1>'
open('index.html', 'w', encoding='utf-8').write(head + ''.join(parts) + '</body></html>')
print(len(df), 'taom menyuga yozildi')
