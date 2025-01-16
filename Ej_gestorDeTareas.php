<?php
class tarea {
    public $nombre;
    public $descripcion;
    public $fechaLimite;
    public $estado = "sin completar";

    public function marcarComoCompletada() {
        $this->estado = "Completada";
        echo "Tarea de " . $this->nombre . " completada!!\n";
    }

    public function editarDescripcion($nuevaDescripcion) {
        $this->descripcion = $nuevaDescripcion;
    }

    public function mostrarTarea() {
        echo "Nombre: " . $this->nombre . "\n";
        echo "Descripción: " . $this->descripcion . "\n";
        echo "Fecha Límite: " . $this->fechaLimite . "\n";
        echo "Estado: " . $this->estado . "\n";
    }
}

$tareas = [];

$tareas[0] = new tarea();
$tareas[0]->nombre = "Limpiar";
$tareas[0]->descripcion = "Pereza";
$tareas[0]->fechaLimite = "2025-01-20";

$tareas[1] = new tarea();
$tareas[1]->nombre = "Fregar";
$tareas[1]->descripcion = "Más pereza aún";
$tareas[1]->fechaLimite = "2025-02-01";

$tareas[2] = new tarea();
$tareas[2]->nombre = "Programar";
$tareas[2]->descripcion = "Odio PHP";
$tareas[2]->fechaLimite = "2025-03-10";

echo "Tareas sin completar:\n";
foreach ($tareas as $tarea) {
    $tarea->mostrarTarea();
    echo "\n";
}

$tareas[2]->marcarComoCompletada();
$tareas[2]->editarDescripcion("Pero haré un esfuerzo");
$tareas[0]->editarDescripcion("Me sigue dando pereza");
$tareas[1]->editarDescripcion("No hace falta ni decirlo");

echo "\nTareas con la modificación:\n";
foreach ($tareas as $tarea) {
    $tarea->mostrarTarea();
    echo "\n";
}
?>

