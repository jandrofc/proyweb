def total_boleta(request):
    total = 0
    if request.user.is_authenticated:
        if "carrito"in request.session.keys():
            try:
                for key,value in request.session["carrito"].items():
                    total = total + (int(value['precio']))*(value['cantidad'])
            except KeyError:
                request.session['carrito']={}
                total = 0 
    return {'total_carrito':int(total)}



