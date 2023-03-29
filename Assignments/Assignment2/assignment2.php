<!DOCTYPE html>
<html lang="en-ca">
  <head>
    <meta charset="utf-8">
    <meta name="description" content="Assignment #2">
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
    <title>Assignment #2</title>
  </head>
  <body>
    <script defer src="https://code.getmdl.io/1.3.0/material.min.js"></script>
    <?php
    $d = "";
    if (isset($_POST["d"])) {
      $d = $_POST["d"];
    }
    $u = "";
    if (isset($_POST["u"])) {
      $u = $_POST["u"];
    }
    settype($d, 'float');
    $r = round($d / 2, 2);
    settype($r, 'float');
    $a = round(pi() * ($r ** 2), 2);
    $c = round(2 * pi() * $r, 2);
    settype($u, 'string');
    settype($d, 'string');
    settype($r, 'string');
    settype($a, 'string');
    settype($c, 'string');
    ?>

    <div class="header">
      <h1 class="title">Assignment #2!</h1>
    </div>
    <h3 class="h3">The area and circumference of a circle!</h3>
    <center>
      <div class="demo-card-square mdl-card mdl-shadow--2dp">
        <div class="mdl-card__title mdl-card--border">
          <h6 class="mdl-card__title-text h6">All results (except for the diameter) are rounded to 2 decimal places.</h6>
        </div>
        <div class="mdl-card__supporting-text">
          <p class="results">
          The diameter of your circle is: <?=$d, " ", $u?>
          <br>
          The radius of your circle is: <?=$r, " ", $u?>
          <br>
          The area of your circle is: <?=$a, " ", $u?><sup>2</sup>
          <br>
          And the circumference of your circle is: <?=$c, " ", $u?>
          </p>
        </div>
      </div>
    </center>
    <br>
    <br>
    <img src="./images/circle.png" alt="Circle Image" class="img">
    <br>
    <br>
    <footer class="mdl-mega-footer bottom">
      <div class="mdl-mega-footer__middle-section">
        <div class="mdl-mega-footer__drop-down-section">
          <input class="mdl-mega-footer__heading-checkbox" type="checkbox" checked>
          <h1 class="mdl-mega-footer__heading bottom-title-text">ICS2O</h1>
          <ul class="mdl-mega-footer__link-list bottom-text">
            <li>Assignment #2</li>
            <li>Part B</li>
            <li>Amelia Mohr</li>
          </ul>
        </div>

        <div class="mdl-mega-footer__drop-down-section">
          <input class="mdl-mega-footer__heading-checkbox" type="checkbox" checked>
          <h1 class="mdl-mega-footer__heading bottom-title-text">LINKS</h1>
          <ul class="mdl-mega-footer__link-list bottom-text">
            <li><a href="http://amelia.ics2o.ca/ICS2O/Assignments/Assignment2/assignment2.html">Back to Form (HTML) page</a></li>
            <li><a href="http://amelia.ics2o.ca/ICS2O/Assignments/Assignment2/index.html">What PHP page should look like (in an HTML file)</a></li>
            <li><a href="http://amelia.ics2o.ca/ICS2O/Assignments/Assignment2/assignment2.php">Actual PHP page</a></li>
          </ul>
        </div>

        <div class="mdl-mega-footer__drop-down-section">
          <input class="mdl-mega-footer__heading-checkbox" type="checkbox" checked>
          <h1 class="mdl-mega-footer__heading bottom-title-text">CODE</h1>
          <ul class="mdl-mega-footer__link-list bottom-text">
            <li><a href="https://github.com/amelia-mohr/ICS2O/blob/main/Assignments/Assignment2/assignment2.html">For Form (HTML) page</a></li>
            <li><a href="https://github.com/amelia-mohr/ICS2O/blob/main/Assignments/Assignment2/assignment2.php">For PHP page</a></li>
            <li><a href="https://github.com/amelia-mohr/ICS2O/blob/main/Assignments/Assignment2/assignment2.py">For Python program</a></li>
          </ul>
        </div>
      </div>
    </footer>
  </body>
</html>
