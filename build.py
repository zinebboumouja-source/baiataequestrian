#!/usr/bin/env python3
"""Builds the Baiata site pages from shared parts.
Run: python3 build.py  -> writes *.html in this folder (GitHub Pages ready).
"""
from pathlib import Path

ROOT = Path(__file__).parent
SITE = "https://baiataequestrian.com"


def T(ar, en):
    return f'<span lang="ar">{ar}</span><span lang="en">{en}</span>'


ARROW = '<svg width="16" height="10" viewBox="0 0 16 10" aria-hidden="true"><path d="M0 5h14M10 1l4 4-4 4" fill="none" stroke="currentColor"/></svg>'

NAV = [
    ("history.html", "القصة", "Our Story"),
    ("horses.html", "الدريساج والخيول", "Dressage & Horses"),
    ("academy.html", "الأكاديمية", "Academy"),
    ("consulting.html", "الاستشارات", "Consulting"),
    ("capital.html", "الاستثمار", "Capital"),
    ("index.html#contact", "تواصل", "Contact"),
]

FONTS = '<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;1,300;1,400&family=Jost:wght@300;400&family=Noto+Kufi+Arabic:wght@200;300;400&family=IBM+Plex+Sans+Arabic:wght@300;400&display=swap">'


def header(current):
    links = "".join(
        f'<a href="{h}"{" aria-current=\"page\"" if h == current else ""}>{T(a, e)}</a>' for h, a, e in NAV
    )
    return f'''<header class="top" id="top-bar">
  <div class="wrap">
    <div class="bar">
      <a class="home" href="index.html" aria-label="Baiata, home"><img src="assets/mark.png" alt="" width="684" height="712"><span>BAIATA</span></a>
      <nav aria-label="Main">{links}</nav>
      <div class="lang" role="group" aria-label="Language">
        <button id="btn-ar" type="button" data-set="ar" aria-pressed="true">عربي</button>
        <button id="btn-en" type="button" data-set="en" aria-pressed="false">EN</button>
      </div>
      <button class="menu-btn" id="menu-btn" type="button" aria-label="Menu" aria-expanded="false"><span></span></button>
    </div>
    <nav class="drawer" aria-label="Mobile">{links}</nav>
  </div>
</header>'''


FOOTER = f'''<footer>
  <div class="wrap">
    <div class="grid">
      <a class="brand" href="index.html" aria-label="Baiata, home"><img class="m" src="assets/mark.png" alt="" width="684" height="712"><img class="w" src="assets/wordmark.png" alt="Baiata Equestrian Group" width="1306" height="352"></a>
      <div class="cols">
        <div><span class="label">{T("الدار", "The House")}</span><a href="history.html">{T("قصتنا", "Our story")}</a><a href="index.html#contact">{T("تواصل", "Contact")}</a></div>
        <div><span class="label">{T("الخدمات", "Services")}</span><a href="horses.html">{T("الدريساج والخيول", "Dressage &amp; horses")}</a><a href="academy.html">{T("الأكاديمية", "Academy")}</a><a href="consulting.html">{T("الاستشارات", "Consulting")}</a><a href="capital.html">Baiata Capital</a></div>
        <div><span class="label">{T("الأسواق", "Markets")}</span><span style="color:rgba(255,255,255,.72)">{T("شمال إفريقيا", "North Africa")}</span><span style="color:rgba(255,255,255,.72)">{T("أوروبا", "Europe")}</span><span style="color:rgba(255,255,255,.72)">{T("الخليج", "The Gulf")}</span></div>
      </div>
    </div>
    <div class="base"><small>© Baiata Equestrian Group · <span lang="en">More than horses. We build opportunities.</span><span lang="ar">أكثر من خيول. نبني الفرص.</span></small><small>baiataequestrian.com</small></div>
  </div>
</footer>'''


def cta_band(img, ar, en):
    return f'''<section class="photo cta-band parallax">
  <div class="bg"><img src="assets/{img}" alt=""></div>
  <div class="wrap">
    <h2 class="display">{T(ar, en)}</h2>
    <a class="pill fill" href="index.html#contact">{T("تواصل معنا", "Get in touch")}</a>
  </div>
</section>'''


def page_hero(img, label, ar, en, par, pen, pos="50% 50%"):
    return f'''<section class="photo page-hero">
  <div class="bg"><img src="assets/{img}" alt="" style="object-position:{pos}" fetchpriority="high"></div>
  <div class="wrap">
    <span class="label">{label}</span>
    <h1 class="display">{T(ar, en)}</h1>
    <p>{T(par, pen)}</p>
  </div>
</section>'''


