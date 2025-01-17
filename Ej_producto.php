<?php
class Producto{
    private $nombre;
    private $precio;
    private $cantidad;
    public function __construct($nombre2,$precio2,$cantidad2){
        $this->nombre = $nombre2;
        $this->precio = $precio2;
        $this->cantidad = $cantidad2;
    }
    public function getNombre(){
        return $this->nombre;
    }
    public function getPrecio(){
        return $this->precio;
    }
    public function getCantidad(){
        return $this->cantidad;
    }
} 

class ProductoImportado extends producto{
    private $impuestoAdicional;

    public function __construct($nombre2,$precio2,$cantidad2,$impuestoAdicional2){
        parent::__construct($nombre2,$precio2,$cantidad2);
        $this->impuestoAdicional = $impuestoAdicional2;
    }
    public function calcularPreciofinal(){
        $precioSinImpuestos = parent::getPrecio() * parent::getCantidad();
        $precio_final = $precioSinImpuestos * (1+$this->impuestoAdicional/100);
        echo "Has elegido ".parent::getNombre(). ". Su precio sin impuestos es de: ".$precioSinImpuestos."\n";
        echo "\nY su precio final es: ".$precio_final. "€";

    }
}

$productoImportado = new ProductoImportado("Papel",1.20,20,21);
$productoImportado -> calcularPreciofinal();
?>