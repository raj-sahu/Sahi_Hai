<?php
header("Access-Control-Allow-Origin: *");

if(isset($_POST['url'])) {
    $site = $_POST['url'];
    $html = file_get_contents($site);
    $bytes = file_put_contents('markup.txt', $html);

    $safeSite = escapeshellarg($site);

    $decision = shell_exec("python test.py $safeSite 2>&1");

    echo $decision;
} else {
    echo "The 'url' parameter is missing in the POST request.";
}
?>
