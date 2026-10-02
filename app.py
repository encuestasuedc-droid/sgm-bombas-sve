    # Último mantenimiento registrado
    ultimo_mantenimiento = Mantenimiento.query.order_by( Mantenimiento.id.desc() ).first()

    # Ranking de componentes: cantidad de intervenciones y costo total acumulado
    componentes_consulta = db.session.query(
        Mantenimiento.componente.label("componente"),
        db.func.count(Mantenimiento.id).label("cantidad"),
        db.func.sum(Mantenimiento.costo).label("costo_acumulado")
    ).group_by(
        Mantenimiento.componente
    ).order_by(
        db.func.count(Mantenimiento.id).desc()
    ).all()

    # Convertir el ranking de componentes en una lista sencilla
    ranking_componentes = []
    for fila in componentes_consulta:
        ranking_componentes.append({
            "componente": fila.componente,
            "cantidad": int(fila.cantidad or 0),
            "costo_acumulado": float(fila.costo_acumulado or 0)
        })

    # Renderizar la plantilla con todas las variables del dashboard
    return render_template(
        "dashboard.html",
        total=total,
        costo_total=costo_total,
        costo_promedio=costo_promedio,
        bombas_intervenidas=bombas_intervenidas,
        ranking=ranking,
        bomba_critica=bomba_critica,
        mayor_cantidad=mayor_cantidad,
        ultimo_mantenimiento=ultimo_mantenimiento,
        ranking_componentes=ranking_componentes
    )
