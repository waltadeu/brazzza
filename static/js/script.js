//FIXED MENU MOBILE
window.onscroll = function () {
    fixedMenu();
};

//VARIAVEL INICIAL GENERO
var filtroGenero = localStorage.getItem("genero");
if(filtroGenero == null)
	filtroGenero = 'hetero';

//REQUEST PARA EXIBIR OS VÍDEOS APÓS REALIZAR BUSCA
var requestThumbsBusca = new XMLHttpRequest();
//VARIAVEL PARA GUARDAR O RETORNO DO JSON DE BUSCA
var dataBusca = {}
var entrounaBusca = false;

requestThumbsBusca.open("GET", "static/json/" + filtroGenero + "/tudao.json", true);

//REQUEST THUMBS
requestThumbsBusca.onload = function () {
    dataBusca = JSON.parse(this.response);
    if(entrounaBusca)
        metodoRealizaBusca(itensPagina[5], itensPagina[6]);

}
requestThumbsBusca.send();

var header = document.getElementById("main-menu");
var sticky = header.offsetTop;

function fixedMenu() {
    if (window.pageYOffset > sticky) {
        header.classList.add("sticky");
    } else {
        header.classList.remove("sticky");
    }
}

var logoLGBT = document.getElementById("link-logo-lgbt");
var inicioLGBT = document.getElementById("inicio-lgbt");
var logoDefault = document.getElementById("link-logo-default");
var inicioDefault = document.getElementById("inicio-default");

// LINK PÁGINA TERMO
var liLinkTermoContent = document.createElement("span");
    liLinkTermoContent.innerHTML =
    "<form action='termo' method='post'><input type='submit' name='add' value='Termos e condições'></form>";

var linkTermo = document.getElementById("linkTermo");
    linkTermo.appendChild(liLinkTermoContent);

// LINK PÁGINA FORMULARIO CONTATO
// var liLinkContatoFormContent = document.createElement("span");
//     liLinkContatoFormContent.innerHTML =
//     "<form action='formulario' method='post'><input type='submit' name='add' value='Formulário de Contato'></form>";

// var linkContatoForm = document.getElementById("linkContatoForm");
//     linkContatoForm.appendChild(liLinkContatoFormContent);


var pagina1 = window.location.href;

if (pagina1.match("gay")) {
    generoGay(false);
} else if (pagina1.match("hetero")) {
    generoHetero(false);
} else if (pagina1.match("termo")) {
    var logoDefault = document.getElementById("link-logo-default");
    var logoLGBT = document.getElementById("link-logo-lgbt");

    var inicioDefault = document.getElementById("inicio-default");
    var inicioLGBT = document.getElementById("inicio-lgbt");

    if (filtroGenero == "gay") {
        logoDefault.style.display = "none";
        logoLGBT.style.display = "block";

        inicioDefault.style.display = "none";
        inicioLGBT.style.display = "block";
    } else {
        logoDefault.style.display = "block";
        logoLGBT.style.display = "none";

        inicioDefault.style.display = "block";
        inicioLGBT.style.display = "none";
    }
}
else {
    window.location.href = "/?hetero/";
}

function generoGay(direciona) {
    localStorage.setItem("genero", "gay");

    logoLGBT.style.display = "block";
    inicioLGBT.style.display = "block";

    logoDefault.style.display = "none";
    inicioDefault.style.display = "none";

    document.getElementById("genero-gay").checked = true;
    document.getElementById("genero-hetero").checked = false;

    if (direciona) window.location.href = "/?gay/";
}

function generoHetero(direciona) {
    localStorage.setItem("genero", "hetero");

    logoLGBT.style.display = "none";
    inicioLGBT.style.display = "none";

    logoDefault.style.display = "block";
    inicioDefault.style.display = "block";

    document.getElementById("genero-gay").checked = false;
    document.getElementById("genero-hetero").checked = true;

    if (direciona) window.location.href = "/?hetero/";
}

var itensPagina = "";
showCategorias();

