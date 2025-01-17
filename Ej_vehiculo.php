<?php
class Vehiculo{
    private $marca;
    private $modelo;
    public function __construct($marca,$modelo)
    {
        $this->marca = $marca;
        $this->modelo = $modelo;
    }
    public function encender (){
        echo "\nEl coche está arrancado brum brum...";
    }
    public function getMarca(){
        return $this->marca;
    }
    public function getModelo(){
        return $this->modelo;
    }
}
class Coche extends Vehiculo{
    private $combustible;
    public function __construct($marca,$modelo,$combustible)
    {
        parent::__construct($marca,$modelo);
        $this->combustible = $combustible;
    }
    public function mostrarDetalles(){
        echo "\nMarca: ".parent::getMarca();
        echo "\nModelo: ".parent::getModelo();
        echo "\nTipo de Combustible: ".$this->combustible;
    }
}

$carro = new Coche("Mercedes", "AMG GT", "Gasolina");
$carro->mostrarDetalles();
?>