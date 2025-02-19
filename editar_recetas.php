<?php
class recetaEditar {
    private $conexion;
    // Creamos la conexion.
    public function __construct() {
        $this->conexion = new mysqli("localhost", "root", "curso", "recetas");
        if ($this->conexion->connect_error) {
            die("Error en la conexión: " . $this->conexion->connect_error);
        }
    }
    // creamos la funcion sacar los datos de la receta mediante su id, al haberle dada a editar una receta.
    public function obtenerReceta($id) {
        $query = "SELECT * FROM recetas WHERE id = ?";
        $stmt = $this->conexion->prepare($query);
        $stmt->bind_param("i", $id);
        $stmt->execute();
        $resultado = $stmt->get_result();
        return $resultado->fetch_assoc();
    }
    // Hacemos un update de los datos nuevos
    public function actualizarReceta($id, $nombre, $descripcion) {
        $query = "UPDATE recetas SET receta = ?, descripcion = ? WHERE id = ?";
        $stmt = $this->conexion->prepare($query);
        $stmt->bind_param("ssi", $nombre, $descripcion, $id);
        return $stmt->execute();
    }
}

// Comprobamos que hayamos obtenido el id de la receta a editar.
if (!isset($_GET['id'])) {
    die("ID de receta no válido.");
}
$id = $_GET['id'];

// Llamamos a la función y le pasamos el parametro obtenido del id para sacar sus datos
$editarReceta = new recetaEditar();
$receta = $editarReceta->obtenerReceta($id);

// Obtenemos el nombre y la descripcion para actualizarla posteriormente
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $nombre = $_POST['nombre'];
    $descripcion = $_POST['descripcion'];
    
    // Comprobamos que los datos no estén vacios para evitar posibles errores en sql

    if (!empty($nombre) && !empty($descripcion)) {
        if ($editarReceta->actualizarReceta($id, $nombre, $descripcion)) {
            // Añadimos ese location para al terminar volver al inicio y controlamos los errores.
            header("Location: recetas.php");
            exit();
        } else {
            echo "Error al actualizar la receta.";
        }
    } else {
        echo "Todos los campos son obligatorios.";
    }
}
?>
<!-- Creamos el formulario para editar. -->
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Editar Receta</title>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css">
</head>
<body>
    <div class="container">
        <h2 class="mt-4">Editar Receta</h2>
        <form action="" method="POST">
            <div class="mb-3">
                <label for="nombre" class="form-label">Nombre de la Receta</label>
                <input type="text" id="nombre" name="nombre" class="form-control" value="<?= $receta['receta'] ?>" required>
            </div>
            <div class="mb-3">
                <label for="descripcion" class="form-label">Descripción</label>
                <textarea id="descripcion" name="descripcion" class="form-control" required><?= $receta['descripcion'] ?></textarea>
            </div>
            <!-- Añadimos una opción de cancelar y otra de confirmación -->
            <button type="submit" class="btn btn-success">Actualizar</button>
            <a href="recetas.php" class="btn btn-secondary">Cancelar</a>
        </form>
    </div>
</body>
</html>