def doc(name, title, desc, body, current, artifact=False):
    head = f'<title>{title}</title>\n<meta name="claude:viewport-fit-sides" content="cover">\n<meta name="description" content="{desc}">\n{FONTS}\n<link rel="stylesheet" href="css/style.css">'
    content = f'{header(current)}\n<main>\n{body}\n</main>\n{FOOTER}\n<script src="js/main.js"></script>'
    if artifact:
        return f"{head}\n{content}\n"
    return f'''<!doctype html>
<html lang="ar" dir="rtl" data-lang="ar">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
{head}
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:image" content="{SITE}/assets/hero.jpg">
<link rel="canonical" href="{SITE}/{'' if name == 'index.html' else name}">
<link rel="icon" href="assets/mark.png">
</head>
<body>
{content}
</body>
</html>
'''


# ---------------------------------------------------------------- HOME
def split(img, label, ar, en, par, pen, href, more_ar, more_en, flip=False, dark=False, chips=None, pos="50% 50%"):
    cls = "split" + (" flip" if flip else "") + (" dark" if dark else "")
    chip_html = ""
    if chips:
        chip_html = '<div class="chips dark">' + "".join(f"<span>{T(a, e)}</span>" for a, e in chips) + "</div>"
    return f'''<section class="{cls}">
  <figure><img src="assets/{img}" alt="" style="object-position:{pos}"></figure>
  <div class="txt reveal">
    <span class="label">{label}</span>
    <h2 class="display">{T(ar, en)}</h2>
    <p>{T(par, pen)}</p>
    {chip_html}
    <a class="more" href="{href}">{T(more_ar, more_en)}{ARROW}</a>
  </div>
</section>'''


def tile(img, href, en, ar, den, dar, pos="50% 50%"):
    return f'''<a class="tile" href="{href}">
  <img src="assets/{img}" alt="" style="object-position:{pos}">
  <div class="t-in">
    <h2><span lang="en">{en}</span><span lang="ar">{ar}</span></h2>
    <p>{T(dar, den)}</p>
    <span class="t-arrow" aria-hidden="true">{ARROW}</span>
  </div>
</a>'''


