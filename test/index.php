<?php
header("Access-Control-Allow-Origin: *");
$site=$_POST['url'];
// $site="https://www.york.ac.uk/teaching/cws/wws/webpage1.html";
// $site="http://phishtank.org/";
$html = file_get_contents($site);
$bytes=file_put_contents('markup.txt', $html);
$decision=exec("python test.py $site 2>&1 ");
echo $decision;
?>