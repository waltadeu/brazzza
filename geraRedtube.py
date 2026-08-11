#! /usr/bin/python
# -*- coding: iso-8859-15 -*-

from operator import itemgetter
import requests
from bs4 import BeautifulSoup

#HETERO
def videosTudaoHeteroRedtube(listaDeCategoriasXhamster):
    i = 1
    j = 0
    import json
    with open("static/json/hetero/tudao.json", "r", encoding="utf8") as read_file:
        listaGeralFinal = json.load(read_file)

    for row in range(10000):
        if(i == 31):
            i = 1
            j += 1
        if(i == 1):
            url = "https://www.redtube.com.br/?search=" + listaDeCategoriasXhamster[j].get('nomeOriginal')
        else:
            url = "https://www.redtube.com.br/?search=" + listaDeCategoriasXhamster[j].get('nomeOriginal')+"&page="+str(i)
        print(listaDeCategoriasXhamster[j].get('nomeOriginal'))
        #response = requests.get(url)
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
        data = response.text
        soup = BeautifulSoup(data, 'lxml')

        voltaVideo = 0
        for range2 in range(10000):
            try:
                imagemVideo = soup.find_all('img', {"class": "img_video_list"})[range2].get('data-o_thumb')
                if(imagemVideo == None):
                    voltaVideo += 1
                    continue
            except:
                break
            nomeVideo = soup.find_all('a', {"class": "tm_video_title"})[range2].get_text().strip().upper()
            duracaoVideo = soup.find_all('span', {"class": "duration"})[range2-voltaVideo].get_text().strip()
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
            linkVideo = soup.find_all('a', {"class": "video_link"})[range2-voltaVideo].get('href')
            if("/premium" in linkVideo):
                continue
            itemLink['linkvideo'] = 'https://www.redtube.com.br' + linkVideo
            itemLink['imagemVideo'] = imagemVideo
            itemLink['nomeVideo'] = nomeVideo
            itemLink['duracaoVideo'] = duracaoVideo
            listaGeralFinal['videos'].append(itemLink)

        if(i == 30 and j == len(listaDeCategoriasXhamster) - 1):
            sorted_list = listaGeralFinal.get('videos')
            sorted_list.sort(key=itemgetter("nomeVideo"))
            listaGeralFinal = {'videos': sorted_list}

            import json
            with open("static/json/hetero/tudao.json", "w", encoding='utf8') as writeJSON:
                json.dump(listaGeralFinal, writeJSON, ensure_ascii=False)
            break
        i += 1

def videosPorCategoriaHeteroRedtube(listaDeCategoriasXhamster):
    i = 1
    j = 0
    import json
    with open("static/json/hetero/" + listaDeCategoriasXhamster[j].get('nomeOriginal') + ".json", "r",
              encoding="utf8") as read_file:
        listaVideosRedtube = json.load(read_file)

    for row in range(10000):
        if(i == 31):
            i = 1
            j += 1
            with open("static/json/hetero/" + listaDeCategoriasXhamster[j].get('nomeOriginal') + ".json", "r",
                      encoding="utf8") as read_file:
                listaVideosRedtube = json.load(read_file)
        print(listaDeCategoriasXhamster[j].get('nomeOriginal'))
        # PASSA URL DE BUSCA - CATEGORIA
        if(i == 0):
            url = "https://www.redtube.com.br/?search=" + listaDeCategoriasXhamster[j].get('nomeOriginal')
        else:
            url = "https://www.redtube.com.br/?search=" + listaDeCategoriasXhamster[j].get('nomeOriginal')+"&page="+str(i)
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

        voltaVideo = 0
        for range2 in range(10000):
            try:
                imagemVideo = soup.find_all('img', {"class": "img_video_list"})[range2].get('data-o_thumb')
                if(imagemVideo == None):
                    voltaVideo += 1
                    continue
            except:
                break
            nomeVideo = soup.find_all('a', {"class": "tm_video_title"})[range2].get_text().strip().upper()
            duracaoVideo = soup.find_all('span', {"class": "duration"})[range2-voltaVideo].get_text().strip()
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
            linkVideo = soup.find_all('a', {"class": "video_link"})[range2-voltaVideo].get('href')
            if("/premium" in linkVideo):
                continue
            itemLink['linkvideo'] = 'https://www.redtube.com.br' + linkVideo
            itemLink['imagemVideo'] = imagemVideo
            itemLink['nomeVideo'] = nomeVideo
            itemLink['duracaoVideo'] = duracaoVideo
            listaVideosRedtube[listaDeCategoriasXhamster[j].get('nomeOriginal')].append(itemLink)

        if (i == 30):
            sorted_list = listaVideosRedtube.get(listaDeCategoriasXhamster[j].get('nomeOriginal'))
            sorted_list.sort(key=itemgetter("nomeVideo"))
            listaVideosRedtube = {listaDeCategoriasXhamster[j].get('nomeOriginal'): sorted_list}

            import json
            with open("static/json/hetero/" + listaDeCategoriasXhamster[j].get('nomeOriginal') + ".json", "w", encoding='utf8') as writeJSON:
                json.dump(listaVideosRedtube, writeJSON, ensure_ascii=False)
            if(j == len(listaDeCategoriasXhamster) - 1):
                break
        i += 1