HOME = f'''<section class="home-hero">
  <div class="bg"><img src="assets/band.jpg" alt="Grey and bay horses" fetchpriority="high"></div>
  <div class="wrap hh-in">
    <div class="logo"><img class="mark" src="assets/mark_gold.png" alt="" width="684" height="712"><h1 style="margin:0"><img class="word" src="assets/wordmark_gold.png" alt="Baiata Equestrian Group" width="1306" height="352"></h1></div>
    <div class="tagline label"><span>Investment</span><i></i><span>Trade</span><i></i><span>Equestrian</span></div>
    <p class="lead">{T("بيت فروسية عائلي، بين شمال إفريقيا وأوروبا والخليج.", "A family equestrian house between North Africa, Europe and the Gulf.")}</p>
    <div class="ctas"><a class="pill gold" href="#contact">{T("تواصل معنا", "Get in touch")}</a><a class="pill" href="history.html">{T("قصتنا", "Our story")}</a></div>
  </div>
</section>

<section class="tiles" aria-label="Baiata">
  {tile("h3.jpg", "capital.html", "Investment", "الاستثمار", "Invest in exceptional horses and promising opportunities.", "استثمار في خيول استثنائية وفرص واعدة.")}
  {tile("h1.jpg", "horses.html", "Dressage &amp; Horses", "الدريساج والخيول", "Selected horses, trained and sold with a full file.", "خيول مختارة، تُدرَّب وتُباع بملف كامل.", "60% 50%")}
  {tile("mane.jpg", "history.html", "Our Story", "قصتنا", "A family business, from our grandfather to today.", "أعمال عائلية، من الجد إلى اليوم.", "50% 30%")}
  {tile("leather.jpg", "academy.html", "Workshops &amp; Mentoring", "الورشات والمرافقة", "Learn, improve, grow. On site and online.", "تعلّم، تطوّر، انمُ. حضورياً وعن بُعد.")}
  {tile("hero.jpg", "consulting.html", "Consulting", "الاستشارات", "Expert advice for lasting success.", "خبرة عملية لنجاح يدوم.", "50% 8%")}
  {tile("h2.jpg", "consulting.html#sourcing", "B2B with Suppliers", "الموردون B2B", "Direct connections for stronger partnerships.", "علاقات مباشرة لشراكات أقوى.")}
</section>

<section class="home-story">
  <div class="wrap grid">
    <div class="label">{T("قصتنا", "Our Story")}</div>
    <div class="reveal">
      <p class="display">{T("بدأت الحكاية مع الجد عبد القادر بياطة وحبّه للخيل. واليوم يواصل الأحفاد الطريق بالقيم نفسها: الأصالة، والكلمة، والعناية بكل حصان.", "It began with our grandfather, Abdelkader Baiata, and his love of horses. Today his grandchildren carry it on with the same values: lineage, a kept word, and care for every horse.")}</p>
      <div class="foot"><p class="sign">{T("عبد القادر بياطة، رحمه الله", "In memory of Abdelkader Baiata")}</p><a class="more" href="history.html">{T("اقرأ القصة كاملة", "Read the full story")}{ARROW}</a></div>
    </div>
  </div>
</section>

<section class="bridge">
  <div class="wrap">
    <span class="label">{T("الجسر", "The Bridge")}</span>
    <h2 class="display reveal">{T("نصل بين ثلاث ضفاف تتكلم لغة الخيل", "Connecting three shores that speak the language of horses")}</h2>
    <div class="route">
      <svg viewBox="0 0 1000 24" preserveAspectRatio="none" aria-hidden="true"><path d="M7 12 C 300 -6, 700 30, 993 12"/></svg>
      <div class="stops">
        <div class="stop reveal"><span class="dot"></span><span class="label">Base</span><h3 class="display">{T("شمال إفريقيا", "North Africa")}</h3><p>{T("جذور العائلة وخبرتها، وقرب جغرافي من أوروبا.", "The family's roots and know-how, close to Europe.")}</p></div>
        <div class="stop reveal"><span class="dot"></span><span class="label">Source</span><h3 class="display">{T("أوروبا", "Europe")}</h3><p>{T("خيول رياضية بنسب موثق، وموردون ومعايير مرجعية.", "Sport horses with documented pedigrees, suppliers and benchmarks.")}</p></div>
        <div class="stop reveal"><span class="dot"></span><span class="label">Market</span><h3 class="display">{T("الخليج", "The Gulf")}</h3><p>{T("مشترون وأندية وإسطبلات خاصة تبحث عن خدمة راقية وموثوقة.", "Buyers, clubs and private stables seeking discreet, reliable service.")}</p></div>
      </div>
    </div>
  </div>
</section>

<section class="enquire dark" id="contact">
  <div class="wrap grid">
    <div>
      <span class="label">{T("تواصل", "Contact")}</span>
      <h2 class="display">{T("كيف نخدمك؟", "How may we help?")}</h2>
      <p class="intro-t">{T("شراء حصان أو بيعه، تسجيل في الأكاديمية، استشارة، أو فرصة استثمار. نرد شخصياً على كل طلب.", "Buying or selling a horse, joining the Academy, consulting or an investment opportunity. Every request receives a personal reply.")}</p>
    </div>
    <form id="enquiry-form" novalidate>
      <div class="f"><label for="f-name">{T("الاسم", "Name")}</label><input id="f-name" name="name" autocomplete="name"></div>
      <div class="f"><label for="f-country">{T("البلد", "Country")}</label><input id="f-country" name="country" autocomplete="country-name"></div>
      <div class="f full"><label for="f-topic">{T("الموضوع", "Subject")}</label>
        <select id="f-topic" name="topic">
          <option data-ar="الدريساج وشراء حصان" data-en="Dressage &amp; buying a horse">الدريساج وشراء حصان</option>
          <option data-ar="بيع حصان" data-en="Selling a horse">بيع حصان</option>
          <option data-ar="الأكاديمية: ورشة أو مرافقة" data-en="Academy: workshop or mentoring">الأكاديمية: ورشة أو مرافقة</option>
          <option data-ar="استشارة" data-en="Consulting">استشارة</option>
          <option data-ar="الاستثمار" data-en="Capital &amp; investment">الاستثمار</option>
        </select>
      </div>
      <div class="f full"><label for="f-msg">{T("رسالتك", "Your message")}</label><textarea id="f-msg" name="message"></textarea></div>
      <button class="send" type="submit">{T("إرسال", "Send")}</button>
      <p class="note" id="form-note" hidden>{T("الموقع في مرحلة التطوير، والرسائل لا تُرسل بعد.", "The site is in development. Messages are not sent yet.")}</p>
    </form>
  </div>
</section>'''

