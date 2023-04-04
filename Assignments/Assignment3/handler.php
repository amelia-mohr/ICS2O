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
    $size = "";
    if (isset($_POST["size"])) {
      $size = $_POST["size"];
    }
    $t1 = "";
    if (isset($_POST["t1"])) {
      $t1 = $_POST["t1"];

    }
    $t2 = "";
    if (isset($_POST["t2"])) {
      $t2 = $_POST["t2"];
    }
    $t3 = "";
    if (isset($_POST["t3"])) {
      $t3 = $_POST["t3"];
    }
    $t4 = "";
    if (isset($_POST["t4"])) {
      $t4 = $_POST["t4"];
    }
    $toppings = 
    
    echo $size;
    echo $t1;
    echo $t2;
    echo $t3;
    echo $t4;
    ?>
    
    <div>
      <h1 class="title">Pizza Code</h1>
    </div>
    <center>
      <form action="./index.php" method="post">
        <table>
          <tr>
            <td>
              <div class="options demo-card-square mdl-card mdl-shadow--2dp">
                <div class="mdl-card__title mdl-card--border">
                  <h2 class="mdl-card__title-text h6">What size would you like?</h2>
                </div>
                <div class="mdl-card__supporting-text">
                  <input type="radio" id="l" name="size" value="l">
                  <label for="l" class="choices">Large ($6.00)</label>
                  <br>
                  <input type="radio" id="xl" name="size" value="xl">
                  <label for="xl" class="choices">Extra Large ($10.00)</label>
                </div>
              </div>
            </td>
            <td>
              <div class="options demo-card-square mdl-card mdl-shadow--2dp">
                <div class="mdl-card__title mdl-card--border">
                  <h2 class="mdl-card__title-text h6">What toppings would you like? (Not including cheese)</h2>
                </div>
                <div class="mdl-card__supporting-text">
                  <input type="checkbox" id="t1" name="t1" value="t1">
                  <span for="t1" class="choices">Onions</span>
                  <br>
                  <input type="checkbox" id="t2" name="t2" value="t2">
                  <span for="t2" class="choices">Pepperoni</span>
                  <br>
                  <input type="checkbox" id="t3" name="t3" value="t3">
                  <span for="t3" class="choices">Bacon</span>
                  <br>
                  <input type="checkbox" id="t4" name="t4" value="t4">
                  <span for="t3" class="choices">Onions</span>
                </div>
              </div>
            </td>
            <td>
              <div class="float-child3">
                <img src="./images/6776_Pizza-Dough_ddmfs_4x3_1724-fd91f26e0bd6400a9e89c6866336532b.jpg" style="border-radius: 8px;" width="300px" height="auto" alt="pizza" class="img">
              </div>
            </td>
          </tr>
        </table>
        <button style="font-family: 'Times New Roman', Times, serif;" class="mdl-button mdl-js-button mdl-button--accent">Submit Pizza</button>
      </form>
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
            <li><a href="">Back to Form (HTML) page</a></li>
            <li><a href="">PHP page</a></li>
          </ul>
        </div>

        <div class="mdl-mega-footer__drop-down-section">
          <input class="mdl-mega-footer__heading-checkbox" type="checkbox" checked>
          <h1 class="mdl-mega-footer__heading bottom-title-text">CODE</h1>
          <ul class="mdl-mega-footer__link-list bottom-text">
            <li><a href="">For Form (HTML) page</a></li>
            <li><a href="">For PHP page</a></li>
            <li><a href="">For Python program</a></li>
          </ul>
        </div>
      </div>
    </footer>
  </body>
</html>
