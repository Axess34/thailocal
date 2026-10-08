# Builds OG image, hero phone visual, favicons and draft thumbnails for the Thai Local landing page.
from PIL import Image, ImageDraw
src=open('/workspace/fb-ad-udon/make_c_v2.py').read().split('base=grad(')[0]
exec(src)  # reuses the ad's helpers: S=2, F, grad, pin, phone, hexc, fit
WHITE=(255,255,255); YEL=(253,224,71); MINT=(209,250,229); ORANGE=(234,88,12)

# ---------- OG image 1200x630 ----------
W,H=1200*S,630*S
base=grad(W,H,hexc("#064E3B"),hexc("#0F766E")).convert("RGBA"); d=ImageDraw.Draw(base)
d.rounded_rectangle((s(56),s(48),s(471),s(110)),s(31),fill=WHITE)
pin(d,s(90),s(73),s(11),ORANGE)
d.text((s(114),s(79)),"Thai Local",font=F("Bold",32),fill=(17,24,39),anchor="lm")
d.text((s(296),s(81)),"thailocal.online",font=F("Medium",24),fill=(55,65,81),anchor="lm")
d.text((s(56),s(140)),"ดูเว็บไซต์",font=F("Bold",80),fill=WHITE)
d.text((s(52),s(232)),"ร้านคุณฟรี!",font=F("ExtraBold",100),fill=YEL)
d.text((s(58),s(372)),"See what your website",font=F("Bold",40),fill=WHITE)
d.text((s(58),s(420)),"could look like, free",font=F("Bold",40),fill=WHITE)
d.text((s(58),s(492)),"ธุรกิจท้องถิ่นทั่วไทย · Local businesses across Thailand",font=fit(d,"ธุรกิจท้องถิ่นทั่วไทย · Local businesses across Thailand","Medium",28,640),fill=MINT)
d.text((s(58),s(538)),"No setup fee · No contract",font=F("SemiBold",28),fill=MINT)
px,py,pw,ph=s(840),s(84),s(245),s(504)
phone(base,px,py,pw,ph,("#F59E0B","#EA580C")); d=ImageDraw.Draw(base)
bf=F("Bold",32); label="ฟรี · FREE"; tw=d.textlength(label,font=bf); bw=tw+s(48); bh=s(56)
bx1=px+pw+s(40); bx0=bx1-bw; by0=py-s(34); by1=by0+bh
d.rounded_rectangle((bx0-s(4),by0-s(4),bx1+s(4),by1+s(4)),(bh+s(8))//2,fill=WHITE)
d.rounded_rectangle((bx0,by0,bx1,by1),bh//2,fill=ORANGE)
d.text(((bx0+bx1)/2,(by0+by1)/2),label,font=bf,fill=WHITE,anchor="mm")
base.convert("RGB").resize((1200,630),Image.LANCZOS).save("img/og-image.jpg",quality=86,optimize=True,progressive=True)

# ---------- hero phone visual (transparent) ----------
hp=Image.new("RGBA",(s(420),s(760)),(0,0,0,0))
phone(hp,s(40),s(30),s(330),s(680),("#F59E0B","#EA580C"))
hp=hp.resize((420,760),Image.LANCZOS)
hp.save("img/hero-phone.webp",quality=88,method=6); hp.save("img/hero-phone.png",optimize=True)

# ---------- favicons ----------
for size,name in [(32,"favicon-32.png"),(180,"apple-touch-icon.png"),(512,"icon-512.png")]:
    k=8; im=Image.new("RGBA",(size*k,size*k),(0,0,0,0)); dd=ImageDraw.Draw(im)
    R=size*k
    dd.rounded_rectangle((0,0,R-1,R-1),int(R*0.22),fill=hexc("#0F766E"))
    r=R*0.2; cx=R/2; cy=R*0.40
    dd.ellipse((cx-r,cy-r,cx+r,cy+r),fill=ORANGE)
    dd.polygon([(cx-r*0.82,cy+r*0.55),(cx+r*0.82,cy+r*0.55),(cx,cy+r*2.25)],fill=ORANGE)
    dd.ellipse((cx-r*0.42,cy-r*0.42,cx+r*0.42,cy+r*0.42),fill="white")
    im.resize((size,size),Image.LANCZOS).save("img/"+name,optimize=True)

# ---------- example thumbnails (Ton Koon draft + two fictional example sites) ----------
# fictional example thumbs (example-isan-lantern-kitchen / example-khaen-kram-shop) are cropped the same way from
# 390x640@2x screenshots of https://axess34.github.io/<repo>/
for r in ['ton-koon-hotel']:
    im=Image.open(f'/tmp/pw/{r}.png').convert('RGB')   # 780x1280 (390x640 @2x)
    im=im.crop((0,0,780,1020)).resize((480,628),Image.LANCZOS)
    im.save(f'img/draft-{r}.webp',quality=74,method=6)
    im.save(f'img/draft-{r}.jpg',quality=78,optimize=True,progressive=True)
print("done")
