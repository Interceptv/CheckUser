<?php $media = $_POST['username'];
      $media1 = $_POST['deviceid'];
      $json = file_get_contents("$media");
     $decodificado = json_decode ($json);

if (!$decodificado) {
    die('JSON invalido');
}

     
$decodificado->DEVICE= $media1;

$codificado = json_encode($decodificado);

 echo $codificado; ?>