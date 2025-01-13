<?php
class circulo{
    public $radio;
    public $area;
    public function calcularArea(){
        echo "\nEl área de una circunferencia de radio: ". $this->radio. ", es ". 2*3.14*$this->radio;
    }
}

$circulito = new circulo;
$circulito->radio = 2;
$circulito->calcularArea();
?>