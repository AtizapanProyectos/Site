


<?php
require_once('fpdf/fpdf.php');
require 'phpqrcode/qrlib.php';


// Conexión a la base de datos
$conn = new mysqli("localhost", "root", "", "dbsite");
$conn->set_charset("utf8");

// Establecer la configuración regional para México, Ciudad de México
setlocale(LC_TIME, 'es_MX.utf8', 'es_MX', 'Spanish_Mexico');

// Obtiene la fecha actual en formato español de México, Ciudad de México
$fechaHoy = strftime('%d de %B de %Y'); // %d: día, %B: mes completo, %Y: año

// Crear un nuevo documento PDF
$pdf = new FPDF();

// Agregar una página en blanco
$pdf->AddPage();

// Establecer el tamaño y tipo de fuente
$pdf->SetFont('Arial', '', 9);

// Obtener la fecha actual en el formato deseado
$fecha_actual = date("d, F Y");

// Consulta SQL
$sql = "SELECT c.id_cand,
               (SELECT p.descrip FROM procesos p WHERE p.idProceso = c.idProceso) AS proceso,
               (SELECT pr.descrip_princ FROM principio pr WHERE pr.idprinc = c.idprincipio) AS principio,
               (SELECT tc.descrip_tcargo FROM tipocargo tc WHERE tc.idtipo_cargo = c.idtipo_cargo) AS tipo_cargo,
               (SELECT d.nombredistrito FROM distritos d WHERE d.idDistrito = c.idDistrito) AS distrito,
               (SELECT m.nombre_mpo FROM municipios m WHERE m.idMunicipio = c.idMunicipio) AS municipio,
               (SELECT e.nombre_edo FROM estados e WHERE e.idEstado = c.idEstado) AS estado_nacimiento,
               c.idPartido,
               c.idEstado_nacimiento,
               c.nombres,
               c.apaterno,
               c.amaterno,
               c.apodo,
               c.genero,
               c.fecha_nac,
               c.tel,
               c.domicilio,
               c.tiempo_res,
               c.ocupacion,
               c.reeleccion,
               c.anos_cons,
               c.grup_vul,
               c.grup_vulne,
               c.Correo,
               c.clave_elect,
               c.CIC,
               c.OCR,
               c.num_emicion
        FROM candidatos c
        WHERE c.Centinela = 1";
$result = $conn->query($sql);

// Agregar encabezado con alineación a la derecha
$sql4 = "SELECT p.descrip FROM procesos p INNER JOIN candidatos c ON p.idProceso = c.idProceso WHERE c.Centinela = 1 LIMIT 1;";
$result4 = $conn->query($sql4); // ejecuta la consulta sql

// Consulta OPLE SQL
$sql2 = "SELECT Siglas, Nombre_completo, Logo FROM oples WHERE idOple=1;";
$result2 = $conn->query($sql2); // ejecuta la consulta sql

// Consulta OPLE SQL
$sql3 = "SELECT tc.idtipoc AS tipo_cargo, p.partido, p.desc_partido FROM candidatos c LEFT JOIN tipocargo tc ON c.idtipo_cargo = tc.idtipo_cargo LEFT JOIN partidos p ON c.idPartido = p.idPartido WHERE c.Centinela = 1;";
$result3 = $conn->query($sql3); // ejecuta la consulta sql




if ($result2->num_rows > 0) {    
  
    $pdf->SetFont('Arial', 'B', 10);

    // Datos de la tabla obtenidos de la consulta
    while ($row = $result2->fetch_assoc()) {
        $Siglas = isset($row['Siglas']) ? $row['Siglas'] : '';
        $Nombre_completo = isset($row['Nombre_completo']) ? $row['Nombre_completo'] : '';
        $Logo = isset($row['Logo']) ? $row['Logo'] : '';

    }

    // Datos de la tabla obtenidos de la consulta
    while ($row = $result4->fetch_assoc()) {
        $eleccion = isset($row['descrip']) ? $row['descrip'] : '';
    }

    $pdf->Image($Logo, 10, 10, 40, 0, 'PNG'); // Logo en la esquina superior izquierda

    $pdf->Ln(4);
    // Agregar el título en el encabezado
    $pdf->SetFont('Arial', '', 13);
    $pdf->SetTextColor(0); // Texto en color negro
    $pdf->Cell(0, 5, utf8_decode ($Nombre_completo) , 0, 1, 'C');
    $pdf->Cell(0, 5, utf8_decode($eleccion), 0, 1, 'C');
    $pdf->Cell(0, 5, ('Reporte Individual de Candidato'), 0, 1, 'C');
} else {
    // Si no se encontraron resultados, se puede imprimir un mensaje o hacer algo más.
    // Establecer color de texto negro para el mensaje
    $pdf->SetTextColor(0); // Negro
    $pdf->Cell(0, 10, 'No se encontraron resultados', 0, 1, 'C');
}

