<?php
$puerto = '1234';
$url = "http://localhost:$puerto/v1/chat/completions";  // Asegúrate de que este endpoint coincide con el expuesto por LM Studio.

// 2. Preparar los datos a enviar.
// Creamos un array con la información que queremos enviar al modelo.
// En este ejemplo, enviamos un mensaje (prompt) y configuramos un parámetro como el número máximo de tokens.

$nombre = isset($_POST['nombre']) ? $_POST['nombre'] : 'default';  // Si no se recibe 'nombre', asignamos un valor por defecto.

$datos = array(
    "model"=> "llama-3.2-1b-instruct",
    "messages"=> 
    array(
        array("role"=> "system", "content"=> "Solo escribe la receta, ninguna frase extra"),
        array("role"=> "user", "content"=> "Hazme una receta de '$nombre' pero, no te extiendas demasiado")
    ),
    "temperature"=> 0.7,
    "max_tokens"=> -1,
    "stream"=> false
);


// Convertir el array a formato JSON.
$jsonDatos = json_encode($datos);

// 3. Inicializar cURL para preparar la petición.
$ch = curl_init($url);

// 4. Configurar cURL:
// - Establecemos que usaremos el método POST.
// - Indicamos que la respuesta se guarde en una variable en lugar de mostrarse directamente.
// - Enviamos el cuerpo de la petición con nuestros datos en formato JSON.
curl_setopt($ch, CURLOPT_POST, true);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
curl_setopt($ch, CURLOPT_POSTFIELDS, $jsonDatos);

// 5. Configurar las cabeceras HTTP necesarias.
// Es fundamental indicar que el contenido enviado es de tipo JSON.
curl_setopt($ch, CURLOPT_HTTPHEADER, array(
    'Content-Type: application/json',
    'Content-Length: ' . strlen($jsonDatos)
));

// 6. Ejecutar la petición y capturar la respuesta del servidor.
$respuesta = curl_exec($ch);

// 7. Comprobar si se produjo algún error en la comunicación.
if (curl_errno($ch)) {
    echo 'Error en cURL: ' . curl_error($ch);
} else {
    // Mostrar la respuesta recibida de LM Studio.
    //echo "Respuesta de LM Studio: " . $respuesta;
    // Decodificamos el JSON
    $data = json_decode($respuesta, true);

    // Accedemos al contenido del mensaje
    $message = $data['choices'][0]['message']['content'];
}
curl_close($ch);


// De nuevo creamos la conexion.
$conexion = new mysqli("localhost", "root", "curso", "recetas");
if ($conexion->connect_error) {
    die("Error en la conexión: " . $conexion->connect_error);
}

// Craeamos la clase la cual obtendrá todos los datos anteriores y los meterá en la base de datos para mostrarla
// en el php de recetas

class crearRecetas {
    private $conexion;

    public function __construct($conexion) {
        $this->conexion = $conexion;
    }

    public function crearRecetas($message) { 
        // Le pasaremos el parametro del mensaje que hemos obtenido anteriormente
        // Comprobamos que hayamos obtenido el nombre con post
        if ($_SERVER['REQUEST_METHOD'] == 'POST') {
            $nombre = $_POST['nombre'];

            // Los valores que introducimos son el nombre y el mensaje de Llama.
            $query = "INSERT INTO recetas (receta, descripcion) VALUES ('$nombre', '$message')";
            if ($this->conexion->query($query)) {

                // Así simplemente se recarga la página y vemos los cambios al instante.
                header('location: recetas.php');
                exit();
            } else {
                echo "Error al agregar la receta: " . $this->conexion->error;
            }
        }
    }
}


$receta = new crearRecetas($conexion);
$receta->crearRecetas($message);

?>
