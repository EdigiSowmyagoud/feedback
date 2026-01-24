document.getElementById("form").addEventListener("submit", function(e) {
  e.preventDefault();

  const name = document.getElementById("name").value;
  const email = document.getElementById("email").value;
  const feedback = document.getElementById("feedback").value;

  fetch("http://EC2_PUBLIC_DNS_OR_ALB_DNS/submit", {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify({ name, email, feedback })
  })
  .then(res => res.json())
  .then(data => alert("Feedback submitted"))
  .catch(err => console.error(err));
});