// Agregar la fecha de impresión
$pdf->SetFont('Arial', '', 9);

$pdf->Cell(0, 14, utf8_decode('Fecha: '. $fechaHoy), 0, 1, 'R');
$pdf->Ln(15);
$pdf->SetFont('Arial', '', 10);


//poner qr 

$dir = 'temp/';

if (!file_exists($dir)) {
    mkdir($dir);
}
//hora y fecha usuario captura

$sqlx = "SELECT fecha_De_captura FROM candidatos WHERE Centinela=1;";
$resultx = $conn->query($sqlx); // ejecuta la consulta sql





// Verificar si se obtuvieron resultados
if ($result->num_rows > 0) {
    // Agregar el cuerpo del documento
    while ($row = $result->fetch_assoc()) {
        $proceso = isset($row['proceso']) ? $row['proceso'] : '';
        $genes= isset($row['genero']) ? $row['genero'] : '';





        while ($row2 = $result3->fetch_assoc()) {
            $partido = isset($row2['partido']) ? $row2['partido'] : '';
            $tipocargo = isset($row2['tipo_cargo']) ? $row2['tipo_cargo'] : '';
            $nombrepartido = isset($row2['desc_partido']) ? $row2['desc_partido'] : '';
    
            if ($tipocargo == 'GU') {
                $pdf->SetX(15);
                $pdf->MultiCell(0, 5, utf8_decode("Por medio del presente se da por recibido el registro del Candidato para la elección: " . $proceso ." para el cargo: " . $row["tipo_cargo"] . " del Estado: " . $row["estado_nacimiento"] . " por parte del partido: " . $row2["desc_partido"] . " (" . $row2["partido"] . "). "), 0, 'J');
                $pdf->Ln();
            }
            else if ($tipocargo == 'AY') {
                $pdf->SetX(15);
                $pdf->MultiCell(0, 5, utf8_decode("Por medio del presente se da por recibido la captura del Candidato para la elección: " . $proceso . " para el cargo: " . $row["tipo_cargo"] . " del Estado: " . $row["estado_nacimiento"] . " del Municipio: " . $row["municipio"] . " por parte del partido: " . $row2["desc_partido"] . " (" . $row2["partido"] . "). "), 0, 'J');
                $pdf->Ln();
            
            

            } else if ($tipocargo == 'CO') {
                $pdf->SetX(15);
                $pdf-> MultiCell(0, 5, utf8_decode("Por medio del presente se da por recibido el registro del Candidato para la elección: " . $proceso . " para el cargo: " . $row["tipo_cargo"] . " del Estado: " . $row["estado_nacimiento"] . " del Municipio: " . $row["municipio"] . " del Distrito: " . $row["distrito"] . "por parte del partido: " . $row2["desc_partido"] . " (" . $row2["partido"] . "). "), 0, 'J');
            $pdf->Ln();
            
            
            }
        }
        $pdf->Ln(2);
        $pdf->SetFont('Arial', 'B', 12);
        $pdf->Cell(5);
        $pdf->Cell(0, 10, utf8_decode(""), 0, 1, 'L');
        $pdf->Ln(4);
        while ($rowx = $resultx->fetch_assoc()) {
            $pdf->SetFont('Arial', '', 10);
           
$fechaCaptura = date("d/m/Y H:i:s", strtotime($rowx["fecha_De_captura"]));
$pdf->Cell(10);
$pdf->Cell(0, 5, utf8_decode("Fecha de registro: " . $fechaCaptura), 0, 1, 'L');

                
        }
        $pdf->SetFont('Arial', '', 10);
        



         
        
        $pdf->Cell(10);
        $pdf->Cell(0, 7, utf8_decode("Nombre Completo: " . $row["nombres"] . " " . $row["apaterno"] . " " . $row["amaterno"]), 0, 1, 'L');
        $pdf->Cell(10);
        $pdf->Cell(0, 7, utf8_decode("Sobrenombre: " . $row["apodo"]), 0, 1, 'L');
        if ($row["genero"] == 'X') {
            $pdf->Cell(10);
            $pdf->Cell(0, 7, utf8_decode("Género: No binario"), 0, 1, 'L');
        } elseif ($row["genero"] == 'H') {
            $pdf->Cell(10);
            $pdf->Cell(0, 7, utf8_decode("Género: Hombre"), 0, 1, 'L');
        } elseif ($row["genero"] == 'M') {
            $pdf->Cell(10);
            $pdf->Cell(0, 7, utf8_decode("Género: Mujer"), 0, 1, 'L');
        }
        
        $pdf->Cell(10);
        $pdf->Cell(0, 7, utf8_decode("Fecha de nacimiento: " . $row["fecha_nac"]), 0, 1, 'L');
        $pdf->Cell(10);
        $pdf->Cell(0, 7, utf8_decode("Número Telefónico: " . $row["tel"]), 0, 1, 'L');
        $pdf->Cell(10);
        $pdf->Cell(0, 7, utf8_decode("Ocupación: " . $row["ocupacion"]), 0, 1, 'L');
        $pdf->Cell(10);
        $pdf->Cell(0, 7, utf8_decode("Domicilio: " . $row["domicilio"]), 0, 1, 'L');
        $pdf->Cell(10);
        $pdf->Cell(0, 7, utf8_decode("Tiempo de Residencia: " . $row["tiempo_res"]), 0, 1, 'L');
        $pdf->Cell(10);
        $pdf->Cell(0, 7, utf8_decode("Grupo Vulnerable: " . $row["grup_vulne"]), 0, 1, 'L');
        $pdf->Cell(10);
        $pdf->Cell(0, 7, utf8_decode("Correo Electrónico: " . $row["Correo"]), 0, 1, 'L');
        $pdf->Cell(10);
        $pdf->Ln(4);
        $pdf->SetFont('Arial', 'B', 12);
        $pdf->Cell(5);
        $pdf->Cell(0, 7, utf8_decode("Datos Electorales:"), 0, 1, 'L');
        $pdf->SetFont('Arial', '', 10);
        $pdf->Ln(4);
        $pdf->Cell(10);
        $pdf->Cell(0, 7, utf8_decode("Clave Electoral: " . $row["clave_elect"]), 0, 1, 'L');
        $pdf->Cell(10);
        $pdf->Cell(0, 7, utf8_decode("CIC: " . $row["CIC"]), 0, 1, 'L');
        $pdf->Cell(10);
        $pdf->Cell(0, 7, utf8_decode("OCR: " . $row["OCR"]), 0, 1, 'L');
        $pdf->Cell(10);
        $pdf->Cell(0, 10, utf8_decode("Número de Emisión: " . $row["num_emicion"]), 0, 1, 'L');
        $pdf->Cell(10);



$prueba2='ESTO ESS';
$filename = $dir . 'test.png';
$tamanio = 8;
$level = 'H';
$frameSize = 3;
$Contenido = $row["nombres"]." ".$row["apaterno"] . " " .$row["amaterno"]." ".$row["clave_elect"]." SEGURO✅";

QRcode::png($Contenido, $filename, $level, $tamanio, $frameSize);

  // Agregar el código QR al centro y alineado a la derecha
  $qrWidth = 32; // Ancho de la imagen del código QR
  $pageWidth = $pdf->GetPageWidth(); // Ancho de la página
  $qrX = $pageWidth - $qrWidth - 86; // Coordenada X para alineación a la derecha
  
  $pdf->Image($filename, $qrX, 262, $qrWidth, 0, 'PNG'); 









        $pdf->Ln(2);
    }






} else {
    // Si no se encontraron resultados, se puede imprimir un mensaje o hacer algo más.
    echo "No se encontraron resultados";
}



