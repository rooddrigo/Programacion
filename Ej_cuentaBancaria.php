<?php
class CuentaBancaria{
    private $titular;
    private $saldo;
    private $tipoCuenta;
    public function __construct($titular,$tipoCuenta)
    {
        $this->titular = $titular;
        $this->saldo = 0;
        $this->tipoCuenta = $tipoCuenta;
    }
    public function depositar($cantidad){
        $this->saldo += $cantidad;
        echo "Se ha ingresado correctamente la cantidad de: ".$cantidad."€\n";
    }
    public function retirar($cantidad){
        if ($this->verificarSaldoSuficiente($cantidad)){
            $this->saldo -= $cantidad;
            echo "Se ha retirado correctamente la cantidad de: ".$cantidad."€\n";
        } else {
            echo "No se puede retirar ese dinero, tendrás que ingresar primero, RATA...";
        }
    }
    private function verificarSaldoSuficiente($cantidad) {
        return $this->saldo >= $cantidad; 
    }
    public function mostrarInfo(){
        echo "\nTitular: ".$this->titular;
        echo "\nSaldo: ".$this->saldo;
        echo "\nTipo de Cuenta: ".$this->tipoCuenta."\n";
    }
}

$cuenta = new CuentaBancaria($titular = readline("Introduzca su nombre y apellidos: "),$tipoDeCuenta = readline("Introduzca el tipo de cuenta deseada: "));
do {
    $operacion = readline("\nIntroduzca '1 - depositar', '2 - retirar', '3 - info' o 'fin' para terminar: ");
    if ($operacion == "1"){     
        $cantidad = readline("\nIntroduce la cantidad deseada: ");
        $cuenta->depositar($cantidad);
    }elseif($operacion == "2"){
        $cantidad = readline("\nIntroduce la cantidad deseada: ");
        $cuenta->retirar($cantidad);
    } elseif ($operacion =="3"){
        $cuenta->mostrarInfo();

    } 
} while($operacion <> "fin");
echo "Cerrando programa, Hasta la vista."


?>