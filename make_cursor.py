from PIL import Image

# Open the scraper image
img = Image.open('/Users/guanguan/.gemini/antigravity/brain/c737c3cf-a105-4f7d-afa1-b315f57f0565/scraper_1780576766029.png')
img = img.convert("RGBA")

datas = img.getdata()

newData = []
for item in datas:
    # change all white (also shades of whites)
    # to transparent
    if item[0] > 240 and item[1] > 240 and item[2] > 240:
        newData.append((255, 255, 255, 0))
    else:
        newData.append(item)

img.putdata(newData)

# Resize to cursor size (max 128x128 for browsers, 48x48 is good)
img = img.resize((48, 48), Image.Resampling.LANCZOS)
img.save('/Users/guanguan/Desktop/vibe coding project/幕布/scraper_cursor.png', "PNG")
