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



}



?>