// Consulta OPLE SQL
$sql5 = "SELECT dc.idtipo_doc, dc.Estatus, Estatus_revición FROM documentos_candidatos dc INNER JOIN candidatos c ON dc.id_cand = c.id_cand WHERE c.Centinela = 1;";
$result5 = $conn->query($sql5); // ejecuta la consulta sql
if ($result5->num_rows > 0) {  
     
    $pdf->SetFont('Arial', 'B', 12);
    $pdf->Cell(5);
    $pdf->Cell(0, 7, utf8_decode("Documentos del Candidato: "), 0, 1, 'L');
    $pdf->Ln(4);

    $pdf->SetFont('Arial', '', 10);

    // Datos de la tabla obtenidos de la consulta
    while ($row = $result5->fetch_assoc()) {

        $doc= isset($row['idtipo_doc']) ? $row['idtipo_doc'] : '';
        $estatus = isset($row['Estatus']) ? $row['Estatus'] : '';
        $estatusople = isset($row['Estatus_revición']) ? $row['Estatus_revición']:'';
        $pdf->Cell(10);

        if($estatusople=='APROBADO'){
            $pdf->Cell(0, 7, utf8_decode($doc." (".$estatus.") : APROBADO"), 0, 1, 'L');
        }else if($estatusople==null){
            $pdf->Cell(0, 7, utf8_decode($doc." (".$estatus.") : POR REVISAR"), 0, 1, 'L');
        }else {
            $pdf->Cell(0, 7, utf8_decode($doc." (".$estatus.") : EN REVICIÓN"), 0, 1, 'L');
        }
        



    }

} else {
    // Si no se encontraron resultados, se puede imprimir un mensaje o hacer algo más.
    // Establecer color de texto negro para el mensaje
    $pdf->SetTextColor(0); // Negro
    $pdf->Cell(0, 10, 'No se encontraron resultados', 0, 1, 'C');
}

















 $pdf->Output('listado_candidatos.pdf', 'I');

// Cerrar la conexión a la base de datos
$conn->close();
?>