# ---------------------------------------------------------------- HISTORY
HISTORY = f'''{page_hero("mane.jpg", "Our Story", "عائلة واحدة، وشغف واحد بالخيل", "One family, one love of horses",
    "بياطة اسم عائلة قبل أن يكون علامة. حكاية بدأت مع الجد، وتستمر مع الأبناء والأحفاد.",
    "Baiata was a family name long before it was a brand. A story that began with our grandfather and continues with his children and grandchildren.", "50% 35%")}

<section>
  <div class="wrap lead-block">
    <span class="label">{T("الجد", "The Founder")}</span>
    <div class="body reveal">
      <p class="display">{T("الجد عبد القادر بياطة، رحمه الله، عاش مع الخيل وعلّم أبناءه أن الحصان أمانة قبل أن يكون تجارة.", "Our grandfather, Abdelkader Baiata, lived among horses and taught his children that a horse is a trust before it is a trade.")}</p>
      <p class="muted">{T("من خبرته في اختيار الخيول ورعايتها وتدريبها، ومن كلمته التي كان يعرفها الجميع، وُلدت سمعة العائلة في هذا الميدان.", "From his eye for choosing, caring for and training horses, and from a word everyone knew he would keep, the family's name in this field was born.")}</p>
    </div>
  </div>
</section>

<section style="padding-top:0">
  <div class="wrap">
    <div class="chapters">
      <article class="chapter reveal">
        <span class="when">{T("البدايات", "The beginning")}</span>
        <div><h3 class="display">{T("الجد والخيل", "A grandfather and his horses")}</h3><p>{T("بدأ كل شيء بشغف رجل واحد بالخيل، وبطريقة في العمل تقوم على الصدق والصبر والعناية بالتفاصيل.", "It all began with one man's passion for horses, and a way of working built on honesty, patience and attention to detail.")}</p></div>
      </article>
      <article class="chapter reveal">
        <span class="when">{T("عبر السنين", "Over the years")}</span>
        <div><h3 class="display">{T("أعمال عائلية", "A family business")}</h3><p>{T("انتقلت الخبرة من جيل إلى جيل: شراء الخيول الرياضية، وتدريبها، وإعادة بيعها، وبناء علاقات ثقة مع الفرسان والملاك والموردين.", "The know-how passed from one generation to the next: buying sport horses, training them, selling them on, and building trusted relationships with riders, owners and suppliers.")}</p></div>
      </article>
      <article class="chapter reveal">
        <span class="when">{T("اليوم", "Today")}</span>
        <div><h3 class="display">Baiata Equestrian Group</h3><p>{T("يجمع الأحفاد هذه الخبرة تحت اسم واحد، ليقدّموها لعملاء في شمال إفريقيا وأوروبا والخليج بمعايير مهنية حديثة.", "The grandchildren now bring this experience together under one name, offering it to clients across North Africa, Europe and the Gulf with modern professional standards.")}</p></div>
      </article>
    </div>
  </div>
</section>

<section class="on-dark">
  <div class="wrap">
    <div class="sec-head"><h2 class="display">{T("ثلاث قيم ورثناها", "Three values we inherited")}</h2><span class="label">{T("القيم", "Values")}</span></div>
    <div class="values">
      <div class="reveal"><h3 class="display">{T("الأصالة", "Lineage")}</h3><p>{T("نعرف أصل كل حصان ونوثّقه، ونحترم تاريخه كما نحترم تاريخنا.", "We know and document every horse's origins, and respect its history as we respect our own.")}</p></div>
      <div class="reveal"><h3 class="display">{T("الكلمة", "Our word")}</h3><p>{T("ما نعد به نكتبه في عقد واضح، وما نكتبه نلتزم به.", "What we promise, we put in a clear contract, and what we write, we honour.")}</p></div>
      <div class="reveal"><h3 class="display">{T("العناية", "Care")}</h3><p>{T("رفاه الحصان قبل الصفقة: رعاية، فحص بيطري، وتدريب يحترم إيقاعه.", "The horse's welfare comes before the deal: proper care, veterinary checks and training at its own pace.")}</p></div>
    </div>
  </div>
</section>

<section>
  <div class="wrap lead-block">
    <span class="label">{T("الأرشيف", "Archive")}</span>
    <figure class="archive reveal">
      <div class="frame">{T("مكان مخصص لصورة من أرشيف العائلة", "Reserved for a photograph from the family archive")}</div>
      <figcaption>{T("الجد عبد القادر بياطة، رحمه الله", "Abdelkader Baiata, our grandfather")}</figcaption>
    </figure>
  </div>
</section>

{cta_band("hero.jpg", "نكتب الفصل التالي معكم", "Write the next chapter with us")}'''

# ---------------------------------------------------------------- HORSES
def horse(img, disc, name, age, h, lvl, sb):
    return f'''<a class="card reveal" href="index.html#contact">
  <figure><img src="assets/{img}" alt=""></figure>
  <div><span class="label">{disc}</span><h3>{name}</h3></div>
  <dl class="spec">
    <div><dt>{T("العمر", "Age")}</dt><dd>{age}</dd></div>
    <div><dt>{T("الطول", "Height")}</dt><dd>{h}</dd></div>
    <div><dt>{T("المستوى", "Level")}</dt><dd>{lvl}</dd></div>
    <div><dt>{T("السلالة", "Studbook")}</dt><dd>{sb}</dd></div>
  </dl>
</a>'''


