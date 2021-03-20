// Purpose - This file contains all the logic relevant to the extension such as getting the URL, calling the server
// side clientServer.php which then calls the core logic.

function transfer() {
  // alert("Reached 1");
  var tablink;
  chrome.tabs.getSelected(null, function (tab) {
    tablink = tab.url;
    if(tablink.length > 30) {
      tablink = tablink.slice(0,30) + " ...";
    }
    $("#site").text(tablink);

    var xhr = new XMLHttpRequest();
    params = "url=" + tablink;
    // alert(params);
    var markup =
      "url=" + tablink + "&html=" + document.documentElement.innerHTML;
    xhr.open("POST", "http://localhost:8000", false);
    xhr.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
    // alert("Reached 2");

    // alert(markup);
    xhr.send(markup);
    // alert("Reached 3");
    // Uncomment this line if you see some error on the extension to see the full error message for debugging.
    // alert(xhr.responseText + "Jo_tha_Yahi_tha");
    // alert("Reached 4");

    if(xhr.responseText === "SAFE") {
      $("#div1").text(xhr.responseText);
    }
    else {
      $("#div2").text(xhr.responseText);
    }
    return xhr.responseText;
  });
}

$(document).ready(function () {
  $("button").click(function () {
    // alert("Transfering..");
    var val = transfer();
  });
});

chrome.tabs.getSelected(null, function (tab) {
  var tablink = tab.url;
  if(tablink.length > 30) {
    tablink = tablink.slice(0,30) + " ...";
  }
  $("#site").text( tablink + "\n\n");
});