#######################################################################################################################

#GAY
def videosTudaoGayRedtube(listaDeCategoriasXhamster):
    i = 1
    j = 0
    import json
    with open("static/json/gay/tudao.json", "r", encoding="utf8") as read_file:
        listaGeralFinal = json.load(read_file)

    for row in range(10000):
        if(i == 31):
            i = 1
            j += 1
        if(i == 1):
            url = "https://www.redtube.com.br/gay?search=" + listaDeCategoriasXhamster[j].get('nomeOriginal')
        else:
            url = "https://www.redtube.com.br/gay?search=" + listaDeCategoriasXhamster[j].get('nomeOriginal')+"&page="+str(i)
        print(listaDeCategoriasXhamster[j].get('nomeOriginal'))
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

        voltaVideo = 0
        for range2 in range(10000):
            try:
                imagemVideo = soup.find_all('img', {"class": "img_video_list"})[range2].get('data-o_thumb')
                if(imagemVideo == None):
                    voltaVideo += 1
                    continue
            except:
                break
            nomeVideo = soup.find_all('a', {"class": "tm_video_title"})[range2].get_text().strip().upper()
            duracaoVideo = soup.find_all('span', {"class": "duration"})[range2-voltaVideo].get_text().strip()
            itemLink = {}
            itemLink['categoria'] = listaDeCategoriasXhamster[j].get('nomeOriginal')
            nomeCategoria = listaDeCategoriasXhamster[j].get('nomeCategoria')
            if (listaDeCategoriasXhamster[j].get('nomeOriginal') == 'asian'):
                nomeCategoria = 'ASIÁTICOS'
            elif (listaDeCategoriasXhamster[j].get('nomeOriginal') == 'hunk'):
                nomeCategoria = 'HOMEM FORTE'
            elif (listaDeCategoriasXhamster[j].get('nomeOriginal') == 'bukkake'):
                nomeCategoria = 'EJACULAÇÃO EM GRUPO'
            elif (listaDeCategoriasXhamster[j].get('nomeOriginal') == 'gaping'):
                nomeCategoria = 'OBJETOS'
            elif (listaDeCategoriasXhamster[j].get('nomeOriginal') == 'glory-hole'):
                nomeCategoria = 'BURACO PERFEITO'
            elif (listaDeCategoriasXhamster[j].get('nomeOriginal') == 'black'):
                nomeCategoria = 'NEGROS'
            elif (listaDeCategoriasXhamster[j].get('nomeOriginal') == 'outdoor'):
                nomeCategoria = 'AO AR LIVRE'
            elif (listaDeCategoriasXhamster[j].get('nomeOriginal') == 'daddy'):
                nomeCategoria = 'PAPAI'
            elif (listaDeCategoriasXhamster[j].get('nomeOriginal') == 'small-cock'):
                nomeCategoria = 'PICA PEQUENA'
            elif (listaDeCategoriasXhamster[j].get('nomeOriginal') == 'big-cock'):
                nomeCategoria = 'PICA GRANDE'
            elif (listaDeCategoriasXhamster[j].get('nomeOriginal') == 'twink'):
                nomeCategoria = 'SEM PÊLOS'
            elif (listaDeCategoriasXhamster[j].get('nomeOriginal') == 'bear'):
                nomeCategoria = 'URSOS'
            elif (listaDeCategoriasXhamster[j].get('nomeOriginal') == 'old-young'):
                nomeCategoria = 'VELHOS E JOVENS'
            itemLink['categoriabr'] = nomeCategoria
            linkVideo = soup.find_all('a', {"class": "video_link"})[range2-voltaVideo].get('href')
            if("/premium" in linkVideo):
                continue
            itemLink['linkvideo'] = 'https://www.redtube.com.br' + linkVideo
            itemLink['imagemVideo'] = imagemVideo
            itemLink['nomeVideo'] = nomeVideo
            itemLink['duracaoVideo'] = duracaoVideo
            listaGeralFinal['videos'].append(itemLink)

        if(i == 30 and j == len(listaDeCategoriasXhamster) - 1):
            sorted_list = listaGeralFinal.get('videos')
            sorted_list.sort(key=itemgetter("nomeVideo"))
            listaGeralFinal = {'videos': sorted_list}

            import json
            with open("static/json/gay/tudao.json", "w", encoding='utf8') as writeJSON:
                json.dump(listaGeralFinal, writeJSON, ensure_ascii=False)
            break
        i += 1

