function verification_formulaire()
{
 if(document.formulaire_finance.date1.value == "")  {
   alert("Veuillez entrer la première date");
   document.formulaire_finance.date1.focus();
   return false;
  }
 if(document.formulaire_finance.date2.value == "")  {
   alert("Veuillez entrer la deuxième date");
   document.formulaire_finance.date2.focus();
   return false;
  }
 
}