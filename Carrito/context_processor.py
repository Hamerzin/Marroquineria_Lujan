def total_carrito(request):
    total = 0
    total2 = 0
    total3 = 0
    if request.user.is_authenticated:
        if "carrito" in request.session.keys():
            for key, value in request.session["carrito"].items():
                total += int(value["acumulado"])
                total2 += int(value["cantidad"])
                total3 =int(total2)
    return {"total_carrito": total, "total":total2, "total3":total3}

