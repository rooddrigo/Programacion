<?php
class Empleado {
    private $nombre;
    private $sueldo;
    private $puesto;

    public function __construct($nombre, $sueldo, $puesto) {
        $this->nombre = $nombre;
        $this->sueldo = $sueldo;
        $this->puesto = $puesto;
    }
    public function setSueldo($nuevoSueldo) {
        $this->sueldo = $nuevoSueldo;
        echo "\nEste es el nuevo sueldo del empleado: " . $nuevoSueldo . "€";
    }
    public function getSueldo() {
        return $this->sueldo;
    }
    public function getNombre() {
        return $this->nombre;
    }
    public function getPuesto() {
        return $this->puesto;
    }
}

class Manager extends Empleado {
    private $departamento;

    public function __construct($nombre, $sueldo, $puesto, $departamento) {
        parent::__construct($nombre, $sueldo, $puesto);
        $this->departamento = $departamento;
    }
    public function revisarEmpleado(Empleado $empleado) {
        echo "\nNombre del empleado: " . $empleado->getNombre();
        echo "\nPuesto del empleado: " . $empleado->getPuesto();
    }
    public function puestoDepartamento() {
        echo "\nDepartamento del empleado: " . $this->departamento;
    }
}

$empleado = new Empleado("Manolito", 1500, "Currito");
$manager = new Manager("Sr. Manuel", 3000, "Supervisor", "Ventas");
$manager->revisarEmpleado($empleado);
$manager->puestoDepartamento();
$empleado->setSueldo(readline("\nIntroduce el sueldo que le quieras poner al currito: "));
?>