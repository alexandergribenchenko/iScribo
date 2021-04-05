def xml_generator_V_02(path_excel, path_output):

    import pandas as pd

    path_format = 'patrones_xml_base.txt'
    path_excel = path_excel
    path_output = path_output

    handler = open(path_format)
    contenido = handler.read()

    matriz_reemplazos = pd.read_excel(path_excel, engine='openpyxl', header=None)

    salida=''
    for index in range(len(matriz_reemplazos)):

        comment_replace = 'comment'
        id_replace = matriz_reemplazos[0][index] + '/' + matriz_reemplazos[1][index]
        name_replace = id_replace
        # token_replace = matriz_reemplazos[0][index]
        message_replace = matriz_reemplazos[2][index]
        sugestion_replace = matriz_reemplazos[1][index]

        token_replace_in = matriz_reemplazos[0][index]
        token_replace=''
        for x in token_replace_in.split():
            token_replace+='<token>'+x+'</token>'+'\n'+'  '
        token_replace = token_replace[:-3]

        contenido_temp = contenido.replace("comment_replace", comment_replace)
        contenido_temp = contenido_temp.replace("id_replace", id_replace)
        contenido_temp = contenido_temp.replace("name_replace", name_replace)
        contenido_temp = contenido_temp.replace("<token>token_replace</token>", token_replace)
        contenido_temp = contenido_temp.replace("message_replace", message_replace)
        contenido_temp = contenido_temp.replace("sugestion_replace", sugestion_replace)

        salida+=contenido_temp+'\n\n'

    text_file = open(path_output, "w")
    text_file.write(salida)
    text_file.close()
    return