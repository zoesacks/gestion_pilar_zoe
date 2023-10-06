import datetime
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from contaduria.meses import MESES_CUSTOM
from contaduria.models import *
from facturas.models import factura
from django.core.paginator import Paginator, EmptyPage
from django.db.models import Sum

@login_required(login_url='/login/')
def aplicaciones_contaduria(request):

    context = {
        'lista_ventas': 'lista_ventas', 
        }
    return render(request, 'aplicaciones_contaduria.html', context)

@login_required(login_url='/login/')
def ingresos_contaduria(request):

    context = {
        'lista_ventas': 'lista_ventas', 
        }
    return render(request, 'ingresos_contaduria.html', context)

@login_required(login_url='/login/')
def gastos_contaduria(request):

    context = {
        'lista_ventas': 'lista_ventas', 
        }
    return render(request, 'gastos_contaduria.html', context)

@login_required(login_url='/login/')
def asientos_gastos(request):

    #gastos_query = asientosGastos.objects.all().filter(Fecha__year=2023).order_by('Fecha')
    gastos_query = asientosGastos.objects.all()

    proyecciones = proyeccionGastos.objects.all()

    # calculo del total para tarjetas
    # -------------------------------------------------------------------------------------
    total_pagado = gastos_query.aggregate(total_pagado=Sum('Pagado')/1000000)
 

    total_proyecciones = 0
    proyectado_mes_pagado = {}
    for x in proyecciones:
        mes = x.MES
        total = x.IMPORTE
        proyectado_mes_pagado[mes] = proyectado_mes_pagado.get(mes, 0) + total
        total_proyecciones += total

    total_proyecciones = total_proyecciones / 1000000
    # -------------------------------------------------------------------------------------

    # -------------------------------------------------------------------------------------
    # Configuracion de tabla
    
    items_per_page = 100

    paginator = Paginator(gastos_query, items_per_page)
    page_number = request.GET.get('page')

    if not page_number:
        page_number = 1
    try:
        page_obj = paginator.page(page_number)
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)

    context = {
        'proyecciones':proyecciones,
        'gastos_query':gastos_query,    
        'page_obj':page_obj,
        'total_pagado':total_pagado,
        'total_proyecciones':total_proyecciones,      
        }
    
    return render(request, 'asientosgastos.html', context)

@login_required(login_url='/login/')
def proyeccion_gastos(request):

    context = {
        'proyecciones':'proyecciones', 
        }
    
    return render(request, 'proyecciongastos.html', context)

@login_required(login_url='/login/')
def prestamos(request):

    context = {
        'prestamos':'prestamos', 
        }
    
    return render(request, 'prestamos.html', context)

@login_required(login_url='/login/')
def asientosingresos(request):

    context = {
        'asientosingreso':'asientosingresos', 
        }
    
    return render(request, 'asientosingresos.html', context)

@login_required(login_url='/login/')
def proyeccioningresos(request):

    context = {
        'proyeccioningresos':'proyeccioningresos', 
        }
    
    return render(request, 'proyeccioningreso.html', context)
