# Representable

Representable is creating maps of communities to fight for equal and impartial representation. The core web app is written in Django with Javascript/HTML/CSS frontend and Postgres/PostGIS backend. Our mapping & visualization app, currently in beta, is written in React & built using `createreactapp` and `Material UI`.

[![code style: prettier](https://img.shields.io/badge/code_style-prettier-ff69b4.svg)](https://github.com/prettier/prettier) [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

### Documentation
Check out our [Docs](https://docs.representable.org) site for a guide to installing Representable and contributing to various parts of the site. If you find any issues, we would love to know! Please open an issue request for any incomplete documentation.

### General Issue Reporting
For bug reports and general feature requests, please open a [Github issue](https://github.com/Representable/representable/issues/new/choose). We welcome all feedback and suggestions!

### Reporting Security Issues
We take security very seriously at Representable.org. Please send an email to [team@representable.org](mailto:team@representable.org) with any security issues and we'll open a private issue request with your concerns. We aim to respond to all security issues in a timely manner.

### Active Contributors
Our core team of engineers is currently 6 members strong, though we've been supported by many others along the way. See more about our team and how we work at [representable.org/about](https://representable.org/about/)

- Somya Arora
- Kyle Barnes
- Chukwuagoziem Uzoegwu
- Jason Yuan
- Anna Eaton
- Izzy Zaller

### Founders
Representable began as a final project for Princeton University course Advanced Programming Techniques, taught by Brian Kernighan. The original project team is:

- Theodor Marcu
- Lauren Johnston
- Preeti Iyer
- Somya Arora
- Kyle Barnes

### License
Representable is under the GPL-3.0 License.

## 2025 Updates 
Postgres 17
Dump and restore db from heroku postgres
(TODO: Compare with old repo)
export paths (see current bash_profile)
typed-ast to ast, which is included with python so can be removed from requirements.txt: https://github.com/python/typed_ast/issues/179
#Production Email Settings - comment out
#EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
### Python 3.13
Change runtime.txt to python 3.13

Change pyenv.cfg

Remove versions from requirements.txt

django.core.exceptions.ImproperlyConfigured: allauth.account.middleware.AccountMiddleware must be added to settings.MIDDLEWARE

ugettext to gettext:https://stackoverflow.com/questions/74826436/importerror-cannot-import-name-ugettext-from-django-utils-translation