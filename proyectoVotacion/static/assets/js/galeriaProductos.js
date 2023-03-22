function fotoMedianaGrande (src){
    var ruta = src.replace("medium", "big");
    window.open(ruta, "_blank");
}

function cambiarfotoSiguiente (){
    const elementos = document.getElementsByClassName('smallfoto');
    var arr = Array.prototype.slice.call(elementos)
    var ruta = elementos[1].currentSrc.replace("small", "medium");
    var mediana = document.getElementById("medium");
    var x = mediana.src.replace("medium", "small");
    var actual = arr.findIndex(element => element.currentSrc === x);
    if(actual == (arr.length-1)){
        siguiente = 0;
    }
    else{
        siguiente = actual + 1;
    }
    console.log(siguiente);
    var elem = elementos[siguiente].src.replace("small", "medium");
    document.getElementById("medium").src = elem;
}

function cambiarfotoAnterior(){
    const elementos = document.getElementsByClassName('smallfoto');
    var arr = Array.prototype.slice.call(elementos)
    var ruta = elementos[1].currentSrc.replace("small", "medium");
    var mediana = document.getElementById("medium");
    var x = mediana.src.replace("medium", "small");
    var actual = arr.findIndex(element => element.currentSrc === x);
    if(actual == 0){
        anterior = arr.length - 1;
    }
    else{
        anterior = actual - 1;
    }
    console.log(anterior);
    var elem = elementos[anterior].src.replace("small", "medium");
    document.getElementById("medium").src = elem;
}

function onClickChange(small){
    var medium = document.getElementById("medium");
    var src = small.src;
    var newSrc = src.replace("small", "medium");
    medium.src = newSrc;
}

