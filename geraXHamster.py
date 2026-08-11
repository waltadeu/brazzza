#! /usr/bin/python
# -*- coding: iso-8859-15 -*-

import requests
from bs4 import BeautifulSoup

#HETERO
def categoriasHeteroXhamster():
    #PASSA URL DE BUSCA - CATEGORIA
    listaDeCategorias = []
    url = "https://pt.xhamster.com/"
    response = requests.get(url)
    data = response.text

    soup = BeautifulSoup(data, 'lxml')
    ### INÍCIO CATEGORIAS ###
    pegaCategorias = soup.find_all('div', {"class": "all-categories"})
    for categoria in pegaCategorias:
        pegaCategoriasTagA = categoria.find_all('a')
        for tagA in pegaCategoriasTagA:
            pegahref = tagA.get('href')
            if "categories/" in pegahref:
                categoria = {}
                categoria['nomeOriginal'] = pegahref.split('/')[-1]
                nomeCategoria = tagA.get_text().strip().upper()
                if (pegahref.split('/')[-1] == 'casting'):
                    nomeCategoria = 'CASTIGO'
                elif (pegahref.split('/')[-1] == 'tight-pussy'):
                    nomeCategoria = 'BUCETA APERTADA'
                elif (pegahref.split('/')[-1] == 'creampie'):
                    nomeCategoria = 'EJACULAÇÃO NA VAGINA'
                elif (pegahref.split('/')[-1] == 'dildo'):
                    nomeCategoria = 'VIBRADOR'
                elif (pegahref.split('/')[-1] == 'femdom'):
                    nomeCategoria = 'DOMINAÇÃO'
                elif (pegahref.split('/')[-1] == 'futanari'):
                    nomeCategoria = 'HERMAFRODITA'
                elif (pegahref.split('/')[-1] == 'eating-pussy'):
                    nomeCategoria = 'LAMBER BUCETA'
                elif (pegahref.split('/')[-1] == 'pawg'):
                    nomeCategoria = 'BUNDA GRANDE'
                elif (pegahref.split('/')[-1] == 'hairy'):
                    nomeCategoria = 'PELUDAS'
                elif (pegahref.split('/')[-1] == 'big-cock'):
                    nomeCategoria = 'PICA GRANDE'
                elif (pegahref.split('/')[-1] == 'old-young'):
                    nomeCategoria = 'VELHOS E JOVENS'
                categoria['nomeCategoria'] = nomeCategoria
                listaDeCategorias.append(categoria)

    return listaDeCategorias
    ### FINALIZA CATEGORIAS ###

