from PIL import Image

img = Image.open('/Users/guanguan/.gemini/antigravity/brain/c737c3cf-a105-4f7d-afa1-b315f57f0565/lighter_1780585918515.png')
img = img.convert("RGBA")

datas = img.getdata()
newData = []
for item in datas:
    if item[0] > 240 and item[1] > 240 and item[2] > 240:
        newData.append((255, 255, 255, 0))
    else:
        newData.append(item)

img.putdata(newData)
img = img.resize((48, 48), Image.Resampling.LANCZOS)
img.save('/Users/guanguan/Desktop/vibe coding project/幕布/lighter_cursor.png', "PNG")
