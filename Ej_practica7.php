<?php
// class persona{
//     public $nombre;
//     public $edad;
//     public $genero;
//     public function presentar(){
//         echo "Hola ". $this -> nombre. ", tienes ". $this ->edad ." años y eres " .$this -> genero;
//     }
// }

// $humano = new persona();
// $humano -> nombre = "Rodrigo Rios";
// $humano -> edad = 18;
// $humano -> genero = "hombre.";
// $humano -> presentar();


// class rectangulo{
//     public $base;
//     public $altura;
//     public function calcularArea(){
//         $area = $this -> base * $this ->altura;
//         echo "\nEl área del rectángulo es ". $area;
//     }
// }
// $area = new rectangulo();
// $area -> base = 10;
// $area -> altura = 5;
// $area ->calcularArea();


// class animal {
//     public $especie;

//     public function emitirSonido() {
//         if ($this->especie == "perro") {
//             echo "Guau guau!";
//         } elseif ($this->especie == "gato") {
//             echo "Miau miau!";
//         } else {
//             echo "Este animal no tiene un sonido definido.";
//         }
//     }
// }
// class perro extends animal{
//     public $raza;
//     public function raza(){
//         echo "Es un ". $this->raza;
//     }
// }
// $perrito = new perro();
// $perrito -> especie = "perro";
// $perrito -> raza = "pastor alemán";
// $perrito -> emitirSonido();
// $perrito -> raza();


// class producto {
//     public $nombre;
//     public $precio;
//     public function mostrarDetalles(){
//         echo "\nEl producto elegido es: ". $this-> nombre . " y tiene un coste de ". $this->precio. "€";
//     }
// }
// class electrodomestico extends producto{
//     public $consumo;
//     public function mostrarDetalles()
//     {
//         echo "\nEste producto cuenta con un consumo de ". $this ->consumo. "W";
//     }
// }
// $electrodomestico = new producto();
// $electrodomestico -> nombre = "Frigorífico";
// $electrodomestico -> precio = 300;
// $electrodomestico -> mostrarDetalles();

// $frigorifico = new electrodomestico();
// $frigorifico -> consumo = 700;
// $frigorifico -> mostrarDetalles();


class conversormoneda {
    public $cantidad;
    public $tipo_cantidad;
        public function convertirDolaresAEuros(){
        if($this->tipo_cantidad == "dolares"){
        $total = $this-> cantidad * 0.98;
        echo $this-> cantidad. " dolares a euros son: " .$total. "€";
    }
    }

    public function convertirEurosADolares(){
        if($this->tipo_cantidad == "euros"){
        $total = $this-> cantidad * 1.02;
        echo $this-> cantidad. " euros a dolares son: " .$total. "$";
    }
}
}
$conversor = new conversormoneda();
$conversor -> cantidad = 1000;
$conversor ->tipo_cantidad = "euros";
$conversor-> convertirDolaresAEuros();
$conversor-> convertirEurosADolares();
?>