def videosTudaoHeteroXhamster(listaDeCategoriasXhamster):
    i = 1
    j = 0
    listaGeralFinal = {'videos': []}

    for row in range(10000):
        if(i == 31):
            i = 1
            j += 1
        print(listaDeCategoriasXhamster[j].get('nomeOriginal'))
        # PASSA URL DE BUSCA - CATEGORIA
        if(i == 1):
            url = "https://pt.xhamster.com/categories/" + listaDeCategoriasXhamster[j].get('nomeOriginal')
        else:
            url = "https://pt.xhamster.com/categories/" + listaDeCategoriasXhamster[j].get('nomeOriginal')+"/"+str(i)
        response = ''
        for retries in range(10000):
            try:
                response = requests.get(url)
                break
            except:
                print('tentou conexão')
                continue
        else:
            print("não foi possível conectar")
        #response = requests.get(url)
        data = response.text
        soup = BeautifulSoup(data, 'lxml')

        for range2 in range(10000):
            try:
                imagemVideo = soup.find_all('img', {"class": "thumb-image-container__image"})[range2]
            except:
                break
            nomeVideo = soup.find_all('a', {"class": "video-thumb-info__name"})[range2]
            duracaoVideo = soup.find_all('div', {"class": "thumb-image-container__duration"})[range2]
            itemLink = {}
            itemLink['categoria'] = listaDeCategoriasXhamster[j].get('nomeOriginal')
            nomeCategoria = listaDeCategoriasXhamster[j].get('nomeCategoria')
            if (listaDeCategoriasXhamster[j].get('nomeOriginal') == 'casting'):
                nomeCategoria = 'CASTIGO'
            elif (listaDeCategoriasXhamster[j].get('nomeOriginal') == 'tight-pussy'):
                nomeCategoria = 'BUCETA APERTADA'
            elif (listaDeCategoriasXhamster[j].get('nomeOriginal') == 'creampie'):
                nomeCategoria = 'EJACULAÇÃO NA VAGINA'
            elif (listaDeCategoriasXhamster[j].get('nomeOriginal') == 'dildo'):
                nomeCategoria = 'VIBRADOR'
            elif (listaDeCategoriasXhamster[j].get('nomeOriginal') == 'femdom'):
                nomeCategoria = 'DOMINAÇÃO'
            elif (listaDeCategoriasXhamster[j].get('nomeOriginal') == 'futanari'):
                nomeCategoria = 'HERMAFRODITA'
            elif (listaDeCategoriasXhamster[j].get('nomeOriginal') == 'eating-pussy'):
                nomeCategoria = 'LAMBER BUCETA'
            elif (listaDeCategoriasXhamster[j].get('nomeOriginal') == 'pawg'):
                nomeCategoria = 'BUNDA GRANDE'
            elif (listaDeCategoriasXhamster[j].get('nomeOriginal') == 'hairy'):
                nomeCategoria = 'PELUDAS'
            elif (listaDeCategoriasXhamster[j].get('nomeOriginal') == 'big-cock'):
                nomeCategoria = 'PICA GRANDE'
            elif (listaDeCategoriasXhamster[j].get('nomeOriginal') == 'old-young'):
                nomeCategoria = 'VELHOS E JOVENS'
            itemLink['categoriabr'] = nomeCategoria
            itemLink['linkvideo'] = nomeVideo.get('href')
            itemLink['imagemVideo'] = imagemVideo.get('src')
            itemLink['nomeVideo'] = nomeVideo.get_text()
            itemLink['duracaoVideo'] = duracaoVideo.get_text()
            listaGeralFinal['videos'].append(itemLink)

        if (i == 30 and j == len(listaDeCategoriasXhamster) - 1):
            import json
            with open("static/json/hetero/tudao.json", "w", encoding='utf8') as writeJSON:
                json.dump(listaGeralFinal, writeJSON, ensure_ascii=False)
            break
        i += 1

