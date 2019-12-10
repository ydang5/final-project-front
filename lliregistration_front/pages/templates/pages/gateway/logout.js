function onPageLoadRunPostLogoutFromApi(){

  localStorage.removeitem('indoor_air_token')
  window.location.href = "{% url 'login_page' %}";
}


onPageLoadRunPostLogoutFromApi()
