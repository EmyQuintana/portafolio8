from django.shortcuts import render
from .models import Proyecto 

def index(request):
    
    proyectos_web_dinamicos = Proyecto.objects.all()

    proyectos_gamedev = [
        {
            'titulo': 'Demo App',
            'descripcion': 'Aplicación de ejemplo (Novela Visual) para mostrar el uso de tecnologías no web.',
            'tipo': 'Software',
            'tecnologias': ['Renpy', 'Python'],
            'link_demo': '#', 
        },
        {
            'titulo': 'UX/UI Prototipo',
            'descripcion': 'Diseño de interfaz en Figma para un proyecto de gestión de inventario.',
            'tipo': 'Diseño',
            'tecnologias': ['Figma', 'Prototipado'],
            'link_demo': '#',
        },
    ]
    
    # 3. Habilidades (Lista estática para rellenar la sección de habilidades)
    habilidades = {
        'frontend': [
            'HTML5',
            'CSS3',
            'Bootstrap',
            'Diseño Responsivo'
        ],
        'backend': [
            'Python',
            'Django',
            'PostgreSQL',
            'SQLite',
            'Git/GitHub',
            'Deployment (Render)'
        ],
        'organizacion': [
            'Agile/Scrum',
            'Resolución de Problemas'
        ]
    }
    
    # 4. Servicios 
    servicios = [
        {
            'titulo': 'Desarrollo Web Full Stack',
            'descripcion': 'Construcción de aplicaciones web robustas con Python/Django. Base de datos segura y escalable.',
            'icono': 'bi-code-slash'
        },
        {
            'titulo': 'Despliegue y Mantenimiento (DevOps)',
            'descripcion': 'Configuración de entornos de producción y despliegue en plataformas cloud (Render).',
            'icono': 'bi-cloud-check-fill'
        },
        {
            'titulo': 'Gestión de Proyectos SDLC',
            'descripcion': 'Aplicación de buenas prácticas en el ciclo de vida del software, desde la planificación hasta las pruebas.',
            'icono': 'bi-diagram-3'
        },
    ]
    
    # 5. Información de contacto (Estática)
    contacto = {
        'email': 'emily.quintana@ejemplo.com', 
        'github': 'https://github.com/EmyQuintana',
        'linkedin': 'https://www.linkedin.com/in/Emily-Quintana/',
    }
    
    # 6. Prepara el Contexto
    context = {
    
        'proyectos_web': proyectos_web_dinamicos, 
        'habilidades': habilidades,
        'servicios': servicios,
        'contacto': contacto,
    }
    
    # Renderiza la plantilla hija (index.html)
    return render(request, 'portafolio_app/index.html', context)