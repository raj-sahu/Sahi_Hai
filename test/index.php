<?php
header("Access-Control-Allow-Origin: *");
$site=$_POST['url'];
$html = file_get_contents($site);
$bytes=file_put_contents('markup.txt', $html);
$decision=exec("python test.py $site 2>&1 ");
echo $decision;
?>