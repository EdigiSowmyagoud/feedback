document.getElementById("form").addEventListener("submit", function(e){
  e.preventDefault();

  fetch("http://LOAD_BALANCER_DNS/submit", {
    method: "POST",
    headers: {"Content-Type":"application/json"},
    body: JSON.stringify({
      name: name.value,
      email: email.value,
      feedback: feedback.value
    })
  }).then(() => alert("Submitted"));
});

