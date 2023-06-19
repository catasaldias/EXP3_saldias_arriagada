function calcular(pe){
  var dol = 2500; 
  var re ;   
  var pe =parseInt(document.getElementById('pesos').value, 10);
   
  re = pe / dol ;
  document.getElementById('resul').innerHTML= re;
  
  }
  