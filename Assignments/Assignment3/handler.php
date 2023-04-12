<!DOCTYPE html>
<html lang="en-ca">
  <head>
    <meta charset="utf-8">
    <meta name="description" content="Assignment #3">
    <meta name="keywords" content="ics2o">
    <meta name="author" content="Amelia M">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="./css/style.css">
    <link rel="stylesheet" href="https://fonts.googleapis.com/icon?family=Material+Icons">
    <link rel="stylesheet" href="https://code.getmdl.io/1.3.0/material.teal-pink.min.css">
    <link rel="apple-touch-icon" sizes="180x180" href="./images/apple-touch-icon.png">
    <link rel="icon" type="image/png" sizes="32x32" href="./images/favicon-32x32.png">
    <link rel="icon" type="image/png" sizes="16x16" href="./images/favicon-16x16.png">
    <link rel="manifest" href="./images/site.webmanifest">
    <title>Assignment #3</title>
  </head>
  <body>
    <script defer src="https://code.getmdl.io/1.3.0/material.min.js"></script>
    <?php
    $size = $_POST["size"];
    $sprices = array(
      "Large" => 6.00,
      "Extra Large" => 10.00
    );
    $psize = $sprices[$size];
    settype($psize, 'float');

    $list = array();
    if (isset($_POST["t1"])) {
      $t1 = "Onions";
      array_push($list, $t1);
    }
    if (isset($_POST["t2"])) {
      $t2 = "Pepperoni";
      array_push($list, $t2);
    }
    if (isset($_POST["t3"])) {
      $t3 = "Bacon";
      array_push($list, $t3);
    }
    if (isset($_POST["t4"])) {
      $t4 = "Olives";
      array_push($list, $t4);
    }
    $number = count($list);
    list($a, $b, $c, $d) = $list;

    $toppings = "";
    if ($number = 0) {
      $toppings = "0.00";
    } elseif ($number = 1) {
      $toppings = "1.00";
    } elseif ($number = 2) {
      $toppings = "1.75";
    } elseif ($number = 3) {
      $toppings = "2.50";
    } elseif ($number = 4) {
      $toppings = "3.35";
    }
    settype($toppings, 'float');
    
    $subtotal = $psize + $toppings;
    settype($subtotal, 'float');
    $tax = round($subtotal * 0.13, 2);
    $total = round($subtotal * 1.13, 2);

    settype($psize,'string');
    settype($toppings,'string');
    settype($number,'string');
    settype($subtotal,'string');
    settype($tax,'string');
    settype($total,'string');
    ?>
    
    <div>
      <h1 class="title">CHECKOUT</h1>
    </div>
    <center>
      <table>
        <tr>
          <td>
            <div class="options demo-card-square mdl-card mdl-shadow--6dp">
              <div class="mdl-card__title mdl-card--border">
                <h2 class="mdl-card__title-text h6">Your Order</h2>
              </div>
              <div class="mdl-card__supporting-text">
                <p class="choices">
                  SIZE: <?=$size?>
                  <br>
                  TOPPINGS: <br>
                  <?=$a?> <br>
                  <?=$b?> <br>
                  <?=$c?> <br>
                  <?=$d?>
                <p>
              </div>
            </div>
          </td>
          <td>
            <div class="options demo-card-square mdl-card mdl-shadow--6dp">
              <div class="mdl-card__title mdl-card--border">
                <h2 class="mdl-card__title-text h6">Cost</h2>
              </div>
              <div class="mdl-card__supporting-text">
                <p class="choices">
                  SIZE: <?=$psize?>
                  <br>
                  TOPPINGS: <?=$toppings?>
                  <br>
                  SUBTOTAL: <?=$subtotal?>
                  <br>
                  TAX: <?=$tax?>
                  <br>
                  TOTAL: <?=$total?>
                <p>
              </div>
            </div>
          </td>
          <td>
            <div class="float-child3">
              <img src="./images/6776_Pizza-Dough_ddmfs_4x3_1724-fd91f26e0bd6400a9e89c6866336532b.jpg" style="border-radius: 8px;" width="300px" height="auto" alt="pizza" class="img mdl-shadow--6dp">
            </div>
          </td>
        </tr>
      </table>
      <center>
        <p class="message">
          Thank you for ordering from
          <br>
          Pizza Code!
        </p>
      </center>
    </center>
    <br>
    <footer style="background-color: #00695e;" class="mdl-mega-footer">
      <div class="mdl-mega-footer__middle-section">
        <div class="mdl-mega-footer__drop-down-section">
          <input class="mdl-mega-footer__heading-checkbox" type="checkbox" checked>
          <h1 class="mdl-mega-footer__heading bottom-title-text">ICS2O</h1>
          <ul class="mdl-mega-footer__link-list bottom-text">
            <li>Assignment #3</li>
            <li>Part B</li>
            <li>Amelia Mohr</li>
          </ul>
        </div>

        <div class="mdl-mega-footer__drop-down-section">
          <input class="mdl-mega-footer__heading-checkbox" type="checkbox" checked>
          <h1 class="mdl-mega-footer__heading bottom-title-text">LINKS</h1>
          <ul class="mdl-mega-footer__link-list bottom-text">
            <li><a href="./assignment3.html">Back to Form (HTML) page</a></li>
            <li><a href="./handler.php">PHP page</a></li>
          </ul>
        </div>

        <div class="mdl-mega-footer__drop-down-section">
          <input class="mdl-mega-footer__heading-checkbox" type="checkbox" checked>
          <h1 class="mdl-mega-footer__heading bottom-title-text">CODE</h1>
          <ul class="mdl-mega-footer__link-list bottom-text">
            <li><a href="https://github.com/amelia-mohr/ICS2O/blob/main/Assignments/Assignment3/assignment3.html">For Form (HTML) page</a></li>
            <li><a href="https://github.com/amelia-mohr/ICS2O/blob/main/Assignments/Assignment3/handler.php">For PHP page</a></li>
            <li><a href="https://github.com/amelia-mohr/ICS2O/blob/main/Assignments/Assignment3/assignment3.py">For Python program</a></li>
          </ul>
        </div>
      </div>
    </footer>
  </body>
</html>
