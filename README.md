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

## DeSuscribirse:

### newsletters/views.py:

Indicamos que trabajaremos con el formulario siguiente
y decimos que si existe este correo en la base de datos
este se eliminara y nos mostrara el mensaje de eliminado
De lo contrario nos saldra un mensaje warnig
Agregamos contexto
 y retornamos render


    def newsletter_unsubscribe(request):
        form =NewsletterUserSignUpForm(request.POST or None)

        if form.is_valid():
            instance = form.save(commit=False)
            if NewsletterUser.objects.filter(email=instance.email).exists():
                NewsletterUser.objects.filter(email=instance.email).delete()
                messages.success(request, 'Email has been removed.')
            else:
                print('Email not found.')
                messages.warning(request, 'Email not found.')

        context = {
            "form": form,
        }

        return render(request, 'unsuscribe.html', context)

### src/newsletters/admin.py:

    from .models import NewsletterUser,Newsletter

    admin.site.register(NewsletterUser)
    admin.site.register(Newsletter)

### templates:
crear unsuscribe.html

    {% extends 'base.html' %}
    {% block content %}
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
    <!-- We've used 3xl here, but feel free to try other max-widths based on your needs -->
    <div class="max-w-3xl mx-auto">
        <!-- Content goes here -->
            <div class="bg-white">
                <div class="max-w-7xl mx-auto py-12 px-4 sm:px-6 lg:py-16 lg:px-8">
                    <p class="inline text-3xl font-extrabold tracking-tight text-indigo-600 sm:block sm:text-4xl">Unsubscribe from our newsletter.</p>
                    <form method="POST" class="mt-8 sm:flex">
                        {% csrf_token %}
                        <label for="emailAddress" class="sr-only">Email address</label>
                        <input id="emailAddress" name="email" type="email" autocomplete="email" required class="mr-3 px-5 py-3 placeholder-gray-500 focus:ring-indigo-500 focus:border-indigo-500 sm:max-w-xs border-gray-300 rounded-md" placeholder="Enter your email">
                        <div class="mt-3 rounded-md shadow sm:mt-0 sm:ml-3 sm:flex-shrink-0">
                            <button type="submit" class="w-full flex items-center justify-center px-5 py-3 border border-transparent text-base font-medium rounded-md text-white bg-indigo-600 hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500">
                            Unsubscribe
                            </button>
                        </div>
                    </form>
                </div>
            </div>
    </div>
    </div>
    {% endblock content %}
    
### newsletters:
creamos urls.py


Indicamos que trabajaremos con el formulario siguiente
comenzamos declarando la instancia del usuario y decimos 
si existe este correo en la base de datos este se eliminara
y nos mostrara el mensaje de eliminado
De lo contrario nos saldra un mensaje warnig
Agregamos contexto
para terminar retornamos render pero con ussuscribe.html
    
    from django.urls import path
    from .views import newsletter_signup, newsletter_unsubscribe

    app_name="newsletters"

    urlpatterns = [
        path('entrenamiento/', newsletter_signup, name="optin"),
        path('unsubscribe/', newsletter_unsubscribe, name="unsubscribe"),
    ]

### core/urls.py:
from django.urls import path,include
al momento de hacer nuestro path en core tenemos que 
especificar que estamos incluyendo a urls de newletter

    urlpatterns = [
        path('admin/', admin.site.urls),
        path('newsletter/', include('newsletters.urls',namespace='newsletter')),

    ]

## Opt-in:

### src/templates/base.html:

    {% load static tailwind_tags %}
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Document</title>

        <script src="https://cdn.jsdelivr.net/gh/alpinejs/alpine@v2.8.2/dist/alpine.min.js" defer></script>

        {% tailwind_css %}
    </head>
    <body>
    {% block content %}

    {% endblock content %}
    </body>
    </html>

## Crear usuario:

    python manage.py createsuperuser
    
# ⋖⥐⋗⫷·.·⫸○⫷⫸█■¯Δ|Δ⋖_⋗》¬﹝⍨﹞⌐《⋖_⋗Δ|Δ¯■█⫷⫸○⫷·.·⫸⋖⥐⋗


# MensajeEnPantalla:
esto es el mensajito que sale cuando te registrar el mensaje pantalla

## src/templates/messages.html:
    
    {% if messages %}
    {% for message in messages %}
    <div x-data="{ open: true }" @keydown.window.escape="open = false" x-show="open"
        class="fixed z-10 inset-0 overflow-y-auto" aria-labelledby="modal-title" x-ref="dialog" aria-modal="true">
        <div class="flex items-end justify-center min-h-screen pt-4 px-4 pb-20 text-center sm:block sm:p-0">
            <div x-show="open" x-transition:enter="ease-out duration-300" x-transition:enter-start="opacity-0"
                x-transition:enter-end="opacity-100" x-transition:leave="ease-in duration-200"
                x-transition:leave-start="opacity-100" x-transition:leave-end="opacity-0"
                x-description="Background overlay, show/hide based on modal state."
                class="fixed inset-0 bg-gray-500 bg-opacity-75 transition-opacity" @click="open = false" aria-hidden="true">
            </div>

            <!-- This element is to trick the browser into centering the modal contents. -->
            <span class="hidden sm:inline-block sm:align-middle sm:h-screen" aria-hidden="true">​</span>

            <div x-show="open" x-transition:enter="ease-out duration-300"
                x-transition:enter-start="opacity-0 translate-y-4 sm:translate-y-0 sm:scale-95"
                x-transition:enter-end="opacity-100 translate-y-0 sm:scale-100" x-transition:leave="ease-in duration-200"
                x-transition:leave-start="opacity-100 translate-y-0 sm:scale-100"
                x-transition:leave-end="opacity-0 translate-y-4 sm:translate-y-0 sm:scale-95"
                x-description="Modal panel, show/hide based on modal state."
                class="inline-block align-bottom dark:bg-dark-second bg-white rounded-lg px-4 pt-5 pb-4 text-left overflow-hidden shadow-xl transform transition-all sm:my-8 sm:align-middle sm:max-w-sm sm:w-full sm:p-6">
                <div>
                    <div class="mx-auto flex items-center justify-center h-12 w-12 rounded-full bg-green-100">
                        <svg class="h-6 w-6 text-green-600" x-description="Heroicon name: outline/check"
                            xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor"
                            aria-hidden="true">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path>
                        </svg>
                    </div>
                    <div class="mt-3 text-center sm:mt-5">
                        <h3 class="text-lg leading-6 font-medium dark:text-dark-txt text-gray-900" id="modal-title">
                            {{ message.tags }}
                        </h3>
                        <div class="mt-2">
                            <p class="text-sm  dark:text-dark-txt text-gray-500">
                                {{ message }}
                            </p>
                        </div>
                    </div>
                </div>
                <div class="mt-5 sm:mt-6">
                    <button type="button"
                        class="inline-flex justify-center w-full rounded-md border border-transparent shadow-sm px-4 py-2 bg-blue-600 text-base font-medium text-white hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-500 sm:text-sm"
                        @click="open = false">
                        Ok
                    </button>
                </div>
            </div>

        </div>
    </div>
    {% endfor %}
    {% endif %}

## src/templates/base.html:

    <body>
    {% block messages %}{% include 'messages.html' %}{% endblock messages %}
    {% block content %}

    {% endblock content %}
    </body>

# ⋖⥐⋗⫷·.·⫸○⫷⫸█■¯Δ|Δ⋖_⋗》¬﹝⍨﹞⌐《⋖_⋗Δ|Δ¯■█⫷⫸○⫷·.·⫸⋖⥐⋗