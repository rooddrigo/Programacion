<?php
class Empleado {
    public $nombre;
    public $sueldo;
    public $añosExperiencia;

    public function calcularBonus() {
        $this->sueldo *= (1 + floor($this->añosExperiencia / 2) * 0.05);
    }

    public function mostrarDetalles() {
        echo "\nNombre: " . $this->nombre . "\n";
        echo "Sueldo: " . $this->sueldo . "€\n";
        echo "Años de Experiencia: " . $this->añosExperiencia . "\n";
    }
}

class Consultor extends Empleado {
    public $horasPorProyecto;

    public function calcularBonus() {
        if ($this->horasPorProyecto > 100) {
            $this->sueldo += 0.1 * $this->sueldo;
        }
    }
}

$empleado = new Empleado();
$empleado->nombre = "Pepe";
$empleado->sueldo = 2000;
$empleado->añosExperiencia = 10;

if ($empleado->añosExperiencia > 2) {
    $empleado->calcularBonus();
}
$empleado->mostrarDetalles();
$consultor = new Consultor();
$consultor->nombre = "Ana";
$consultor->sueldo = 2500;
$consultor->añosExperiencia = 5;
$consultor->horasPorProyecto = 120;
if ($consultor->añosExperiencia > 2) {
    $consultor->calcularBonus();
}
$consultor->mostrarDetalles();

?>
