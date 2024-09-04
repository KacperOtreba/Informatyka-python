<?php
    $serwer = "localhost";
    $user = "root";
    $password = "";
    $base = "rejestr";

    $connection = new mysqli($serwer,$user, $password, $base);

    // 8.1 
    $zapytanie1 = "SELECT Imie,Nazwisko, SUM(taryfikator.Kwota) FROM kierowcy 
    INNER JOIN rejestr ON kierowcy.IdOsoby = rejestr.IdOsoby 
    INNER JOIN taryfikator ON rejestr.IdWykroczenia = taryfikator.IdWykroczenia
    GROUP BY kierowcy.IdOsoby
    ORDER BY 3 DESC
    LIMIT 1";

    // 8.4
    $zapytanie2 = 
    "SELECT fotoradar.IdFotoradaru 
    FROM fotoradar 
    WHERE fotoradar.IdFotoradaru NOT IN (SELECT DISTINCT rejestr.IdFotoradaru FROM rejestr)";




    $result = $connection->query($zapytanie1);

    while ($row = $result ->fetch_array()) {
        echo $row[0]." ".$row[1]." ".$row[2]."<br>";
    }



    
?>