# Usage: pip install edge-tts   then:   python make_audio.py
import asyncio, csv, os, shutil
import edge_tts

MALE = "ar-SA-HamedNeural"
FEMALE = "ar-SA-ZariyahNeural"
OVERWRITE = False   # True = ولّد كل شيء من جديد حتى لو الملف موجود
RATE = "-10%"   # sedikit lebih lambat untuk pemula; ubah ke "+0%" jika ingin normal

here = os.path.dirname(os.path.abspath(__file__))
out = os.path.join(here, "audio")
os.makedirs(out, exist_ok=True)

rows = list(csv.DictReader(open(os.path.join(here, "audio_list.csv"), encoding="utf-8-sig")))
done = {}

async def main():
    for r in rows:
        name, text = r["nama_file"], r["teks_arab"]
        path = os.path.join(out, name)
        voice = FEMALE if name.endswith("f.mp3") else MALE
        if os.path.exists(path) and not OVERWRITE:
            continue
        key = (text, voice)
        if key in done and os.path.exists(done[key]):
            shutil.copy(done[key], path)
            print("copy", name); continue
        for attempt in range(3):
            try:
                await edge_tts.Communicate(text, voice, rate=RATE).save(path)
                break
            except Exception as e:
                print("retry", name, e); await asyncio.sleep(2)
        done[key] = path
        print("ok", name)

asyncio.run(main())
print("Selesai. Folder audio siap diunggah.")
