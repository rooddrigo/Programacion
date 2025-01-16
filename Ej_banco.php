<?php
class cuenta{

    public $titular;
    public $saldo;
    public $tipoDeCuenta;
    public $cantidad;
    public $operacion;

    public function depositar($cantidad){
        if ($this->operacion =="1"){
        $this -> saldo = $this -> saldo + $cantidad;
        echo "\nSe han ingresado los " .$cantidad. "€ correctamente.\n";
        echo "\nEl saldo total es de ".$this->saldo. "€\n";
        }
    }
    public function retirar($cantidad){
        if ($this->operacion =="2"){
        if ($this->saldo >= $cantidad){
        $this ->saldo = $this -> saldo - $cantidad;
        echo "\nSe han retirado los " .$cantidad. "€ correctamente.\n";
        echo "\nEl saldo total es de ".$this->saldo. "€\n";
        } else {
            echo "No es posible retirar esa cantidad.\n";
        }
    }
    }
    public function mostrarInfo(){
        if ($this->operacion =="3"){
        echo "Titular: ". $this->titular;
        echo "\nSaldo: ". $this->saldo. "€";
        echo "\nTipo de cuenta: ". $this->tipoDeCuenta."\n";
    }
    }
}


$cuenta = new cuenta();
$cuenta->titular = readline("Introduzca su nombre y apellidos: ");
$cuenta->saldo = readline("Introduce un saldo: ");
$cuenta->tipoDeCuenta = "Ahorros";
do {
    $cuenta->operacion = readline("Introduzca '1 - depositar', '2 - retirar', '3 - info' o 'fin' para terminar: ");
    if ($cuenta->operacion == "1" || $cuenta->operacion == "2"){ //para que al depositar o retirar me pida cantidad y al pulsar info, no lo haga.
        $cantidad = readline("\nIntroduce la cantidad deseada: ");
        $cuenta->depositar($cantidad);
        $cuenta->retirar($cantidad);
    } elseif ($cuenta->operacion =="3"){
        $cuenta->mostrarInfo();

    } 
} while($cuenta->operacion <> "fin");
echo "Cerrando programa, Hasta la vista."
?> 