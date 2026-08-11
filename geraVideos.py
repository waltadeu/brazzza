#! /usr/bin/python
# -*- coding: iso-8859-15 -*-

import geraRedtube
import geraXHamster


def geraVideosHeteroXhamster():

    #GERA CATEGORIAS
    listaDeCategoriasXhamster = geraXHamster.categoriasHeteroXhamster()
    import json
    with open("static/json/hetero/categorias.json", "w", encoding='utf8') as writeJSON:
        json.dump(listaDeCategoriasXhamster, writeJSON, ensure_ascii=False)

    #GERA CATEGORIAS
    import json
    with open("static/json/hetero/categorias.json", "r", encoding="utf8") as read_file:
        listaDeCategoriasXhamster = json.load(read_file)

    print('XHAMSTER - HETERO HOME')
    #GERA HOME HETERO
    geraXHamster.videosHomeHeteroXhamster(listaDeCategoriasXhamster)

    print('XHAMSTER - HETERO CATEGORIAS')
    #GERA VÍDEOS POR CATEGORIAS
    geraXHamster.videosPorCategoriaHeteroXhamster(listaDeCategoriasXhamster)

    #GERA VÍDEOS TUDÃO HETERO
    print('XHAMSTER - HETERO TUDAO')
    geraXHamster.videosTudaoHeteroXhamster(listaDeCategoriasXhamster)


def geraVideosHeteroRedtube():

    #GERA CATEGORIAS
    import json
    with open("static/json/hetero/categorias.json", "r", encoding="utf8") as read_file:
        listaDeCategoriasXhamster = json.load(read_file)

    print('REDTUBE - HETERO CATEGORIAS')
    #GERA VÍDEOS POR CATEGORIAS
    geraRedtube.videosPorCategoriaHeteroRedtube(listaDeCategoriasXhamster)

    #GERA VÍDEOS TUDÃO HETERO
    print('REDTUBE - HETERO TUDAO')
    geraRedtube.videosTudaoHeteroRedtube(listaDeCategoriasXhamster)

#GERA JSON HETERO
geraVideosHeteroXhamster()
geraVideosHeteroRedtube()
########################################################################################################################

def geraVideosGayXhamster():

    #GERA CATEGORIAS
    listaDeCategoriasXhamster = geraXHamster.categoriasGayXhamster()
    import json
    with open("static/json/gay/categorias.json", "w", encoding='utf8') as writeJSON:
        json.dump(listaDeCategoriasXhamster, writeJSON, ensure_ascii=False)

    #GERA CATEGORIAS
    import json
    with open("static/json/hetero/categorias.json", "r", encoding="utf8") as read_file:
        listaDeCategoriasXhamster = json.load(read_file)

    print('XHAMSTER - GAY HOME')
    #GERA HOME HETERO
    geraXHamster.videosHomeGayXhamster(listaDeCategoriasXhamster)

    print('XHAMSTER - GAY CATEGORIAS')
    #GERA VÍDEOS POR CATEGORIAS
    geraXHamster.videosPorCategoriaGayXhamster(listaDeCategoriasXhamster)

    #GERA VÍDEOS TUDÃO HETERO
    print('XHAMSTER - GAY TUDAO')
    geraXHamster.videosTudaoGayXhamster(listaDeCategoriasXhamster)


def geraVideosGayRedtube():

    #GERA CATEGORIAS
    import json
    with open("static/json/gay/categorias.json", "r", encoding="utf8") as read_file:
        listaDeCategoriasXhamster = json.load(read_file)

    print('REDTUBE - GAY CATEGORIAS')
    #GERA VÍDEOS POR CATEGORIAS
    geraRedtube.videosPorCategoriaGayRedtube(listaDeCategoriasXhamster)

    #GERA VÍDEOS TUDÃO HETERO
    print('REDTUBE - GAY TUDAO')
    geraRedtube.videosTudaoGayRedtube(listaDeCategoriasXhamster)

#GERA JSON GAY
geraVideosGayXhamster()
geraVideosGayRedtube()