def videosHomeHeteroXhamster(listaDeCategorias):
    j = 0
    listaDeVideos = {'videos': []}

    for row in range(10000):

        if(row >= 1):
            j += 1

        # PASSA URL DE BUSCA - CATEGORIA
        if(row == 0):
            url = "https://pt.xhamster.com/categories/" + listaDeCategorias[j].get('nomeOriginal')
        else:
            url = "https://pt.xhamster.com/categories/" + listaDeCategorias[j].get('nomeOriginal')+"/"+str(row+1)

        response = requests.get(url)
        data = response.text
        soup = BeautifulSoup(data, 'lxml')

        for range2 in range(4):
            try:
                imagemVideo = soup.find_all('img', {"class": "thumb-image-container__image"})[range2]
            except:
                break
            nomeVideo = soup.find_all('a', {"class": "video-thumb-info__name"})[range2]
            duracaoVideo = soup.find_all('div', {"class": "thumb-image-container__duration"})[range2]
            itemLink = {}
            itemLink['categoria'] = listaDeCategorias[j].get('nomeOriginal')
            nomeCategoria = listaDeCategorias[j].get('nomeCategoria')
            if (listaDeCategorias[j].get('nomeOriginal') == 'casting'):
                nomeCategoria = 'CASTIGO'
            elif (listaDeCategorias[j].get('nomeOriginal') == 'tight-pussy'):
                nomeCategoria = 'BUCETA APERTADA'
            elif (listaDeCategorias[j].get('nomeOriginal') == 'creampie'):
                nomeCategoria = 'EJACULAÇÃO NA VAGINA'
            elif (listaDeCategorias[j].get('nomeOriginal') == 'dildo'):
                nomeCategoria = 'VIBRADOR'
            elif (listaDeCategorias[j].get('nomeOriginal') == 'femdom'):
                nomeCategoria = 'DOMINAÇÃO'
            elif (listaDeCategorias[j].get('nomeOriginal') == 'futanari'):
                nomeCategoria = 'HERMAFRODITA'
            elif (listaDeCategorias[j].get('nomeOriginal') == 'eating-pussy'):
                nomeCategoria = 'LAMBER BUCETA'
            elif (listaDeCategorias[j].get('nomeOriginal') == 'pawg'):
                nomeCategoria = 'BUNDA GRANDE'
            elif (listaDeCategorias[j].get('nomeOriginal') == 'hairy'):
                nomeCategoria = 'PELUDAS'
            elif (listaDeCategorias[j].get('nomeOriginal') == 'big-cock'):
                nomeCategoria = 'PICA GRANDE'
            elif (listaDeCategorias[j].get('nomeOriginal') == 'old-young'):
                nomeCategoria = 'VELHOS E JOVENS'
            itemLink['categoriabr'] = nomeCategoria
            itemLink['linkvideo'] = nomeVideo.get('href')
            itemLink['imagemVideo'] = imagemVideo.get('src')
            itemLink['nomeVideo'] = nomeVideo.get_text()
            itemLink['duracaoVideo'] = duracaoVideo.get_text()
            listaDeVideos['videos'].append(itemLink)

        if (j == len(listaDeCategorias) -1):
            import json
            with open("static/json/hetero/tudaoHome.json", "w", encoding='utf8') as writeJSON:
                    json.dump(listaDeVideos, writeJSON, ensure_ascii=False)
            break

def videosPorCategoriaHeteroXhamster(listaDeCategoriasXhamster):
    i = 1
    j = 0
    listaDeVideos = {listaDeCategoriasXhamster[j].get('nomeOriginal'): []}

    for row in range(10000):
        if(i == 31):
            i = 1
            j += 1
            listaDeVideos = {listaDeCategoriasXhamster[j].get('nomeOriginal'): []}
        print(listaDeCategoriasXhamster[j].get('nomeOriginal'))
        if(i == 1):
            url = "https://pt.xhamster.com/categories/" + listaDeCategoriasXhamster[j].get('nomeOriginal')
        else:
            url = "https://pt.xhamster.com/categories/" + listaDeCategoriasXhamster[j].get('nomeOriginal')+"/"+str(i)
        response = ''
        for retries in range(10000):
            try:
                response = requests.get(url)
                break
            except:
                print('tentou conexão')
                continue
        else:
            print("não foi possível conectar")
        #response = requests.get(url)
        data = response.text
        soup = BeautifulSoup(data, 'lxml')

        pegaInformacoesVideos = soup.find_all('div', {"class": "thumb-list__item"})
        for infoVideo in pegaInformacoesVideos:
            nomeVideo = infoVideo.find_all('a', {"class": "video-thumb-info__name"})
            imagemVideo = infoVideo.find_all('img', {"class": "thumb-image-container__image"})
            if(len(nomeVideo) == 1 and len(imagemVideo) == 1):
                duracaoVideo = infoVideo.find_all('div', {"class": "thumb-image-container__duration"})
                itemLink = {}
                nomeCategoria = listaDeCategoriasXhamster[j].get('nomeCategoria')
                if(listaDeCategoriasXhamster[j].get('nomeOriginal') == 'casting'):
                    nomeCategoria = 'CASTIGO'
                elif(listaDeCategoriasXhamster[j].get('nomeOriginal') == 'tight-pussy'):
                    nomeCategoria = 'BUCETA APERTADA'
                elif(listaDeCategoriasXhamster[j].get('nomeOriginal') == 'creampie'):
                    nomeCategoria = 'EJACULAÇÃO NA VAGINA'
                elif(listaDeCategoriasXhamster[j].get('nomeOriginal') == 'dildo'):
                    nomeCategoria = 'VIBRADOR'
                elif(listaDeCategoriasXhamster[j].get('nomeOriginal') == 'femdom'):
                    nomeCategoria = 'DOMINAÇÃO'
                elif(listaDeCategoriasXhamster[j].get('nomeOriginal') == 'futanari'):
                    nomeCategoria = 'HERMAFRODITA'
                elif(listaDeCategoriasXhamster[j].get('nomeOriginal') == 'eating-pussy'):
                    nomeCategoria = 'LAMBER BUCETA'
                elif(listaDeCategoriasXhamster[j].get('nomeOriginal') == 'pawg'):
                    nomeCategoria = 'BUNDA GRANDE'
                elif(listaDeCategoriasXhamster[j].get('nomeOriginal') == 'hairy'):
                    nomeCategoria = 'PELUDAS'
                elif(listaDeCategoriasXhamster[j].get('nomeOriginal') == 'big-cock'):
                    nomeCategoria = 'PICA GRANDE'
                elif(listaDeCategoriasXhamster[j].get('nomeOriginal') == 'old-young'):
                    nomeCategoria = 'VELHOS E JOVENS'
                itemLink['categoria'] = nomeCategoria
                itemLink['linkvideo'] = nomeVideo[0].get('href')
                itemLink['imagemVideo'] = imagemVideo[0].get('src')
                itemLink['nomeVideo'] = nomeVideo[0].get_text()
                itemLink['duracaoVideo'] = duracaoVideo[0].get_text()
                listaDeVideos[listaDeCategoriasXhamster[j].get('nomeOriginal')].append(itemLink)
            else:
                continue

        if(i == 30):
            print('entrou aqui')
            import json
            with open("static/json/hetero/" + listaDeCategoriasXhamster[j].get('nomeOriginal') + ".json", "w",encoding='utf8') as writeJSON:
                json.dump(listaDeVideos, writeJSON, ensure_ascii=False)
            if(j == len(listaDeCategoriasXhamster) - 1):
                break

        i += 1

