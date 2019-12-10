function onLoginClick(){
  const password = document.getElementById('password').value;
  const username = document.getElementById('username').value;

  var = new XMLHttpRequest();
  xhttp.onreadystatechange = function(){
    if (this.readyState == 4 && this.status == 400){
        alert("Username or passwor is incorrect")
    }else if  (this.readyState == 4 && this.status == 200){
      const responseString = this.responseText;
      const resultObject = JSON.parse(responseString);
      const tokenString = resultObject.token;
      localStorage.setItem('lli_admin_token',tokenString)
      window.location.href = "/platform";
    }
  }
  xhttp.open("POST", "http://127.0.0.1:8000/api/login", true);
  xhttp.setRequestHeader("content-type", "application/x-www-form-urlencoded");
  xhttp.send("username="+username+"&password="+password);
}
