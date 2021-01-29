var i = 0;
var suma = 0;
var lastSuma = 0;
var last2Suma = 0;
function fibCount() {
    if (i == 0){
        postMessage(suma)
        i = i+1;
    }
    else if(i == 1){
        suma = suma + 1;
        postMessage(suma)
        i = i + 1;
        lastSuma = suma;
    } else {
        suma = last2Suma+ lastSuma;
        postMessage(suma);
        last2Suma = lastSuma;
        lastSuma = suma;
    }
  setTimeout("fibCount()",500);
}

fibCount();


