<?php
class Usuario{
    private $nombre;
    private $email;

    public function __construct($nombre,$email){
        $this->nombre = $nombre;
        $this->email = $email;
    }
    public function mostrarInfo(){
        echo "\nNombre: ".$this->nombre;
        echo "\nCorreo: ".$this->email;
    }
}
class Administrador extends Usuario{
    private $nivelAcceso;

    public function __construct($nombre,$email,$nivelAcceso){
        parent::__construct($nombre,$email);
        $this->nivelAcceso = $nivelAcceso;
    }
    public function mostrarInfo()
    {
        parent::mostrarInfo();
        echo "\nSu nivel de acceso es: ".$this->nivelAcceso;
    }
}
$usuario = new Administrador(readline("Introduce tu nombre: "), readline("Introduce tu correo: "), random_int(1,5));
$usuario -> mostrarInfo();
?>