HORSES = f'''{page_hero("h2.jpg", "Baiata Horses", "الدريساج وبيع الخيول", "Dressage &amp; sport horses",
    "نختار كل حصان بعناية، نعدّه مع مختصين، ونقدّمه بملف كامل وشفاف.",
    "We choose every horse with care, prepare it with specialists, and present it with a complete, transparent file.", "50% 40%")}

<section>
  <div class="wrap lead-block">
    <span class="label">Dressage</span>
    <div class="body reveal">
      <p class="display">{T("الدريساج فن الانسجام بين الفارس والحصان. نرافق الخيول من سنواتها الأولى حتى المستويات العالية.", "Dressage is the art of harmony between horse and rider. We accompany horses from their first years to the upper levels.")}</p>
      <p class="muted">{T("نعمل مع مدربين ومختصين معتمدين، ونتابع كل حصان بخطة تدريب وسجل تقدم واضح، مع احترام إيقاعه وصحته.", "We work with qualified trainers and specialists, and follow every horse with a training plan and a clear progress record, at a pace that respects its health.")}</p>
    </div>
  </div>
</section>

<section class="on-dark">
  <div class="wrap">
    <div class="sec-head"><h2 class="display">{T("مسار الحصان معنا", "A horse's path with us")}</h2><span class="label">{T("المسار", "The path")}</span></div>
    <div class="rows" style="--hair:rgba(255,255,255,.16)">
      <div class="row reveal"><div><span class="label" style="color:var(--gold)">Young horses</span><h3 class="display">{T("الخيول الصغيرة", "Young horses")}</h3></div><p class="muted">{T("اختيار مبكر على أساس النسب والحركة والطبع، ثم تأسيس هادئ ومتدرج.", "Early selection on pedigree, movement and temperament, followed by calm, gradual foundations.")}</p></div>
      <div class="row reveal"><div><span class="label" style="color:var(--gold)">Medium levels</span><h3 class="display">{T("المستويات المتوسطة", "Medium levels")}</h3></div><p class="muted">{T("بناء القوة والتوازن، والمشاركة في مسابقات تمنح الحصان سجلاً رياضياً.", "Building strength and balance, with competitions that give the horse a sporting record.")}</p></div>
      <div class="row reveal"><div><span class="label" style="color:var(--gold)">Prix St-Georges &amp; beyond</span><h3 class="display">{T("المستويات العالية", "Upper levels")}</h3></div><p class="muted">{T("خيول جاهزة لفرسان متمرسين ومنافسات دولية.", "Horses ready for experienced riders and international competition.")}</p></div>
    </div>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="sec-head"><h2 class="display">{T("كيف نبيع حصاناً", "How we sell a horse")}</h2><span class="label">{T("البيع", "Sales")}</span></div>
    <div class="steps">
      <div class="step reveal"><h3>{T("الملف الكامل", "The full file")}</h3><p>{T("النسب، الوثائق، الصور والفيديو، والسجل الرياضي.", "Pedigree, papers, photos and video, competition record.")}</p></div>
      <div class="step reveal"><h3>{T("الفحص البيطري", "Veterinary check")}</h3><p>{T("فحص مستقل قبل البيع، مع إمكانية فحص يختاره المشتري.", "An independent pre-sale vetting, and a vetting of the buyer's choice if wished.")}</p></div>
      <div class="step reveal"><h3>{T("المعاينة والتجربة", "Viewing &amp; trial")}</h3><p>{T("زيارة الحصان وتجربته، حضورياً أو بفيديو مفصل.", "Visit and try the horse, in person or by detailed video.")}</p></div>
      <div class="step reveal"><h3>{T("العقد والنقل", "Contract &amp; transport")}</h3><p>{T("عقد مكتوب، وتنسيق النقل والتأمين حتى وصول الحصان.", "A written contract, with transport and insurance arranged until arrival.")}</p></div>
    </div>
  </div>
</section>

<section style="padding-top:0">
  <div class="wrap">
    <div class="sec-head"><h2 class="display">{T("خيول مختارة", "Selected horses")}</h2><span class="sample">{T("أمثلة توضيحية لشكل الكتالوج، وليست خيولاً معروضة للبيع", "Illustrative examples of the catalogue, not horses for sale")}</span></div>
    <div class="cards">
      {horse("h1.jpg", "Dressage", "Example I", "8", "1.70 m", "M", "KWPN")}
      {horse("h2.jpg", "Dressage", "Example II", "10", "1.72 m", "PSG", "Hanoverian")}
      {horse("h3.jpg", "Young horse", "Example III", "5", "1.66 m", "—", "Oldenburg")}
    </div>
  </div>
</section>

{cta_band("band.jpg", "تبحث عن حصان، أو تريد بيع حصانك؟", "Looking for a horse, or selling yours?")}'''

