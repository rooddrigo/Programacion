<?php
class vehiculo {
    public $marca;

    public function encender() {
        echo "\nEstá arrancado, brum brum";
    }
}

class coche extends vehiculo {
    public $modelo;

    public function mensaje() {
        echo "El " . $this->marca . " " . $this->modelo;
    }
}

$vehiculito = new coche();
$vehiculito->marca = "Mercedes"; 
$vehiculito->modelo = "AMG"; 
$vehiculito->mensaje();
$vehiculito->encender();
?>
