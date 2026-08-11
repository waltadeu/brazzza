function alteraCorErro() {

    var darkModeCache = localStorage.getItem('darkMode');

    if (darkModeCache == "true")
        document.getElementById("textoErro2").style.color = 'black';
    else
        document.getElementById("textoErro2").style.color = 'white';
}

function validaTextoBuscado() {
    var textoBuscado = document.getElementById("campoBusca").value;;

    if (textoBuscado.length < 2) {
        event.preventDefault();
        document.getElementById("textoErro").style.display = "block";
        document.getElementById("textoErro").innerHTML = 'DIGITE 2 DÍGITOS OU MAIS PARA REALIZAR A BUSCA!';

        setTimeout(function() {
            document.getElementById("textoErro").style.display = "none";
        }, 6000);
    }
}

// DARKMODE & GENDER & HAND
window.onload = function() {
	
    //VARIAVEL GENERO
    var filterGenero = localStorage.getItem('genero');

    if (filterGenero == "gay") {
        var filtroGenero = 'gay';
        document.getElementById("genero-gay").checked = true;
        document.getElementById("campoGenero").value = 'gay';
    } else {
        var filtroGenero = 'hetero';
        document.getElementById("genero-hetero").checked = true;
        document.getElementById("campoGenero").value = 'hetero';
    }


    //DARK MODE
    var darkModeCache = localStorage.getItem('darkMode');
    var btnDarkMode = document.getElementById('dark-mode-btn');

    if (darkModeCache == "true") {
        document.body.classList.remove("darkModeView");
        document.body.classList.add("whiteModeView");
    } else {
        btnDarkMode.checked = true;
        document.body.classList.add("darkModeView");
        document.body.classList.remove("whiteModeView");
    }

    //HAND
    var maoEscolhida = localStorage.getItem('maoEscolhida');

    if (maoEscolhida == "direita") {
        document.body.classList.remove("maoEsquerdaClass");
        document.body.classList.add("maoDireitaClass");

        modal.style.display = 'none';
    } else if (maoEscolhida == 'nenhumamao') {
        document.body.classList.remove("maoEsquerdaClass");
        document.body.classList.remove("maoDireitaClass");

        modal.style.display = 'none';
    } else if (maoEscolhida == 'esquerda'){
        document.body.classList.add("maoEsquerdaClass");
        document.body.classList.remove("maoDireitaClass");

        modal.style.display = 'none';
    }
    else{
        if(window.screen.width <= 576)
            modal.style.display = 'flex';
    }

}

//DARKMODE - ACTION
var btnDarkMode = document.getElementById('dark-mode-btn');
btnDarkMode.onclick = function() {
    if (btnDarkMode.checked) {
        console.log('Dark Mode => Inativo');
        document.body.classList.add("darkModeView");
        document.body.classList.remove("whiteModeView");

        localStorage.setItem('darkMode', 'false');
    } else {
        console.log('Dark Mode => Ativo');
        document.body.classList.remove("darkModeView");
        document.body.classList.add("whiteModeView");

        localStorage.setItem('darkMode', 'true');
    }
}


//CLOSE HAMBURG-MENU MOBILE
var subMenuCat = document.getElementById('sub-menu');
var openHamburgMenu = document.getElementById('hamburg-menu');
var closeHamburgMenu = document.getElementById('close-hamburg-menu');
closeHamburgMenu.style.display = 'none';

openHamburgMenu.onclick = function() {
    subMenuCat.style.display = 'block';
    openHamburgMenu.style.display = 'none';
    closeHamburgMenu.style.display = 'block';
}

closeHamburgMenu.onclick = function() {
    subMenuCat.style.display = 'none';
    openHamburgMenu.style.display = 'block';
    closeHamburgMenu.style.display = 'none';
}

//CLOSE MODAL
var modal = document.getElementById('modal');
var closeModal = document.getElementById('close-modal');
var openModal = document.getElementById('change-hand');

closeModal.onclick = function() {
    modal.style.display = 'none';
}

openModal.onclick = function() {
    modal.style.display = 'flex';
}

//CHANGE HAND
var removerMao = document.getElementById('remove-hand');
var maoDireita = document.getElementById('hand-right');
var maoEsquerda = document.getElementById('hand-left');

maoDireita.onclick = function() {
    console.log('Escolheu a mão direita!');
    document.body.classList.remove("maoEsquerdaClass");
    document.body.classList.add("maoDireitaClass");

    localStorage.setItem('maoEscolhida', 'direita');

    modal.style.display = 'none';
}

maoEsquerda.onclick = function() {
    console.log('Escolheu a mão esquerda!');
    document.body.classList.add("maoEsquerdaClass");
    document.body.classList.remove("maoDireitaClass");

    localStorage.setItem('maoEscolhida', 'esquerda');

    modal.style.display = 'none';
}

removerMao.onclick = function() {
    console.log('Escolheu navegar sem melhoria!');
    document.body.classList.remove("maoEsquerdaClass");
    document.body.classList.remove("maoDireitaClass");

    localStorage.setItem('maoEscolhida', 'nenhumamao');

    modal.style.display = 'none';
}


