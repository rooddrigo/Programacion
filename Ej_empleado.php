<?php
class empleado {
    public $nombre;
    public $sueldo;

    public function mostrarDetalles() {
        echo "\nEl empleado, ". $this-> nombre. " gana ". $this->sueldo;
    }
}

class gerente extends empleado {
    public $departamento;

    public function mostarDetalles() {
        echo "\nEl gerente, " . $this->nombre . " gana " . $this->sueldo. " y está en el departamento de ". $this->departamento;
    }
}

$empleadillo = new empleado();
$empleadillo->nombre = "Rodrigo Rios";
$empleadillo->sueldo = "1500€";
$empleadillo -> mostrarDetalles();

$gerentillo = new gerente();
$gerentillo->nombre = "César Rios";
$gerentillo->sueldo = "2500€";
$gerentillo->departamento = "Limpieza";
$gerentillo -> mostarDetalles();
?>