# ---------------------------------------------------------------- ACADEMY
ACADEMY = f'''{page_hero("leather.jpg", "Baiata Academy", "الأكاديمية: ورشات ومرافقة", "The Academy: workshops &amp; mentoring",
    "نقل خبرة العائلة إلى المهنيين والملاك والفرسان، حضورياً وعن بُعد.",
    "Passing on the family's experience to professionals, owners and riders, on site and online.")}

<section>
  <div class="wrap">
    <div class="sec-head"><h2 class="display">{T("صيغتان، نفس الجودة", "Two formats, one standard")}</h2><span class="label">{T("الصيغ", "Formats")}</span></div>
    <div class="duo">
      <article class="reveal"><span class="label">On site</span><h3 class="display">{T("حضورياً", "On site")}</h3><p>{T("ورشات في الإسطبلات والأندية، وعلى هامش المعارض والبطولات، بالتعاون مع شريكنا في تنظيم الفعاليات.", "Workshops at stables and clubs, and alongside shows and competitions, organised with our events partner.")}</p><ul><li>{T("مجموعات صغيرة", "Small groups")}</li><li>{T("تطبيق عملي مع الخيل", "Hands-on work with horses")}</li><li>{T("لقاءات بين المشترين والموردين", "Buyer–supplier meetings")}</li></ul></article>
      <article class="reveal"><span class="label">Online</span><h3 class="display">{T("عن بُعد", "Online")}</h3><p>{T("جلسات مباشرة ومسجّلة تتيح المتابعة من أي بلد، بالعربية والفرنسية والإنجليزية.", "Live and recorded sessions you can follow from any country, in Arabic, French and English.")}</p><ul><li>{T("جلسات مباشرة", "Live sessions")}</li><li>{T("وثائق ونماذج عملية", "Practical templates and documents")}</li><li>{T("أسئلة وأجوبة مع الفريق", "Q&amp;A with the team")}</li></ul></article>
    </div>
  </div>
</section>

<section class="on-dark">
  <div class="wrap">
    <div class="sec-head"><h2 class="display">{T("الورشات", "Workshops")}</h2><span class="label">Workshops</span></div>
    <div class="rows" style="--hair:rgba(255,255,255,.16)">
      <div class="row reveal"><div><span class="label" style="color:var(--gold)">Workshop I</span><h3 class="display">{T("بناء مشروع فروسية مربح", "Building a profitable equestrian business")}</h3></div><p class="muted">{T("هيكل التكاليف، التسعير، التدفق النقدي، ونموذج التشغيل وإدارة المخاطر.", "Cost structure, pricing, cash flow, operating model and risk.")}</p></div>
      <div class="row reveal"><div><span class="label" style="color:var(--gold)">Workshop II</span><h3 class="display">{T("شراء الخيول الرياضية وبيعها", "Buying and selling sport horses")}</h3></div><p class="muted">{T("خطوات الاختيار، الفحص البيطري، تكاليف الاحتفاظ، وخطة إعادة البيع.", "Selection, veterinary checks, holding costs and resale planning.")}</p></div>
      <div class="row reveal"><div><span class="label" style="color:var(--gold)">Workshop III</span><h3 class="display">{T("التجارة الدولية في الفروسية", "International equestrian trade")}</h3></div><p class="muted">{T("البحث عن الموردين، عروض الأسعار، التفاوض، والتنسيق عبر الحدود.", "Finding suppliers, quotations, negotiation and cross-border logistics.")}</p></div>
    </div>
  </div>
</section>

<section>
  <div class="wrap lead-block">
    <span class="label">Mentoring</span>
    <div class="body reveal">
      <p class="display">{T("مرافقة فردية لمن يريد أن يتقدم بخطوات ثابتة.", "One-to-one mentoring for those who want to progress with confidence.")}</p>
      <p class="muted">{T("لملاك الخيول، والفرسان، ومسيّري الإسطبلات، ومن يطلق مشروعاً جديداً. نحدد الأهداف معاً، ثم نلتقي بانتظام لمتابعة التقدم واتخاذ القرارات.", "For horse owners, riders, stable managers and anyone launching a new project. We set goals together, then meet regularly to review progress and take decisions.")}</p>
      <div class="steps" style="margin-top:20px">
        <div class="step"><h3>{T("جلسة تعارف", "First meeting")}</h3><p>{T("نفهم وضعك وأهدافك.", "We understand your situation and goals.")}</p></div>
        <div class="step"><h3>{T("خطة شخصية", "Personal plan")}</h3><p>{T("أولويات واضحة ومراحل محددة.", "Clear priorities and defined stages.")}</p></div>
        <div class="step"><h3>{T("لقاءات منتظمة", "Regular sessions")}</h3><p>{T("حضورياً أو عن بُعد.", "On site or online.")}</p></div>
        <div class="step"><h3>{T("تقييم", "Review")}</h3><p>{T("نقيس النتائج ونعدّل الخطة.", "We measure results and adjust the plan.")}</p></div>
      </div>
    </div>
  </div>
</section>

{cta_band("h3.jpg", "احجز مكانك في الورشة القادمة", "Reserve your seat at the next workshop")}'''