// EXIBE CATEGORIAS NO MENU
function showCategorias() {
    var pagina = window.location.href;
	itensPagina = pagina.split(/[&=/]/);
	//REQUEST PARA EXIBIR OS AS CATEGORIAS
	var requestCategorias = new XMLHttpRequest();
    requestCategorias.open("GET", "static/json/" + filtroGenero + "/categorias.json", true);
    requestCategorias.setRequestHeader("Content-Type", "text/plain;charset=UTF-8");

    requestCategorias.onload = function () {
        var data = JSON.parse(this.response);
        if (requestCategorias.status >= 200 && requestCategorias.status < 400) {
            data.forEach((data) => {
                var liCategorias = document.createElement("li");

                liCategorias.innerHTML =
                    "<form action='mudacategoria' method='post'><input type='hidden' name='categoria' value='" +
                    data.nomeOriginal +
                    "'/><input type='hidden' name='genero' value='" +
                    itensPagina[3] +
                    "'/><input type='submit' name='add' value='" +
                    data.nomeCategoria +
                    "' data-categoria='" +
                    data.nomeCategoria +
                    "'></form>";

                var containerMenu = document.getElementById("sub-menu-ul");
                containerMenu.appendChild(liCategorias);

                var containerMenu = document.getElementById("sub-menu-ul");
            });
        } else {
            console.log("error");
        }
    }
    requestCategorias.send();
}

//VISÃO HÉTERO
// VALIDAÇÃO APÓS REALIZAR BUSCA
if (itensPagina[3] == "?hetero" && itensPagina[4] == "?busca") {
	entrounaBusca = true;
	//metodoRealizaBusca(itensPagina[5], itensPagina[6]);
}
// VALIDAÇÃO SELECIONANDO CATEGORIA E CONSIDERANDO PAGINAÇÃO
else if (itensPagina[3] == "?hetero" && itensPagina[4] == "?categoria") {
    metodoSelecionaCategoria(itensPagina[5], itensPagina[6]);
}
// VALIDAÇÃO DA PAGINA HOME (ISSO SERÁ REMOVIDO)
else if (itensPagina[3] == "?hetero" && itensPagina[4] == "") {
    metodoSelecionaCategoria("");
}

//VISÃO GAY
// VALIDAÇÃO APÓS REALIZAR BUSCA
else if (itensPagina[3] == "?gay" && itensPagina[4] == "?busca") {
    metodoRealizaBusca(itensPagina[5], itensPagina[6]);
}
// VALIDAÇÃO SELECIONANDO CATEGORIA E CONSIDERANDO PAGINAÇÃO
else if (itensPagina[3] == "?gay" && itensPagina[4] == "?categoria") {
    metodoSelecionaCategoria(itensPagina[5], itensPagina[6]);
}
// VALIDAÇÃO DA PAGINA HOME (ISSO SERÁ REMOVIDO)
else if (itensPagina[3] == "?gay" && itensPagina[4] == "") {
    metodoSelecionaCategoria("");
}

// APÓS APERTAR O ENTER NO CAMPO DE BUSCA, REALIZA CHAMADA PARA UM CLICK FORÇADO NO BOTÃO
var input = document.getElementById("campoBusca");

input.addEventListener("keyup", function (event) {
    if (event.keyCode === 13) {
        event.preventDefault();
        document.getElementById("botaoBusca").click();
    }
});

function exibePaginaBanner(){
	setTimeout(function() {
		document.getElementById('botaoBanner').click();
    }, 300);
    
}