########################################################################################################################

#GAY
def categoriasGayXhamster():
    #PASSA URL DE BUSCA - CATEGORIA
    listaDeCategorias = []
    url = "https://pt.xhamster.com/gay/"
    response = requests.get(url)
    data = response.text

    soup = BeautifulSoup(data, 'lxml')
    ### INÍCIO CATEGORIAS ###
    pegaCategorias = soup.find_all('div', {"class": "all-categories"})
    for categoria in pegaCategorias:
        pegaCategoriasTagA = categoria.find_all('a')
        for tagA in pegaCategoriasTagA:
            pegahref = tagA.get('href')
            if "categories/" in pegahref:
                categoria = {}
                categoria['nomeOriginal'] = pegahref.split('/')[-1]
                nomeCategoria = tagA.get_text().strip().upper()
                if (pegahref.split('/')[-1] == 'asian'):
                    nomeCategoria = 'ASIÁTICOS'
                elif (pegahref.split('/')[-1] == 'hunk'):
                    nomeCategoria = 'HOMEM FORTE'
                elif (pegahref.split('/')[-1] == 'bukkake'):
                    nomeCategoria = 'EJACULAÇÃO EM GRUPO'
                elif (pegahref.split('/')[-1] == 'gaping'):
                    nomeCategoria = 'OBJETOS'
                elif (pegahref.split('/')[-1] == 'glory-hole'):
                    nomeCategoria = 'BURACO PERFEITO'
                elif (pegahref.split('/')[-1] == 'black'):
                    nomeCategoria = 'NEGROS'
                elif (pegahref.split('/')[-1] == 'outdoor'):
                    nomeCategoria = 'AO AR LIVRE'
                elif (pegahref.split('/')[-1] == 'daddy'):
                    nomeCategoria = 'PAPAI'
                elif (pegahref.split('/')[-1] == 'small-cock'):
                    nomeCategoria = 'PICA PEQUENA'
                elif (pegahref.split('/')[-1] == 'big-cock'):
                    nomeCategoria = 'PICA GRANDE'
                elif (pegahref.split('/')[-1] == 'twink'):
                    nomeCategoria = 'SEM PÊLOS'
                elif (pegahref.split('/')[-1] == 'bear'):
                    nomeCategoria = 'URSOS'
                elif (pegahref.split('/')[-1] == 'old-young'):
                    nomeCategoria = 'VELHOS E JOVENS'
                categoria['nomeCategoria'] = nomeCategoria
                listaDeCategorias.append(categoria)

    return listaDeCategorias
    ### FINALIZA CATEGORIAS ###