# ---------------------------------------------------------------- CONSULTING
CONSULTING = f'''{page_hero("band.jpg", "Baiata Consulting", "استشارات لأعمال الفروسية", "Consulting for equestrian businesses",
    "نضع خبرة سنوات في الميدان في خدمة الأندية والإسطبلات والمستثمرين.",
    "Years of field experience at the service of clubs, stables and investors.", "30% 50%")}

<section>
  <div class="wrap">
    <div class="sec-head"><h2 class="display">{T("ما نقدّمه", "What we offer")}</h2><span class="label">{T("الخدمات", "Services")}</span></div>
    <div class="rows">
      <div class="row reveal"><div><span class="label">Feasibility</span><h3 class="display">{T("دراسات الجدوى", "Feasibility studies")}</h3></div><p>{T("تقدير التكاليف والإيرادات والمخاطر قبل إطلاق نادٍ أو إسطبل أو مشروع جديد.", "Costs, revenue and risk assessed before launching a club, stable or new venture.")}</p></div>
      <div class="row reveal"><div><span class="label">Business plans</span><h3 class="display">{T("خطط الأعمال", "Business plans")}</h3></div><p>{T("نموذج تشغيل واضح، تسعير، وتوقعات مالية يمكن عرضها على الشركاء والممولين.", "A clear operating model, pricing and financial projections you can present to partners and lenders.")}</p></div>
      <div class="row reveal"><div><span class="label">Operations</span><h3 class="display">{T("تنظيم الإسطبلات", "Stable operations")}</h3></div><p>{T("تحسين الإيواء والتغذية والرعاية والتدريب، وضبط المصاريف لكل حصان.", "Improving livery, feeding, care and training, and controlling costs per horse.")}</p></div>
      <div class="row reveal" id="sourcing"><div><span class="label">Sourcing</span><h3 class="display">{T("التوريد", "Sourcing")}</h3></div><p>{T("البحث عن موردين موثوقين للمعدات والمستلزمات والأعلاف، ومقارنة العروض وتنسيق الشحن.", "Finding reliable suppliers of equipment, supplies and feed, comparing quotes and coordinating shipping.")}</p></div>
      <div class="row reveal"><div><span class="label">Market entry</span><h3 class="display">{T("دخول الأسواق", "Market entry")}</h3></div><p>{T("مرافقة دخول أسواق الخليج وأوروبا: الشركاء، القنوات، والإجراءات.", "Support entering Gulf and European markets: partners, channels and procedures.")}</p></div>
    </div>
  </div>
</section>

<section class="on-dark">
  <div class="wrap">
    <div class="sec-head"><h2 class="display">{T("طريقة عملنا", "How we work")}</h2><span class="label">{T("المنهج", "Method")}</span></div>
    <div class="steps">
      <div class="step reveal"><h3>{T("الاستماع", "Listening")}</h3><p>{T("نفهم مشروعك وأهدافك وإمكاناتك.", "We understand your project, goals and means.")}</p></div>
      <div class="step reveal"><h3>{T("التشخيص", "Diagnosis")}</h3><p>{T("زيارة ميدانية وتحليل الأرقام.", "A site visit and a look at the numbers.")}</p></div>
      <div class="step reveal"><h3>{T("الخطة", "The plan")}</h3><p>{T("توصيات عملية بأولويات وتكاليف واضحة.", "Practical recommendations with clear priorities and costs.")}</p></div>
      <div class="step reveal"><h3>{T("المتابعة", "Follow-up")}</h3><p>{T("نرافق التنفيذ حسب حاجتك.", "We support implementation as needed.")}</p></div>
    </div>
  </div>
</section>

{cta_band("hero.jpg", "لنتحدث عن مشروعك", "Let's talk about your project")}'''

