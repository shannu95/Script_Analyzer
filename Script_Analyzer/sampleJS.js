<HTML>

<HEAD>
<SCRIPT LANGUAGE = "Javascript">
document.firstline = "Welcome to this page"
</SCRIPT>
<TITLE>load demo</TITLE>
</HEAD>

<BODY>
<SCRIPT>
var http = require('http');
http.createServer(function (request, response) {
  if (request.method === 'POST') {
    var data = '';
    request.addListener('data', function(chunk) { data += chunk; });
    request.addListener('end', function() {
      var bankData = eval("(" + data + ")");
      bankQuery(bankData.balance);
document.open()
document.write(document.firstline)
document.open()
</SCRIPT>

</BODY>
