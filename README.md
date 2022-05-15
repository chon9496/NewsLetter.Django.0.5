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

# StartApp:
*cmd*
    
    python manage.py startapp newsletters

## core/settings.py:
*INSTALLED_APPS*
'newsletters',

## newsletters/models.py
NewsletterUser es el que guardara a los usuarios 
para ello usaremos la variable; 
*null=Falsees* para que el campo sea obligatorio
*unique=True* hace que si el correo ya esta registrado no se
vuelva a mandar;
*auto_now_add=True* sirve para agregarla la hora 
de registro automaticamente


    class NewsletterUser(models.Model):
        email      = models.EmailField(null=False, unique=True)
        date_added = models.DateTimeField(auto_now_add=True)

        def __str__(self):
            return self.email

Newsletter es el correo que mandaremos
en la variablen 
_Name_ es para el nombre;
_Subject_ es para el tema; 
_Body_ usamos (blank=True,null=True) que permitira mandar 
correos en blanco;
_Email_ tiene ManyToManyField este establece una relacion 
entre modelos;
NewsletterUser que hace referencia a la clase creada 
previamente;
_Created_ con el *auto_now_add=true* agrega automaticamente 
la hora

    class Newsletter(models.Model):
        name    = models.CharField(max_length=250)
        subject = models.CharField(max_length=250)
        body    = models.TextField(blank=True, null=True)
        email   = models.ManyToManyField(NewsletterUser)
        created = models.DateTimeField(auto_now_add=True)

        def __str__(self):
            return self.name

como ya sabemos se debe de hacer las migraciones cada ves
que agregamos modelos en models.py y hacemos esto para que 
lo que hacemos se vea reflejado en la base de datos


## Migraciones:
### Migrations:
python manage.py makemigrations
### Migrate:
python manage.py migrate


# ⋖⥐⋗⫷·.·⫸○⫷⫸█■¯Δ|Δ⋖_⋗》¬﹝⍨﹞⌐《⋖_⋗Δ|Δ¯■█⫷⫸○⫷·.·⫸⋖⥐⋗

# Formularios:
creamos forms.py en newsletters

## newsletters/forms.py:
Hacemos unas importaciones de .models y creamos nuestras
clases
una que es para el email y la otra sera para el mensaje
Ambas funcionan con las clases creadas en models

    from django import forms
    from .models import Newsletter, NewsletterUser


    class NewsletterUserSignUpForm(forms.ModelForm):
        class Meta:
            model = NewsletterUser
            fields = ['email']


    class NewsletterCreationForm(forms.ModelForm):
        class Meta:
            model = Newsletter
            fields=['name','subject','body','email']


# ⋖⥐⋗⫷·.·⫸○⫷⫸█■¯Δ|Δ⋖_⋗》¬﹝⍨﹞⌐《⋖_⋗Δ|Δ¯■█⫷⫸○⫷·.·⫸⋖⥐⋗