// EXIBE VÍDEOS DA CATEGORIA SELECIONADA
function metodoSelecionaCategoria(categoria, pagina) {

    //SPINNER DISPLAY BLOCK
    var spinner = document.getElementById("load-container");
    spinner.style.display = "flex";

    console.log("pagina == " + pagina);

    var paginaGlobal = 0;

    //SPINNER DISPLAY NONE
    spinner.style.display = "none";

    var tituloPagina = document.createElement("H1");
    tituloPagina.setAttribute("class", "category-title");

    var bread = document.getElementById("breadcrumb-container");
    bread.appendChild(tituloPagina);

    //HOME *****************************************************
    if (pagina == undefined) {
        var container = document.getElementById("paginacao");
        var containerHome = document.getElementById("container");
        containerHome.classList.add("containerHome");

        container.style.display = "none";
        bread.style.display = "none";

		var requestThumbsHome = new XMLHttpRequest();
        requestThumbsHome.open("GET", "static/json/" + filtroGenero + "/tudaoHome.json", true);
        requestThumbsHome.onload = function () {
            var data2 = JSON.parse(this.response);

            if (requestThumbsHome.status >= 200 && requestThumbsHome.status < 400) {
                console.log(Object.values(data2)[0].length);
                var categoriaAtual = "";
                var categoriasExibidas = 0;

                for (var j = 1; j < Object.values(data2)[0].length; j++) {
                    if (categoriaAtual == "") {
                        categoriaAtual = Object.values(data2)[0][j].categoriabr;
                    }
                    if (categoriaAtual != Object.values(data2)[0][j].categoriabr || j == 1) {
                        categoriaAtual = Object.values(data2)[0][j].categoriabr;
                        categoriasExibidas++;
                        var thumbVideoContainer = document.createElement("div");
                        thumbVideoContainer.setAttribute("class", "thumb-img porn-grid-xs-1");

                        var url = "/?" + filtroGenero + "/?categoria=" + Object.values(data2)[0][j].categoria + "/?1";
                        var linkVideo = document.createElement("a");
                        linkVideo.setAttribute("href", url);

                        linkVideo.innerHTML = "<div class='imgTime'><img class='imgThumb' src='" + Object.values(data2)[0][j].imagemVideo + "'/></div> <h3 class='videoName'>" + Object.values(data2)[0][j].categoriabr + "</h3>";

                        thumbVideoContainer.appendChild(linkVideo);

                        var container = document.getElementById("container");
                        container.appendChild(thumbVideoContainer);

                        /*var imgQuebrada = document.getElementsByClassName('imgThumb')[j];

                                    if(!imgQuebrada.length) {
                                        alert('Imagem está quebrada');
                                    }else {
                                        alert('Imagem está suave');
                                    }*/
                    }

                    if (categoriasExibidas == 30) {
                        break;
                    }
                }
            } else {
                console.log("error");
            }
        };
        requestThumbsHome.send();
    } else {
        //SPINNER DISPLAY BLOCK
        var spinner = document.getElementById("load-container");
        spinner.style.display = "flex";

		//REQUEST PARA EXIBIR OS VÍDEOS DA CATEGORIA SELECIONADA
		var requestThumbsSelCategoria = new XMLHttpRequest();
        requestThumbsSelCategoria.open("GET", "static/json/" + filtroGenero + "/" + categoria + ".json", true);
        var exibeNomeSite = "";

        requestThumbsSelCategoria.onload = function () {

            spinner.style.display = "none";

            var data = JSON.parse(this.response);
            tituloPagina.innerHTML = Object.values(data)[0][0].categoria;
            pagina = pagina.replace("?", "");
            pagina = parseInt(pagina);
            paginaGlobal = pagina;
			var videosRepetidos = [];
			var tamanhoLista = Object.values(data)[0].length;
			var contadorDeVideosExibidos = 0
			
            for (var j = 1; j < Object.values(data)[0].length; j++) {
                var paginaFinal = pagina * 30;
                var paginaInicial = paginaFinal - 30;
				if(!videosRepetidos.includes(Object.values(data)[0][j].nomeVideo)){
					videosRepetidos.push(Object.values(data)[0][j].nomeVideo)
					if (j > paginaInicial) {
						contadorDeVideosExibidos++
						var thumbVideoContainer = document.createElement("div");
						thumbVideoContainer.setAttribute("class", "thumb-img porn-grid-xs-1");

						var urlVideo = Object.values(data)[0][j].linkvideo;
						var linkVideo = document.createElement("a");
							linkVideo.setAttribute("onclick", "exibePaginaBanner()");
							linkVideo.setAttribute("href", urlVideo);
							linkVideo.setAttribute("target", "_blank");

						if (urlVideo.indexOf("xhamster") >= 0) {
						   exibeNomeSite = 'xhamster';
						}else if (urlVideo.indexOf("redtube") >= 0){
						   exibeNomeSite = 'redtube';
						}

						linkVideo.innerHTML =
							"<div class='imgTime'><span class='durationVideo'>" +
							Object.values(data)[0][j].duracaoVideo +
							"</span><img class='imgThumb' src='" +
							Object.values(data)[0][j].imagemVideo +
							"'/></div> <h3 class='videoName'>" +
							Object.values(data)[0][j].nomeVideo +
							"</h3><p class='nomeDoSite'>" + exibeNomeSite + "</p>";

						thumbVideoContainer.appendChild(linkVideo);

						var container = document.getElementById("container");
						container.appendChild(thumbVideoContainer);
					}
				}
				else{
					tamanhoLista--;
				}
				if (contadorDeVideosExibidos == 30) {
					break;
				}
            }

            var paginas = tamanhoLista / 30;
            var paginasFinal = Math.round(paginas);
            var paginasIniciais = 1;
            var showInicio = false;
            var showFinal = false;

            if (paginaGlobal >= 4) {
                paginasIniciais = paginaGlobal - 3;
            }

            for (var i = paginasIniciais; i <= paginasFinal; i++) {
                var linkPaginas = document.createElement("span");
                linkPaginas.innerHTML =
                    "<form action='mudapagina' method='post'><input type='hidden' name='pagina' value='" +
                    i +
                    "'/><input type='hidden' name='genero' value='" +
                    filtroGenero +
                    "'/><input type='hidden' name='categoria' value='" +
                    categoria +
                    "'/><input type='submit' name='add' class='pagina" +
                    i +
                    "' value='" +
                    i +
                    "'></form>";

                var container = document.getElementById("paginacao");
                container.appendChild(linkPaginas);

                if (i == paginaGlobal + 3) {
                    break;
                }

                if (paginaGlobal != 1 && showInicio == false) {
                    showInicio = true;

                    var linkPaginaInicio = document.createElement("span");
                    linkPaginaInicio.innerHTML =
                        "<form action='mudapagina' method='post'><input type='hidden' name='pagina' value='1'/><input type='hidden' name='genero' value='" +
                        filtroGenero +
                        "'/><input type='hidden' name='categoria' value='" +
                        categoria +
                        "'/><input type='submit' name='add' class='pagina0' value='INÍCIO'></form>";

                    var paginaInicialContainer = document.getElementById("paginaInicio");
                    paginaInicialContainer.appendChild(linkPaginaInicio);
                }

                if (paginaGlobal != paginasFinal && showFinal == false) {
                    showFinal = true;

                    var linkPaginaFinal = document.createElement("span");
                    linkPaginaFinal.innerHTML =
                        "<form action='mudapagina' method='post'><input type='hidden' name='pagina' value='" +
                        paginasFinal +
                        "'/><input type='hidden' name='genero' value='" +
                        filtroGenero +
                        "'/><input type='hidden' name='categoria' value='" +
                        categoria +
                        "'/><input type='submit' name='add' class='pagina0' value='FIM'></form>";

                    var paginaFinalContainer = document.getElementById("paginaFim");
                    paginaFinalContainer.appendChild(linkPaginaFinal);
                }
            }

            document.querySelector(".pagina" + paginaGlobal).disabled = true;
        };
        requestThumbsSelCategoria.send();
    }
}

