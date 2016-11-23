from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages

def compra(request):
#    if request.method == "POST":
#        formulario = CompraForm(request.POST)
#        if formulario.is_valid():
#            com = formulario.save(commit=False)
#            for usuario_id in request.POST.getlist('usuario'):
#                for producto_id in request.POST.getlist('producto'):
#                    com = Compra(usuario_id=usuario_id,
#                    producto_id=producto_id,
#                    cantidad=formulario.cleaned_data['cantidad'],
#                    fecha=formulario.cleaned_data['fecha'],
#                    com.save()
#                    return render(request, 'cita/compra.html', {'formulario':formulario})
#    else:
#        formulario = CompraForm()
    return render(request, 'ventas/compra.html', {})
