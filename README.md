# Baiata Equestrian Group — baiataequestrian.com

Static website (Arabic / English), hosted on GitHub Pages.

## Pages
| File | Page |
|---|---|
| `index.html` | Home: hero + tiles linking to every page + contact form |
| `history.html` | Our story: our grandfather Abdelkader Baiata and the family business |
| `horses.html` | Dressage & sport horse sales |
| `academy.html` | Workshops & mentoring, on site and online |
| `consulting.html` | Consulting & B2B sourcing |
| `capital.html` | Baiata Capital: investment approach |

## How to edit
- Text lives in `build.py`. Each line uses `T("Arabic", "English")`.
- After editing, run `python3 build.py` to regenerate the `.html` pages.
- Styles: `css/style.css`. Scripts: `js/main.js`. Images: `assets/`.

## To do
- Replace moodboard photos in `assets/` with the family's own photos.
- Add the grandfather's archive photo on `history.html`.
- Connect the contact form (e.g. Formspree) and add email / WhatsApp.
- Get the logo as SVG or transparent PNG from the designer.
