# NewsLetter.Django.0.5
 
# NewsLetter.Django.04

# ⌘⥏¤┊⊰⫷⋑_》╣≜〔[Creaciones]〕≜╠《_⋐⫸⊱┊¤⥑⌘

# Ambiente:

## Instalar:

    pip install virtualenv env

Crear:

↨↨↨ AMBOS CREAN UN ENTONRNO IGUAL? ↨↨↨ 

    python -m venv env

Activar:

    cd env/Scripts

    activate

Activar en Linux y mac:

    source env/bin/activate

## Requiriments.txt:
Creamos un archivo con el nombre requiriments.txt

    Django==4.0.4
    pillow==9.1.0
    Django-environ==0.8.1
    Django-tailwind==2.2.0

Ejecutamos en la terminal

    pip install -r requiriments.txt

# ⋖⥐⋗⫷·.·⫸○⫷⫸█■¯Δ|Δ⋖_⋗》¬﹝⍨﹞⌐《⋖_⋗Δ|Δ¯■█⫷⫸○⫷·.·⫸⋖⥐⋗

# StartProject:

## Crear:

### Opcion 1:

Crear una carpeta:

    mkdir src

Entrar:

    cd src

Crear proyecto:

    django-admin startproject core .

### Opcion 2:

Todo se crear dentro de una carpeta

    django-admin startproject project

## core:

### core\settings.py:
*importamos*
    
    from pathlib 
    import os
    import environ

*instalamos environ*

    env    = environ.Env()
    environ.Env.read_env()

*cortamos SECRET_KEY y DEBUG y creamos una archivo .env luego lo sustituimos* 
    
    SECRET_KEY = os.environ.get('SECRET_KEY')
    DEBUG = os.environ.get('DEBUG')

*Permitirá cualquier nombre de host que venga en un encabezado de Host*
    
    ALLOWED_HOSTS  = ['*']

    NPM_BIN = "/usr/bin/npm"

### Tailwind:

*INSTALLED_APPS*
    
    'core','tailwind',

*TERMINAL*

    python manage.py tailwind init

*INSTALLED_APPS*

    'theme'

*TAILWIND_APP_NAME*

    TAILWIND_APP_NAME = 'theme'
    INTERNAL_IPS = ["127.0.0.1",]

*TERMINAL*

    python manage.py tailwind install

### core\settings.py:

*TEMPLATES*

    'DIRS': [os.path.join(BASE_DIR, 'templates')],

*añadimos estos urls al final*

    STATIC_URL  = '/static/'
    STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')] 
    STATIC_ROOT = os.path.join(BASE_DIR, 'static_root') 
    MEDIA_URL   = '/media/' 
    MEDIA_ROOT  = os.path.join(BASE_DIR, 'media_static')

#### core/.env:
pegamos  
    
    SECRET_KEY=hd=ugsn49f4rk(er4yu#d*ca_hfw05nrh5-plxb-+0a$qgx&x6
    DEBUG =True

### Imagenes:
Para ello debemos de crear nustra carpeta static y media

### core/urls.py:
*importamos*

    from django.conf import settings 
    from django.conf.urls.static import static

*fuera de urlpatterns*
    
    if settings.DEBUG: 
        urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
        urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


# ⋖⥐⋗⫷·.·⫸○⫷⫸█■¯Δ|Δ⋖_⋗》¬﹝⍨﹞⌐《⋖_⋗Δ|Δ¯■█⫷⫸○⫷·.·⫸⋖⥐⋗
