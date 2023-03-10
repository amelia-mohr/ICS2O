<!DOCTYPE html>
<html lang="en-ca">
    <head>
        <meta charset="utf-8">
        <meta name="description" content="Assignment #2">
        <meta name="keywords" content="isc2o">
        <meta name="author" content="Amelia M">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link rel="stylesheet" href="https://fonts.googleapis.com/icon?family=Material+Icons">
        <link rel="stylesheet" href="https://code.getmdl.io/1.3.0/material.teal-pink.min.css">
        <link rel="apple-touch-icon" sizes="180x180" href="./images/apple-touch-icon.png">
        <link rel="icon" type="image/png" sizes="32x32" href="./images/favicon-32x32.png">
        <link rel="icon" type="image/png" sizes="16x16" href="./images/favicon-16x16.png">
        <link rel="manifest" href="./images/site.webmanifest">
        <title>Assignment #2</title>
    </head>
    <body>
        <script defer src="https://code.getmdl.io/1.3.0/material.min.js"></script>
        <?php
        $d = "";
        if (isset($_POST["d"])) {
            $d = $_POST["d"];
        }
        settype($d, 'integer');
        $r = $d / 2;
        settype($r, 'float');
        $a = round(pi() * ($r ** 2), 2);
        $c = round(2 * pi() * $r, 2);
        settype($a, 'float');
        settype($c, 'float');
        ?>
        
        <h1>Assignment #2!</h1>
        <h3>The area and circumference of a circle!</h3>
        <h5>The area and circumference are rounded to 2 decimal places.</h5>
        <p>The diameter of your circle is: <?=$d?></p>
        <p>The radius of your circle is: <?=$r?></p>
        <p>The area of your circle is: <?=$a?></p>
        <p>And the circumference of your circle is: <?=$c?></p>
    </body>
</html>
