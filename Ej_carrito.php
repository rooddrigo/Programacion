<?php
class Carrito {
    public $productos = []; 

    public function agregarProducto($nombre, $precio, $cantidad) {
        $this->productos[] = [
            "nombre" => $nombre,
            "precio" => $precio,
            "cantidad" => $cantidad
        ];
    }
    public function quitarProducto($nombre) {
        foreach ($this->productos as $key => $producto) {
            if ($producto["nombre"] == $nombre) {
                unset($this->productos[$key]);
                echo "Se ha eliminado el producto " . $nombre . " correctamente.\n";
                return;
            }
        }
        echo "El producto '$nombre' no se encuentra en el carrito.\n";
    }
    public function calcularTotal() {
        $total = 0;
        foreach ($this->productos as $producto) {
            $total += $producto["precio"] * $producto["cantidad"]; 
        }
        return $total;
    }
    public function mostrarDetalleCarrito() {
        echo "\nDetalle del carrito:\n";
        foreach ($this->productos as $producto) {
            echo "Producto: " . $producto["nombre"] . ", Precio: " . $producto["precio"] . "€, Cantidad: " . $producto["cantidad"] . ", Total: " . ($producto["precio"] * $producto["cantidad"]) . "€\n";
        }
    }
}

$carrito = new Carrito();
$carrito->agregarProducto("Teclado", 50, 2);
$carrito->agregarProducto("Monitor", 200, 3);
$carrito->agregarProducto("Ratón", 30, 1);
$carrito->mostrarDetalleCarrito();
echo "Total de la compra: " . $carrito->calcularTotal() . "€\n\n";
$carrito->quitarProducto("Monitor");
$carrito->mostrarDetalleCarrito();
echo "Nuevo total de la compra: " . $carrito->calcularTotal() . "€\n";
?>
