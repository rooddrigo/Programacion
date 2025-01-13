<?php
class libro{
    public $titulo;
    public $paginas;
    public $autor;

    public function mostrarinfo(){
        echo "\nEl libro es ". $this->titulo. ", tiene ". $this->paginas. " páginas y lo escribió ". $this->autor;
    }
}

$libroprueba = new libro;
$libroprueba->titulo = "Entiende la tecnología";
$libroprueba->paginas = 376;
$libroprueba->autor = "Nate Gentile";
$libroprueba->mostrarinfo();
?>