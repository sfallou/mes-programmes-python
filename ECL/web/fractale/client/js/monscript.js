
var Colorselect = document.getElementById('color')
  , reponse =  document.getElementById('reponse')
  , largeur = document.getElementById('width')
  , hauteur = document.getElementById('height')
  , image =  document.querySelector('#reponse img')
  , envoyer =  document.getElementById('envoyer')
  ,message = document.getElementById('message')
  , r = new XMLHttpRequest()
;

// déclaration du gestionnaire d'événement pour les boutons
envoyer.addEventListener('click',traitement);
message.innerHTML="L'image s'affiche ici";
// récupération de la liste des couleurs
/*r.onload = function() {
  var data = JSON.parse(this.responseText)
    , n, o
  ;
  for ( n = 0; n < data.length; n++ ) {
    o = document.createElement('option');
    o.value = data[n].type+'/'+data[n].code;
    o.textContent = data[n].nom;
    ligneselect.appendChild(o);
  }
}
r.open('GET','/lignes',true);
r.send();
*/
// traitement du clic sur le bouton
function traitement(event) {
  var button = event.target
    , color = Colorselect.value
    , w = largeur.value
    , h = hauteur.value
    , r = new XMLHttpRequest()
    , method
  ;
  // récupération
  if ( button.id == 'envoyer') {
    //on verifie que les parametres entrées sont correctes
    var regExp = /^0[0-9]/
    if (regExp.test(w) || regExp.test(h) || w<=0 || h<=0 || !isInt(w) || !isInt(h) ){
      alert("Attention!! Les valeurs que vous donnez sont incorrects !")
      return
      }
    message.innerHTML="<div style='color:red;'><b>Requête en cours de traitement! Merci de patienter</b></div>";
    r.onload = function() {
      var data = JSON.parse(this.responseText);
      image.src = data.image;
      image.alt = data.alt;
      image.title = data.title;
      reponse.style.display = 'block';
      message.innerHTML="Voila l'image générée par le serveur! ";
    };
    method = 'POST';
  }
  r.open(method,'/percolation/'+color+'/'+w+'/'+h,true);
  r.send();
}

function isInt(val) {
    var intRegex = /^-?\d+$/;
    if (!intRegex.test(val))
        return false;

    var intVal = parseInt(val, 10);
    return parseFloat(val) == intVal && !isNaN(intVal);
}