# ---------------------------------------------------------------- CAPITAL
CAPITAL = f'''{page_hero("h1.jpg", "Baiata Capital", "الاستثمار في عالم الخيل", "Investing in the equestrian world",
    "استثمار انتقائي وصبور في الخيول الرياضية ومشاريع الفروسية، مبني على خبرة الميدان والشفافية.",
    "Selective, patient investment in sport horses and equestrian projects, built on field experience and transparency.", "60% 40%")}

<section>
  <div class="wrap lead-block">
    <span class="label">{T("النهج", "Approach")}</span>
    <div class="body reveal">
      <p class="display">{T("لا نستثمر إلا فيما نفهمه: الخيل، والإسطبلات، والأعمال المرتبطة بها.", "We only invest in what we understand: horses, stables and the businesses around them.")}</p>
      <p class="muted">{T("نختار الفرص واحدة واحدة، وندرس كل فرصة بملف مالي كامل قبل أي قرار، ونعمل مع شركاء يشاركوننا القيم نفسها.", "We choose opportunities one by one, study each with a complete financial file before any decision, and work with partners who share our values.")}</p>
    </div>
  </div>
</section>

<section class="on-dark">
  <div class="wrap">
    <div class="sec-head"><h2 class="display">{T("مجالات الاستثمار", "Where we invest")}</h2><span class="label">{T("المجالات", "Areas")}</span></div>
    <div class="rows" style="--hair:rgba(255,255,255,.16)">
      <div class="row reveal"><div><span class="label" style="color:var(--gold)">Sport horses</span><h3 class="display">{T("الخيول الرياضية", "Sport horses")}</h3></div><p class="muted">{T("شراء خيول واعدة، إعدادها، ثم إعادة بيعها في الوقت المناسب.", "Buying promising horses, preparing them, and selling at the right moment.")}</p></div>
      <div class="row reveal"><div><span class="label" style="color:var(--gold)">Projects</span><h3 class="display">{T("مشاريع الفروسية", "Equestrian projects")}</h3></div><p class="muted">{T("أندية، إسطبلات، وخدمات مرتبطة بالقطاع.", "Clubs, stables and related services.")}</p></div>
      <div class="row reveal"><div><span class="label" style="color:var(--gold)">Partnerships</span><h3 class="display">{T("الشراكات", "Partnerships")}</h3></div><p class="muted">{T("استثمار مشترك مع شركاء ومهنيين في فرص محددة.", "Co-investment with partners and professionals in specific opportunities.")}</p></div>
    </div>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="sec-head"><h2 class="display">{T("كل حصان ملف مالي مستقل", "Every horse, its own financial file")}</h2><span class="label">{T("الانضباط", "Discipline")}</span></div>
    <div class="duo">
      <article class="reveal"><span class="label">Full cost</span><h3 class="display">{T("التكلفة الكاملة", "The full cost")}</h3><ul><li>{T("سعر الشراء وعمولة الاقتناء", "Purchase price and acquisition fee")}</li><li>{T("الفحص البيطري والوثائق", "Vetting and papers")}</li><li>{T("التدريب والإيواء والرعاية", "Training, livery and care")}</li><li>{T("التأمين والنقل", "Insurance and transport")}</li><li>{T("التسويق وعمولة البيع", "Marketing and sales commission")}</li></ul></article>
      <article class="reveal"><span class="label">Indicators</span><h3 class="display">{T("ما نقيسه", "What we measure")}</h3><ul><li>{T("الربح المباشر بعد كل التكاليف", "Net result after all costs")}</li><li>{T("العائد على التكلفة", "Return on cost")}</li><li>{T("مدة الاحتفاظ بالحصان", "Holding period")}</li><li>{T("رأس المال المجمّد", "Capital tied up")}</li><li>{T("سيناريو انخفاض السعر", "Downside price scenario")}</li></ul></article>
    </div>
  </div>
</section>

<section style="padding-top:0">
  <div class="wrap">
    <p class="notice">{T("الاستثمار في الخيول ينطوي على مخاطر، ولا نضمن أي عائد. كل شراكة تتم بعقد مكتوب يحدد دور كل طرف، ووفق القوانين المعمول بها.", "Investing in horses carries risk and no return is guaranteed. Every partnership is set out in a written contract defining each party's role, in line with applicable regulations.")}</p>
  </div>
</section>

{cta_band("h2.jpg", "ناقش معنا فرصة استثمار", "Discuss an investment opportunity")}'''

PAGES = [
    ("index.html", "Baiata Equestrian Group", "Family equestrian house: dressage and sport horses, academy, consulting and capital, between North Africa, Europe and the Gulf.", HOME, ""),
    ("history.html", "Baiata · Our Story", "The story of the Baiata family and its grandfather Abdelkader Baiata.", HISTORY, "history.html"),
    ("horses.html", "Baiata · Dressage & Horses", "Dressage training and sport horse sales with a full file for every horse.", HORSES, "horses.html"),
    ("academy.html", "Baiata Academy", "Workshops and mentoring for equestrian professionals, on site and online.", ACADEMY, "academy.html"),
    ("consulting.html", "Baiata Consulting", "Consulting for clubs, stables and equestrian investors.", CONSULTING, "consulting.html"),
    ("capital.html", "Baiata Capital", "Selective investment in sport horses and equestrian projects.", CAPITAL, "capital.html"),
]

if __name__ == "__main__":
    import sys
    artifact_dir = Path(sys.argv[1]) if len(sys.argv) > 1 else None
    for name, title, desc, body, cur in PAGES:
        (ROOT / name).write_text(doc(name, title.replace("&", "&amp;"), desc, body, cur), encoding="utf-8")
        if artifact_dir:
            artifact_dir.mkdir(parents=True, exist_ok=True)
            art = doc(name, title.replace("&", "&amp;"), desc, body, cur, artifact=(name == "index.html"))
            (artifact_dir / name).write_text(art, encoding="utf-8")
    print("built", len(PAGES), "pages")
