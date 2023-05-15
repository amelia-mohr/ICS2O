<!DOCTYPE html>
<html lang="en-ca">
  <head>
    <meta charset="utf-8">
    <meta name="description" content="Assignment #6">
    <meta name="keywords" content="ics2o">
    <meta name="author" content="Amelia M">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="https://fonts.googleapis.com/icon?family=Material+Icons">
    <link rel="stylesheet" href="https://code.getmdl.io/1.3.0/material.teal-pink.min.css">
    <link rel="stylesheet" href="./css/style2.css">
    <link rel="apple-touch-icon" sizes="180x180" href="./images/apple-touch-icon.png">
    <link rel="icon" type="image/png" sizes="32x32" href="./images/favicon-32x32.png">
    <link rel="icon" type="image/png" sizes="16x16" href="./images/favicon-16x16.png">
    <link rel="manifest" href="./images/site.webmanifest">
    <title>Assignment #6</title>
  </head>
  <body>
    <script defer src="https://code.getmdl.io/1.3.0/material.min.js"></script>
    <?php
    $i = "";
    if (isset($_POST["i"])) {
      $i = $_POST["i"];
    }
    settype($i, 'integer');
    $x = 1;
    $z = 1;
    $pi = 0;
    for ($iter = 1; $iter <= $i; $iter++) {
      $pi = $pi + ($z / $x);
      $x = $x + 2;
      $z = $z * -1;
    }
    $pi = $pi * 4;
    settype($pi, 'string');
    ?>
    <div class="header">
      <h1 class="title">Assignment #6!</h1>
    </div>
    <h3 class="h3">The value of PI!</h3>
    <center>
      <div class="demo-card-square mdl-card mdl-shadow--2dp" style="border-radius: 8px;">
        <div class="mdl-card__title mdl-card--border">
          <h6 class="mdl-card__title-text h6">Here is the value of PI with <?=$i?> iteration(s):</h6>
        </div>
        <div class="mdl-card__supporting-text">
          <p class="results">
          PI = <?=$pi?>
          </p>
        </div>
      </div>
    </center>
    <br>
    <br>
    <img src="./images/PI_pic.webp" alt="PI Pic" class="img mdl-shadow--2dp" style="border-radius: 8px;">
    <br>
    <br>
    <footer class="mdl-mega-footer bottom">
      <div class="mdl-mega-footer__middle-section">
        <div class="mdl-mega-footer__drop-down-section">
          <input class="mdl-mega-footer__heading-checkbox" type="checkbox" checked>
          <h1 class="mdl-mega-footer__heading bottom-title-text">ICS2O</h1>
          <ul class="mdl-mega-footer__link-list bottom-text">
            <li>Assignment #6</li>
            <li>Part B</li>
            <li>Amelia Mohr</li>
          </ul>
        </div>

        <div class="mdl-mega-footer__drop-down-section">
          <input class="mdl-mega-footer__heading-checkbox" type="checkbox" checked>
          <h1 class="mdl-mega-footer__heading bottom-title-text">LINKS</h1>
          <ul class="mdl-mega-footer__link-list bottom-text">
            <li><a href="http://amelia.ics2o.ca/ICS2O/Assignments/Assignment6/a6.html">Back to Form (HTML) page</a></li>
            <li><a href="http://amelia.ics2o.ca/ICS2O/Assignments/Assignment6/a6.php">PHP page</a></li>
          </ul>
        </div>

        <div class="mdl-mega-footer__drop-down-section">
          <input class="mdl-mega-footer__heading-checkbox" type="checkbox" checked>
          <h1 class="mdl-mega-footer__heading bottom-title-text">CODE</h1>
          <ul class="mdl-mega-footer__link-list bottom-text">
            <li><a href="https://github.com/amelia-mohr/ICS2O/blob/main/Assignments/Assignment6/a6.html">For Form (HTML) page</a></li>
            <li><a href="https://github.com/amelia-mohr/ICS2O/blob/main/Assignments/Assignment6/a6.php">For PHP page</a></li>
            <li><a href="https://github.com/amelia-mohr/ICS2O/blob/main/Assignments/Assignment6/index.py">For Python program</a></li>
          </ul>
        </div>
      </div>
    </footer>
  </body>
</html>
