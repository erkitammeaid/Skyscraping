<?php
$servername = "d98711.mysql.zonevs.eu";
$username = "d98711_scraper";
$password = "2021projekt";


try {
    $conn = new PDO("mysql:host=$servername;dbname=d98711_skyscraper", $username, $password);
    // set the PDO error mode to exception
    $conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
    $sql = "INSERT INTO user (username, email, password, url, price)
    VALUES ('Madis', 'madis@gmail.com', 'ametikool', 'https://laane.barbora.ee/toode/kohvioad-qualita-rossa-lavazza-1-kg', '18')";
    // use exec() because no results are returned
    $conn->exec($sql);
    echo "New record created successfully";
  } catch(PDOException $e) {
    echo $sql . "<br>" . $e->getMessage();
  }
  
  $conn = null;
?>