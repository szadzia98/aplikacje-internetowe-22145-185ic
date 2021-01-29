var i = 0;
var potega = 0;
function powCount() {
    potega = i * i;
    i = i+1;
    postMessage(potega)
  setTimeout("powCount()",500);
}

powCount();