def videosTudaoGayXhamster(listaDeCategoriasXhamster):
    i = 1
    j = 0
    listaGeralFinal = {'videos': []}

    for row in range(10000):
        if(i == 31):
            i = 1
            j += 1
        print(listaDeCategoriasXhamster[j].get('nomeOriginal'))
        # PASSA URL DE BUSCA - CATEGORIA
        if(i == 1):
            url = "https://pt.xhamster.com/gay/categories/" + listaDeCategoriasXhamster[j].get('nomeOriginal')
        else:
            url = "https://pt.xhamster.com/gay/categories/" + listaDeCategoriasXhamster[j].get('nomeOriginal')+"/"+str(i)
        response = ''
        for retries in range(10000):
            try:
                response = requests.get(url)
                break
            except:
                print('tentou conexão')
                continue
        else:
            print("não foi possível conectar")
        #response = requests.get(url)
        data = response.text
        soup = BeautifulSoup(data, 'lxml')

        for range2 in range(10000):
            try:
                imagemVideo = soup.find_all('img', {"class": "thumb-image-container__image"})[range2]
            except:
                break
            nomeVideo = soup.find_all('a', {"class": "video-thumb-info__name"})[range2]
            duracaoVideo = soup.find_all('div', {"class": "thumb-image-container__duration"})[range2]
            itemLink = {}
            itemLink['categoria'] = listaDeCategoriasXhamster[j].get('nomeOriginal')
            nomeCategoria = listaDeCategoriasXhamster[j].get('nomeCategoria')
            if (listaDeCategoriasXhamster[j].get('nomeOriginal') == 'casting'):
                nomeCategoria = 'CASTIGO'
            elif (listaDeCategoriasXhamster[j].get('nomeOriginal') == 'tight-pussy'):
                nomeCategoria = 'BUCETA APERTADA'
            elif (listaDeCategoriasXhamster[j].get('nomeOriginal') == 'creampie'):
                nomeCategoria = 'EJACULAÇÃO NA VAGINA'
            elif (listaDeCategoriasXhamster[j].get('nomeOriginal') == 'dildo'):
                nomeCategoria = 'VIBRADOR'
            elif (listaDeCategoriasXhamster[j].get('nomeOriginal') == 'femdom'):
                nomeCategoria = 'DOMINAÇÃO'
            elif (listaDeCategoriasXhamster[j].get('nomeOriginal') == 'futanari'):
                nomeCategoria = 'HERMAFRODITA'
            elif (listaDeCategoriasXhamster[j].get('nomeOriginal') == 'eating-pussy'):
                nomeCategoria = 'LAMBER BUCETA'
            elif (listaDeCategoriasXhamster[j].get('nomeOriginal') == 'pawg'):
                nomeCategoria = 'BUNDA GRANDE'
            elif (listaDeCategoriasXhamster[j].get('nomeOriginal') == 'hairy'):
                nomeCategoria = 'PELUDAS'
            elif (listaDeCategoriasXhamster[j].get('nomeOriginal') == 'big-cock'):
                nomeCategoria = 'PICA GRANDE'
            elif (listaDeCategoriasXhamster[j].get('nomeOriginal') == 'old-young'):
                nomeCategoria = 'VELHOS E JOVENS'
            itemLink['categoriabr'] = nomeCategoria
            itemLink['linkvideo'] = nomeVideo.get('href')
            itemLink['imagemVideo'] = imagemVideo.get('src')
            itemLink['nomeVideo'] = nomeVideo.get_text()
            itemLink['duracaoVideo'] = duracaoVideo.get_text()
            listaGeralFinal['videos'].append(itemLink)

        if (i == 30 and j == len(listaDeCategoriasXhamster) - 1):
            import json
            with open("static/json/gay/tudao.json", "w", encoding='utf8') as writeJSON:
                json.dump(listaGeralFinal, writeJSON, ensure_ascii=False)
            break
        i += 1