// EXIBE VÍDEOS DA BUSCA REALIZADA
function metodoRealizaBusca(textoBusca, paginaGlobal) {
    //SPINNER DISPLAY BLOCK
    var spinner = document.getElementById("load-container");
    spinner.style.display = "flex";

	if (requestThumbsBusca.status >= 200 && requestThumbsBusca.status < 400) {
		//SPINNER DISPLAY NONE
		spinner.style.display = "none";

		var tituloPagina = document.createElement("H1");
		tituloPagina.setAttribute("class", "category-title");
		tituloPagina.innerHTML = "BUSCA - " + textoBusca;

		var bread = document.getElementById("breadcrumb-container");
		bread.appendChild(tituloPagina);

		var videos = dataBusca.videos;
		videos.sort((a, b) => (a.categoria > b.categoria) ? 1 : -1);
		var newData =  videos.filter(function(row) {
			return row.nomeVideo.includes(textoBusca);
		});
		//VARIÁVEL PARA CONTROLE CASO NÃO TRAGA RESULTADOS
		var videosRepetidos = [];
		paginaGlobal = paginaGlobal.replace("?", "");
		paginaGlobal = parseInt(paginaGlobal);

		var contadorDePaginas = 0;
		for (var i = 1; i < newData.length; i++) {
			var paginaFinal = paginaGlobal * 30;
			var paginaInicial = paginaFinal - 30;
			if(!videosRepetidos.includes(newData[i].nomeVideo)){
				contadorDePaginas++;
				videosRepetidos.push(newData[i].nomeVideo)

				if (contadorDePaginas > paginaInicial && contadorDePaginas <= paginaFinal) {
					document.getElementById("textoErro2").innerHTML = "";
					var thumbVideoContainer = document.createElement("div");
					thumbVideoContainer.setAttribute("class", "thumb-img porn-grid-xs-1");

					var urlVideo = newData[i].linkvideo;
					var linkVideo = document.createElement("a");
					linkVideo.setAttribute("onclick", "exibePaginaBanner()");
					linkVideo.setAttribute("href", newData[i].linkvideo);
					linkVideo.setAttribute("target", "_blank");
					var exibeNomeSite = "";
                    if (urlVideo.indexOf("xhamster") >= 0) {
                       exibeNomeSite = 'xhamster';
                    }else if (urlVideo.indexOf("redtube") >= 0){
                       exibeNomeSite = 'redtube';
                    }

					linkVideo.innerHTML =
						"<div class='imgTime'><span class='durationVideo'>" + newData[i].duracaoVideo + "</span><img class='imgThumb' src='" + newData[i].imagemVideo + "'/></div> <h3 class='videoName'>" + newData[i].nomeVideo + "</h3><p class='nomeDoSite'>" + exibeNomeSite + "</p>";

					thumbVideoContainer.appendChild(linkVideo);

					var container = document.getElementById("container");
					container.appendChild(thumbVideoContainer);
				}
			}	
		}
		if (contadorDePaginas == 0) {
			event.preventDefault();
			var darkModeCache = localStorage.getItem("darkMode");
			document.getElementById("textoErro2").innerHTML = '<div class="textoErroContent"><img src="static/images/load-icon.png"/><br/>SEM RESULTADOS PARA A BUSCA REALIZADA!</div>';

			if (darkModeCache == "true") 
				document.getElementById("textoErro2").style.color = "black";
			else 
				document.getElementById("textoErro2").style.color = "white";
		}
		else{
			var paginas = contadorDePaginas / 30;
			var isInteger = Number.isInteger(paginas);
			var paginasFinal = 0;
			var paginasIniciais = 1;
			var showInicio = false;
			var showFinal = false;

			if (isInteger)
				paginasFinal = paginas;
			else 
				paginasFinal = Math.round(paginas) + 1;

			if (paginaGlobal >= 4)
				paginasIniciais = paginaGlobal - 3;

			for (var i = paginasIniciais; i <= paginasFinal; i++) {
				var linkPaginas = document.createElement("span");
				linkPaginas.innerHTML =
					"<form action='mudapaginaBusca' method='post'><input type='hidden' name='pagina' value='" +
					i +
					"'/><input type='hidden' name='genero' value='" +
					filtroGenero +
					"'/><input type='hidden' name='busca' value='" +
					textoBusca +
					"'/><input type='submit' name='add' class='pagina" +
					i +
					"' value='" +
					i +
					"'></form>";

				var container = document.getElementById("paginacao");
				container.appendChild(linkPaginas);

				if (i == paginaGlobal + 3) {
					break;
				}

				if (paginaGlobal != 1 && showInicio == false) {
					showInicio = true;

					var linkPaginaInicio = document.createElement("span");
					linkPaginaInicio.innerHTML =
						"<form action='mudapaginaBusca' method='post'><input type='hidden' name='pagina' value='1'/><input type='hidden' name='genero' value='" +
						filtroGenero +
						"'/><input type='hidden' name='busca' value='" +
						textoBusca +
						"'/><input type='submit' name='add' class='pagina0' value='INÍCIO'></form>";

					var paginaInicialContainer = document.getElementById("paginaInicio");
					paginaInicialContainer.appendChild(linkPaginaInicio);
				}

				if (paginaGlobal != paginasFinal && showFinal == false) {
					showFinal = true;

					var linkPaginaFinal = document.createElement("span");
					linkPaginaFinal.innerHTML =
						"<form action='mudapaginaBusca' method='post'><input type='hidden' name='pagina' value='" +
						paginasFinal +
						"'/><input type='hidden' name='genero' value='" +
						filtroGenero +
						"'/><input type='hidden' name='busca' value='" +
						textoBusca +
						"'/><input type='submit' name='add' class='pagina0' value='FIM'></form>";

					var paginaFinalContainer = document.getElementById("paginaFim");
					paginaFinalContainer.appendChild(linkPaginaFinal);
				}
			}
			
			document.querySelector(".pagina" + paginaGlobal).disabled = true;
		}
	} else {
		console.log("error");
	}
}
