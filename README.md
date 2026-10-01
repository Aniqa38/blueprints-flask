# Flask Blueprints

A teaching resource for **T Level Digital Production, Design and Development (DPDD), Year 2**. It shows how Flask **Blueprints** split an application into separate sections, so it stays organised as it grows. This lesson leads into MVC (Model–View–Controller) in the following session.

The lesson slides are included: [`blueprints-flask-Y2-lesson.pptx`](blueprints-flask-Y2-lesson.pptx)

---

## What learners practise

- Structuring a Flask project as packages instead of a single file
- Creating a Blueprint (`auth`) with its own routes and templates
- Registering a Blueprint with the main app
- Understanding how Blueprints support scalable applications and relate to MVC

---

## Project structure

```
blueprints-flask/
├── run.py                  # Starts the app and registers the auth blueprint
├── app/
│   ├── __init__.py         # Creates the Flask app
│   ├── routes.py           # Home page route  →  /
│   └── templates/
│       └── index.html
└── auth/
    ├── __init__.py         # Creates the auth blueprint
    ├── routes.py           # Auth route  →  /auth
    └── templates/
        └── index1.html
```

---

## Getting started

```bash
pip install -r requirements.txt
python run.py
```

Then visit:

- http://127.0.0.1:5000/ for the home page (main app)
- http://127.0.0.1:5000/auth for the auth page (served by the blueprint)

---

## Extension tasks

- Add a second blueprint, for example `reservation`, with its own route and template
- Give the auth blueprint a `url_prefix` so all its routes start with `/auth`
- Add a navigation bar linking the pages using `url_for()`

---

Lesson resource prepared by **Aniqa Arooj**, Digital Lecturer.