def videosHomeGayXhamster(listaDeCategorias):
    j = 0
    listaDeVideos = {'videos': []}

    for row in range(10000):
        if(row >= 1):
            j += 1
        # PASSA URL DE BUSCA - CATEGORIA
        if(row == 0):
            url = "https://pt.xhamster.com/gay/categories/" + listaDeCategorias[j].get('nomeOriginal')
        else:
            url = "https://pt.xhamster.com/gay/categories/" + listaDeCategorias[j].get('nomeOriginal')+"/"+str(row+1)

        response = requests.get(url)
        data = response.text
        soup = BeautifulSoup(data, 'lxml')

        for range2 in range(4):
            try:
                imagemVideo = soup.find_all('img', {"class": "thumb-image-container__image"})[range2]
            except:
                break
            nomeVideo = soup.find_all('a', {"class": "video-thumb-info__name"})[range2]
            duracaoVideo = soup.find_all('div', {"class": "thumb-image-container__duration"})[range2]
            itemLink = {}
            itemLink['categoria'] = listaDeCategorias[j].get('nomeOriginal')
            nomeCategoria = listaDeCategorias[j].get('nomeCategoria')
            if (listaDeCategorias[j].get('nomeOriginal') == 'casting'):
                nomeCategoria = 'CASTIGO'
            elif (listaDeCategorias[j].get('nomeOriginal') == 'tight-pussy'):
                nomeCategoria = 'BUCETA APERTADA'
            elif (listaDeCategorias[j].get('nomeOriginal') == 'creampie'):
                nomeCategoria = 'EJACULAÇÃO NA VAGINA'
            elif (listaDeCategorias[j].get('nomeOriginal') == 'dildo'):
                nomeCategoria = 'VIBRADOR'
            elif (listaDeCategorias[j].get('nomeOriginal') == 'femdom'):
                nomeCategoria = 'DOMINAÇÃO'
            elif (listaDeCategorias[j].get('nomeOriginal') == 'futanari'):
                nomeCategoria = 'HERMAFRODITA'
            elif (listaDeCategorias[j].get('nomeOriginal') == 'eating-pussy'):
                nomeCategoria = 'LAMBER BUCETA'
            elif (listaDeCategorias[j].get('nomeOriginal') == 'pawg'):
                nomeCategoria = 'BUNDA GRANDE'
            elif (listaDeCategorias[j].get('nomeOriginal') == 'hairy'):
                nomeCategoria = 'PELUDAS'
            elif (listaDeCategorias[j].get('nomeOriginal') == 'big-cock'):
                nomeCategoria = 'PICA GRANDE'
            elif (listaDeCategorias[j].get('nomeOriginal') == 'old-young'):
                nomeCategoria = 'VELHOS E JOVENS'
            itemLink['categoriabr'] = nomeCategoria
            itemLink['linkvideo'] = nomeVideo.get('href')
            itemLink['imagemVideo'] = imagemVideo.get('src')
            itemLink['nomeVideo'] = nomeVideo.get_text()
            itemLink['duracaoVideo'] = duracaoVideo.get_text()
            listaDeVideos['videos'].append(itemLink)

        if (j == len(listaDeCategorias) -1):
            import json
            with open("static/json/gay/tudaoHome.json", "w", encoding='utf8') as writeJSON:
                    json.dump(listaDeVideos, writeJSON, ensure_ascii=False)
            break

