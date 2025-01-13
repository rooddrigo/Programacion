<?php
class calculadora {
    public $numero1;
    public $numero2;
    public function suma(){
    $suma = $this->numero1 + $this->numero2;
    echo "La suma total es: ". $suma;
 }
    public function resta(){
    $resta = $this->numero1 - $this->numero2;
    echo "\nLa resta total es: ". $resta;
 }
    public function producto(){
    $producto = $this->numero1 * $this->numero2;
    echo "\nEl producto total es: ". $producto;
 }
    public function cociente(){
        if($this->numero2 != 0){
        $cociente = $this->numero1 / $this->numero2;
        echo "\nEl cociente total es: ". $cociente;  
        }else{
            echo "\nNo se puede dividir por 0.";
        }
 }
}
$calculos = new calculadora();
$calculos->numero1 = 25;
$calculos->numero2 = 5;
$calculos -> suma();
$calculos -> resta();
$calculos -> producto();
$calculos -> cociente();
?>