def videosPorCategoriaGayRedtube(listaDeCategoriasXhamster):
    i = 1
    j = 0
    import json
    with open("static/json/gay/" + listaDeCategoriasXhamster[j].get('nomeOriginal') + ".json", "r",
              encoding="utf8") as read_file:
        listaVideosRedtube = json.load(read_file)

    for row in range(10000):
        if(i == 31):
            i = 1
            j += 1
            with open("static/json/gay/" + listaDeCategoriasXhamster[j].get('nomeOriginal') + ".json", "r", encoding="utf8") as read_file:
                listaVideosRedtube = json.load(read_file)
        print(listaDeCategoriasXhamster[j].get('nomeOriginal'))
        # PASSA URL DE BUSCA - CATEGORIA
        if(i == 0):
            url = "https://www.redtube.com.br/gay?search=" + listaDeCategoriasXhamster[j].get('nomeOriginal')
        else:
            url = "https://www.redtube.com.br/gay?search=" + listaDeCategoriasXhamster[j].get('nomeOriginal')+"&page="+str(i)
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

        voltaVideo = 0
        for range2 in range(10000):
            try:
                imagemVideo = soup.find_all('img', {"class": "img_video_list"})[range2].get('data-o_thumb')
                if(imagemVideo == None):
                    voltaVideo += 1
                    continue
            except:
                break
            nomeVideo = soup.find_all('a', {"class": "tm_video_title"})[range2].get_text().strip().upper()
            duracaoVideo = soup.find_all('span', {"class": "duration"})[range2-voltaVideo].get_text().strip()
            itemLink = {}
            itemLink['categoria'] = listaDeCategoriasXhamster[j].get('nomeOriginal')
            nomeCategoria = listaDeCategoriasXhamster[j].get('nomeCategoria')
            if (listaDeCategoriasXhamster[j].get('nomeOriginal') == 'asian'):
                nomeCategoria = 'ASIÁTICOS'
            elif (listaDeCategoriasXhamster[j].get('nomeOriginal') == 'hunk'):
                nomeCategoria = 'HOMEM FORTE'
            elif (listaDeCategoriasXhamster[j].get('nomeOriginal') == 'bukkake'):
                nomeCategoria = 'EJACULAÇÃO EM GRUPO'
            elif (listaDeCategoriasXhamster[j].get('nomeOriginal') == 'gaping'):
                nomeCategoria = 'OBJETOS'
            elif (listaDeCategoriasXhamster[j].get('nomeOriginal') == 'glory-hole'):
                nomeCategoria = 'BURACO PERFEITO'
            elif (listaDeCategoriasXhamster[j].get('nomeOriginal') == 'black'):
                nomeCategoria = 'NEGROS'
            elif (listaDeCategoriasXhamster[j].get('nomeOriginal') == 'outdoor'):
                nomeCategoria = 'AO AR LIVRE'
            elif (listaDeCategoriasXhamster[j].get('nomeOriginal') == 'daddy'):
                nomeCategoria = 'PAPAI'
            elif (listaDeCategoriasXhamster[j].get('nomeOriginal') == 'small-cock'):
                nomeCategoria = 'PICA PEQUENA'
            elif (listaDeCategoriasXhamster[j].get('nomeOriginal') == 'big-cock'):
                nomeCategoria = 'PICA GRANDE'
            elif (listaDeCategoriasXhamster[j].get('nomeOriginal') == 'twink'):
                nomeCategoria = 'SEM PÊLOS'
            elif (listaDeCategoriasXhamster[j].get('nomeOriginal') == 'bear'):
                nomeCategoria = 'URSOS'
            elif (listaDeCategoriasXhamster[j].get('nomeOriginal') == 'old-young'):
                nomeCategoria = 'VELHOS E JOVENS'
            itemLink['categoriabr'] = nomeCategoria
            linkVideo = soup.find_all('a', {"class": "video_link"})[range2-voltaVideo].get('href')
            if("/premium" in linkVideo):
                continue
            itemLink['linkvideo'] = 'https://www.redtube.com.br' + linkVideo
            itemLink['imagemVideo'] = imagemVideo
            itemLink['nomeVideo'] = nomeVideo
            itemLink['duracaoVideo'] = duracaoVideo
            listaVideosRedtube[listaDeCategoriasXhamster[j].get('nomeOriginal')].append(itemLink)

        if (i == 30 ):
            sorted_list = listaVideosRedtube.get(listaDeCategoriasXhamster[j].get('nomeOriginal'))
            sorted_list.sort(key=itemgetter("nomeVideo"))
            listaVideosRedtube = {listaDeCategoriasXhamster[j].get('nomeOriginal'): sorted_list}

            import json
            with open("static/json/gay/" + listaDeCategoriasXhamster[j].get('nomeOriginal') + ".json", "w", encoding='utf8') as writeJSON:
                json.dump(listaVideosRedtube, writeJSON, ensure_ascii=False)
            if(j == len(listaDeCategoriasXhamster) - 1):
                break
        i += 1