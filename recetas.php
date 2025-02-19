<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">

<meta name="viewport" content="width=device-width, initial-
scale=1.0">

<link rel="stylesheet"
href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/boot
strap.min.css">
<link
href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;
400;600&display=swap" rel="stylesheet">
<style>
/* Código css reciclado del hito, para añadir container y dar estilos a las fuentes */
html {
height: 100%;
margin: 0;
overflow: auto;
}
body {
background-size: cover;
background-position: center;
background-repeat: no-repeat;
color: white;
font-family: 'Poppins', sans-serif;
display: flex;
justify-content: center;
align-items: flex-start;
flex-direction: column;
min-height: 100vh;
padding: 0;
}
.container {
background-color: rgba(88, 100, 98, 0.7);
padding: 30px;
border-radius: 8px;
width: 70%;
max-width: 900px;
box-shadow: 0 4px 10px rgba(0, 0, 0, 0.5);
margin-top: 20px;
margin-bottom: 20px;
}
h1, h2, p, h3 {
text-align: center;
color: black;
}
h1 {
font-size: 2.5rem;
font-weight: 600;
margin-top: 20px;
}
.btn {
background-color: rgb(9, 112, 229);
color: white;
border: none;
padding: 8px 15px;
font-size: 0.9rem;
margin-top: 10px;
border-radius: 5px;
}
.btn-primary:hover {
background-color: rgb(81, 175, 242);
}
.btn-secondary {
background-color: rgb(249, 100, 0);
color: white;
border: none;
padding: 8px 15px;
font-size: 0.9rem;
margin-top: 10px;
border-radius: 5px;
}
.btn-secondary:hover {
background-color: rgb(249, 153, 85);

}
.btn-danger {
background-color: rgb(220, 20, 60);
color: white;
border: none;
padding: 8px 15px;
font-size: 0.9rem;
margin-top: 10px;
border-radius: 5px;
}
.btn-danger:hover {
background-color: rgb(255, 70, 100);
}
.btn-success {
background-color: rgb(10, 170, 90);
color: white;
border: none;
padding: 8px 15px;
font-size: 0.9rem;
margin-top: 10px;
border-radius: 5px;
}
.btn-success:hover {
background-color: rgb(80, 210, 120);
}
.form-control, .form-select {
margin-bottom: 15px;
}
.form-label {
font-weight: bold;
}
ul {
list-style: none;
padding-left: 0;
}

li {
margin-bottom: 15px;
}
</style>
<title>Recetas</title>
</head>
<body>
<div class="container">
<?php
// Nos contectamos a la base de datos. (No he hecho el archivo conexión para hacer los mínimos phps posibles ;)
$conexion = new mysqli("localhost", "root", "curso", "recetas");
if ($conexion->connect_error) {
    die("Error en la conexión: " . $conexion->connect_error);
}

// Creamos la clase listartareas para que siempre nos aparezcan en la página principal
class ListarTareas {
    private $conexion;
// Accedemos a la conexión.
    public function __construct($conexion) {
        $this->conexion = $conexion;
    }
// Mediante la función listar Recetas, hacemos un select de toda la tabla recetas y lo guardamos en un array
    public function listarRecetas() {
        $query = "SELECT * FROM recetas;";
        $resultado = $this->conexion->query($query);

        // Nos aseguramos de que no de errores.
        if (!$resultado) {
            die("Error en la consulta: " . $this->conexion->error);
        }

        $recetas = [];
        while ($fila = $resultado->fetch_assoc()) {
            $recetas[] = $fila;
        }
        return $recetas;
    }
}
// Llamamos a la función.
$listar = new ListarTareas($conexion);
$recetas = $listar->listarRecetas();
?>

<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Lista de Recetas</title>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css">
</head>
<body>
    <!-- Creamos el input para buscar las recetas con la IA, utilizando un POST -->
    <div class="container">
        <h1 class="mt-8">Recetas</h2>
        <form action="crear_recetas.php" method="POST" class="mb-3">
            <div class="mb-3">
                <label for="nombre" class="form-label">Nombre de la Receta</label>
                <input type="text" id="nombre" name="nombre" class="form-control" placeholder="Ej: Ensalada César" required>
            </div>
        <table class="table table-striped">
            <thead>
                <tr>
                    <th>Nombre</th>
                    <th>Descripción</th>
                </tr>
            </thead>
            <tbody>
                <!-- Mediante un foreach, mostramos el array con todos los datos de recetas. -->
                <?php foreach ($recetas as $receta): ?>
                    <tr>
                        <td><?= $receta['receta'] ?></td>
                        <td><?= $receta['descripcion'] ?></td>
                        <td>
                            <!-- Añadimos la opción de crear o eliminar. -->
                            <a href="editar_recetas.php?id=<?= $receta['id'] ?>" class="btn btn-warning btn-sm">Editar</a>
                            <a href="eliminar_recetas.php?id=<?= $receta['id'] ?>" class="btn btn-danger btn-sm" onclick="return confirm('¿Estás seguro de eliminar esta receta?');">Eliminar</a>
                        </td>
                    </tr>
                <?php endforeach; ?>
            </tbody>
        </table>
    </div>
</body>
</html>
