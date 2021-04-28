def xml_generator_V_03(path_excel, path_output):

    import pandas as pd

    path_format = 'patrones_xml_base.txt'
    path_excel = path_excel
    path_output = path_output

    handler = open(path_format)
    contenido = handler.read()

    matriz_reemplazos = pd.read_excel(path_excel, engine='openpyxl', header=None)

    salida=''
    for index in range(len(matriz_reemplazos)):

        # Entradas sin casos diferentes
        comment_replace = 'comment'
        id_replace = matriz_reemplazos[0][index] + '/' + matriz_reemplazos[1][index]
        name_replace = id_replace
        message_replace = matriz_reemplazos[2][index]

        # Reemplazos para entradas sin casos diferentes
        contenido_temp = contenido.replace("comment_replace", comment_replace)
        contenido_temp = contenido_temp.replace("id_replace", id_replace)
        contenido_temp = contenido_temp.replace("name_replace", name_replace)
        contenido_temp = contenido_temp.replace("message_replace", message_replace)

        # Entradas con casos diferentes
        token_replace_in = matriz_reemplazos[0][index]
        if '-' in token_replace_in:
            token_replace= '<token regexp="yes">'+token_replace_in.replace('-', '|')+'</token>'
        else: 
            token_replace=''
            for x in token_replace_in.split():
                token_replace+='<token>'+x+'</token>'+'\n'+'  '
            token_replace = token_replace[:-3]

        suggestion_replace_in = matriz_reemplazos[1][index]
        if '-' in suggestion_replace_in:
            suggestion_replace=''
            for x in suggestion_replace_in.replace('-', ' ').split():
                suggestion_replace+='<suggestion>'+x+'</suggestion>'+'\n'+' '
            suggestion_replace = suggestion_replace[:-3]
        else: 
            suggestion_replace = '<suggestion>'+suggestion_replace_in+'</suggestion>'

        # Reemplazos para entradas con casos diferentes
        contenido_temp = contenido_temp.replace("<token>token_replace</token>", token_replace)
        contenido_temp = contenido_temp.replace("<suggestion>suggestion_replace</suggestion>", suggestion_replace)

        # Salida que concatena las salidas para cada registro
        salida+=contenido_temp+'\n\n'

    text_file = open(path_output, "w")
    text_file.write(salida)
    text_file.close()
    return