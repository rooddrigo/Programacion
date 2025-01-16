<?php
class Personaje {
    public $nombre;
    public $nivel;
    public $puntosVida;
    public $puntosAtaque;

    public function __construct($nombre, $nivel, $puntosVida, $puntosAtaque) {
        $this->nombre = $nombre;
        $this->nivel = $nivel;
        $this->puntosVida = $puntosVida;
        $this->puntosAtaque = $puntosAtaque;
    }

    public function mostrarVidaInicial() {
        echo "\nVida inicial de " . $this->nombre . ": " . $this->puntosVida;
        echo "\nNivel inicial de " . $this->nombre . ": " . $this->nivel . "\n";
    }
    public function atacar(Personaje $objetivo) {
        $objetivo->puntosVida -= $this->puntosAtaque;
        $objetivo->puntosVida = max(0, $objetivo->puntosVida); // max para que nunca sea menor que cero.

        echo "\nEl objetivo era: " . $objetivo->nombre . " y ha recibido un ataque de " . $this->puntosAtaque . ". Su vida restante es de " . $objetivo->puntosVida."\n";

        if ($objetivo->puntosVida <= 0) {
            echo "\n" . $objetivo->nombre . " ha sido derrotado.";
        }
    }

    public function curarse() {
        if ($this->puntosVida > 0) {
            $this->puntosVida += 1;
            echo "\nEl personaje " . $this->nombre . " ha recibido 1 punto de vida, su vida restante es de: " . $this->puntosVida."\n";
        }
    }

    public function subirNivel() {
        $this->nivel += 1;
        echo "\nEl personaje " . $this->nombre . " ha subido 1 nivel, su nivel actual es: " . $this->nivel."\n";
    }
}

$personaje1 = new Personaje("Pepe", random_int(1, 10), random_int(1, 10), random_int(1, 5));
$personaje2 = new Personaje("Manolo", random_int(1, 10), random_int(1, 10), random_int(1, 5));
$personaje3 = new Personaje("Epifanio", random_int(1, 10), random_int(1, 10), random_int(1, 5));

$lista_personajes = [$personaje1, $personaje2, $personaje3];

$personaje1->mostrarVidaInicial();
$personaje2->mostrarVidaInicial();
$personaje3->mostrarVidaInicial();

while (true) {
    $seleccion_random = $lista_personajes[array_rand($lista_personajes)];
    if ($seleccion_random->puntosVida <= 0) {
        continue; // por si no tienen vida que no ataquen una ultima vez, que se lo salte para que pueda termibar el juego.
    }
        do {
        $objetivo_random = $lista_personajes[array_rand($lista_personajes)]; //para que no me seleccione el mismo objetivo que el atacante
        } while ($seleccion_random === $objetivo_random || $objetivo_random->puntosVida <= 0);
            $seleccion_random->atacar($objetivo_random);
        if ($objetivo_random->puntosVida <= 0) {
            echo " El juego se ha terminado";
            break; 
        }
        $seleccion_random->curarse();
        $seleccion_random->subirNivel();
}
?>
