    print(archivo)
    writer = csv.DictWriter(archivo_nuevo)
    for dato in datos:
        dato["algo"] = id
        writer.writerow(dato)