def videosPorCategoriaGayXhamster(listaDeCategoriasXhamster):
    i = 1
    j = 0
    listaDeVideos = {listaDeCategoriasXhamster[j].get('nomeOriginal'): []}

    for row in range(10000):
        if(i == 31):
            i = 1
            j += 1
            listaDeVideos = {listaDeCategoriasXhamster[j].get('nomeOriginal'): []}
        print(listaDeCategoriasXhamster[j].get('nomeOriginal'))
        if(i == 1):
            url = "https://pt.xhamster.com/gay/categories/" + listaDeCategoriasXhamster[j].get('nomeOriginal')
        else:
            url = "https://pt.xhamster.com/gay/categories/" + listaDeCategoriasXhamster[j].get('nomeOriginal')+"/"+str(i)
        response = ''
        for retries in range(10000):
            try:
                response = requests.get(url)
                break
            except:
                print('tentou conexão')
                continue
        else:
            print("não foi possível conectar")
        #response = requests.get(url)
        data = response.text
        soup = BeautifulSoup(data, 'lxml')

        pegaInformacoesVideos = soup.find_all('div', {"class": "thumb-list__item"})
        for infoVideo in pegaInformacoesVideos:
            nomeVideo = infoVideo.find_all('a', {"class": "video-thumb-info__name"})
            imagemVideo = infoVideo.find_all('img', {"class": "thumb-image-container__image"})
            if(len(nomeVideo) == 1 and len(imagemVideo) == 1):
                duracaoVideo = infoVideo.find_all('div', {"class": "thumb-image-container__duration"})
                itemLink = {}
                nomeCategoria = listaDeCategoriasXhamster[j].get('nomeCategoria')
                if(listaDeCategoriasXhamster[j].get('nomeOriginal') == 'casting'):
                    nomeCategoria = 'CASTIGO'
                elif(listaDeCategoriasXhamster[j].get('nomeOriginal') == 'tight-pussy'):
                    nomeCategoria = 'BUCETA APERTADA'
                elif(listaDeCategoriasXhamster[j].get('nomeOriginal') == 'creampie'):
                    nomeCategoria = 'EJACULAÇÃO NA VAGINA'
                elif(listaDeCategoriasXhamster[j].get('nomeOriginal') == 'dildo'):
                    nomeCategoria = 'VIBRADOR'
                elif(listaDeCategoriasXhamster[j].get('nomeOriginal') == 'femdom'):
                    nomeCategoria = 'DOMINAÇÃO'
                elif(listaDeCategoriasXhamster[j].get('nomeOriginal') == 'futanari'):
                    nomeCategoria = 'HERMAFRODITA'
                elif(listaDeCategoriasXhamster[j].get('nomeOriginal') == 'eating-pussy'):
                    nomeCategoria = 'LAMBER BUCETA'
                elif(listaDeCategoriasXhamster[j].get('nomeOriginal') == 'pawg'):
                    nomeCategoria = 'BUNDA GRANDE'
                elif(listaDeCategoriasXhamster[j].get('nomeOriginal') == 'hairy'):
                    nomeCategoria = 'PELUDAS'
                elif(listaDeCategoriasXhamster[j].get('nomeOriginal') == 'big-cock'):
                    nomeCategoria = 'PICA GRANDE'
                elif(listaDeCategoriasXhamster[j].get('nomeOriginal') == 'old-young'):
                    nomeCategoria = 'VELHOS E JOVENS'
                itemLink['categoria'] = nomeCategoria
                itemLink['linkvideo'] = nomeVideo[0].get('href')
                itemLink['imagemVideo'] = imagemVideo[0].get('src')
                itemLink['nomeVideo'] = nomeVideo[0].get_text()
                itemLink['duracaoVideo'] = duracaoVideo[0].get_text()
                listaDeVideos[listaDeCategoriasXhamster[j].get('nomeOriginal')].append(itemLink)
            else:
                continue
        if(i == 30):
            import json
            with open("static/json/gay/" + listaDeCategoriasXhamster[j].get('nomeOriginal') + ".json", "w",encoding='utf8') as writeJSON:
                json.dump(listaDeVideos, writeJSON, ensure_ascii=False)
            if (j == len(listaDeCategoriasXhamster) - 1):
                break

        i += 1