
var Colorselect = document.getElementById('color')
  , reponse =  document.getElementById('reponse')
  , ray = document.getElementById('rayon')
  , image =  document.querySelector('#reponse img')
  , envoyer =  document.getElementById('envoyer2')
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
    , R = ray.value
    , r = new XMLHttpRequest()
    , method
  ;
  // récupération
  if ( button.id == 'envoyer2') {
    //on verifie que les parametres entrées sont correctes
    var regExp = /^0[0-9]/
    if (regExp.test(R) || R<=0 || !isInt(R)){
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
  r.open(method,'/percolation2/'+color+'/'+R,true);
  r.send();
}

function isInt(val) {
    var intRegex = /^-?\d+$/;
    if (!intRegex.test(val))
        return false;

    var intVal = parseInt(val, 10);
    return parseFloat(val) == intVal && !isNaN(intVal);
}