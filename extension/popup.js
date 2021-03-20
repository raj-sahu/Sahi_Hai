function transfer() {
  var tablink;
  chrome.tabs.getSelected(null, function (tab) {
    tablink = tab.url;
    if (tablink.length > 30) {
      tablink = tablink.slice(0, 30) + " ...";
    }
    $("#site").text(tablink);

    var xhr = new XMLHttpRequest();
    params = "url=" + tablink;
    var markup =
      "url=" + tablink + "&html=" + document.documentElement.innerHTML;
    xhr.open("POST", "http://localhost:8000", false);
    xhr.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
    xhr.send(markup);
    if (xhr.responseText === "SAFE") {
      $("#div1").text(xhr.responseText);
    } else {
      $("#div2").text(xhr.responseText);
    }
    return xhr.responseText;
  });
}

$(document).ready(function () {
  $("button").click(function () {
    var val = transfer();
  });
});

chrome.tabs.getSelected(null, function (tab) {
  var tablink = tab.url;
  if (tablink.length > 30) {
    tablink = tablink.slice(0, 30) + " ....";
  }
  $("#site").text(tablink + "\n\n");
});
