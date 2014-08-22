function calcuateArray(callback){
  var a = [1, 2, 3, 4];
  a.map(function(x){return x*x});
  callback(a);
}

(function(){
  calcuateArray(console.log);
})();
