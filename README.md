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

# Vistas: 

## Suscribirse:

### newsletters/views.py:

    from django.contrib import messages
    from newsletters.models import NewsletterUser
    from django.shortcuts import render
    from .forms import NewsletterUserSignUpForm
    from django.conf import settings
    from django.template.loader import render_to_string
    from django.core.mail import send_mail, EmailMessage

empesamos jalando request.POST a form y si no hay nada 
no jalas nada

    def newsletter_signup(request):
        form =NewsletterUserSignUpForm(request.POST or None)

decimos que si el formulario es valido la informacion la
tomamos como una instancia

    if form.is_valid():
        instance=form.save(commit=False) 

aca vemos si ese usuario existe pasandola por filter 
decimos que hacemos un filtro a email y email es la
instancia y que queremos el email de la instancia
filter(email=instance.email) y si existe nosa saldra un
mensaje

    if NewsletterUser.objects.filter(email=instance.email).exists():
        messages.warning(request, 'Email already exists.')

si el correo no existe se guarda como instancia y sale un 
mensaje y desde ahi mismo mandamos el correo en frpm_email
tenemos que agregar EMAIL_HOST_USER en settings.py

    else:
        instance.save()
        messages.success(request, 'Hemos enviado un correo electronico a su correo, abrelo para continuar con el entrenamiento')
        #Correo electronico
        subject="Libro de cocina"
        from_email=settings.EMAIL_HOST_USER
        to_email=[instance.email]

·Templates y sus ubicaniones
·Luego lo convertimos a cadena para poder usarlo en el 
envio
·para el envio final creamos la variable y ponemos 
EmailMessage
a todo esto le damos un subject y el from_email, to_email 
y html_message
·Para poder enviarlo decimos que el contenido sera tipo 
html luego ponemos  message.send() para enviarlo
·Tenemos que darle un contexto tambien
        'form':form,
·Luego ya ponemos en return porque las funciones lo 
requieren y retornamos: 
render(request, 'start-here.html', context)
request para enviar info al servidor y al cliente
start-.htlm para el llamado a la accion para registrar 
el correo sera la pagina 
y para renderizar poenmos el contexto 
asi ya estara lista nuestra funcion

            html_template='newsletters/email_templates/welcome.html'
            html_message=render_to_string(html_template)
            message=EmailMessage(subject,html_message, from_email, to_email)
            message.content_subtype='html'
            message.send()

    context={
        'form':form,
    }
    return render(request, 'start-here.html', context)

### core/settings.py:

    EMAIL_HOST_USER ='davidarangolucar@gmail.com'
    
    EMAIL_BACKEND='django.core.mail.backends.console.EmailBackend'

### templates/newsletters/email_templates/welcome.html:
dentro de templates creas un start-here.html una carptea
newsletters dentro de esta creamos otra email_templates 
y aca dentro creamos welcome.html
#### welcome.html:

    <html>
        <head>
        </head>
        <body>
        <h2>Bienvenido<h2>
            <p> Here we'll send you important information <p>
        </body>
    </html> 

### start-here.html:

    {% extends 'base.html' %}

    {% block content %}
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
    <!-- We've used 3xl here, but feel free to try other max-widths based on your needs -->
    <div class="max-w-3xl mx-auto">
        <!-- Content goes here -->

            <div class="bg-white">
                <div class="max-w-7xl mx-auto py-12 px-4 sm:px-6 lg:py-16 lg:px-8">
                    <h2 class="inline text-3xl font-extrabold tracking-tight text-gray-900 sm:block sm:text-4xl">
                    Want product news and updates?
                    </h2>
                    <p class="inline text-3xl font-extrabold tracking-tight text-indigo-600 sm:block sm:text-4xl">Sign up for our newsletter.</p>
                    <form method="POST" class="mt-8 sm:flex">
                    {% csrf_token %}
                        <label for="emailAddress" class="sr-only">Email address</label>
                        <input id="emailAddress" name="email" type="email" autocomplete="email" required class="mr-3 px-5 py-3 placeholder-gray-500 focus:ring-indigo-500 focus:border-indigo-500 sm:max-w-xs border-gray-300 rounded-md" placeholder="Enter your email">
                        
                        <div class="mt-3 rounded-md shadow sm:mt-0 sm:ml-3 sm:flex-shrink-0">
                            <button type="submit" class="w-full flex items-center justify-center px-5 py-3 border border-transparent text-base font-medium rounded-md text-white bg-indigo-600 hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500">
                            Notify me
                            </button>
                        </div>
                    </form>
                </div>
            </div>

    </div>
    </div>
    {% endblock content %}



# ⋖⥐⋗⫷·.·⫸○⫷⫸█■¯Δ|Δ⋖_⋗》¬﹝⍨﹞⌐《⋖_⋗Δ|Δ¯■█⫷⫸○⫷·.·⫸⋖⥐⋗