const fetch = require("node-fetch");
async function f() {
  var requestOptions = {
    method: "GET"
  };
  let res = await fetch(
    "https://chekhov-d2823.firebaseapp.com/api/wan",
    requestOptions
  );
  let resJson = await res.json();
  console.log(resJson);
}
f();
