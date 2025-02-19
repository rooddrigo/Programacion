<?php

class borrarRecetas {
    private $conexion;
    
    // creamos la conexion
    public function __construct() {
        $this->conexion = new mysqli("localhost", "root", "curso", "recetas");
        if ($this->conexion->connect_error) {
            die("Error en la conexión: " . $this->conexion->connect_error);
        }
    }
    
    // Creamos la funcion de eliminar pasandole el id de la receta.
    public function eliminarReceta($id) {
        $query = "DELETE FROM recetas WHERE id = ?";
        $stmt = $this->conexion->prepare($query);
        $stmt->bind_param("i", $id);
        return $stmt->execute();
    }
}

// Obtenemos el id de esa receta y la eliminamos llamando a la función creada con ese fin.
$id = $_GET['id'] ?? null;
if ($id) {
    $recetaDB = new borrarRecetas();
    if ($recetaDB->eliminarReceta($id)) {
        header("Location: recetas.php");
        // Volvemos a la principal y comprobamos errores
        exit();
    } else {
        echo "Error al eliminar la receta.";
    }
} else {
    echo "ID no válido.";
}
?>
