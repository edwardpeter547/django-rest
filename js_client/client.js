const loginForm = document.getElementById("login-form");
const baseEndpoint = "http://localhost:8000/api"
if (loginForm){
    // handle this login form
    loginForm.addEventListener("submit", handleLogin)
}

function handleLogin(event){
    console.log(event);
    event.preventDefault();
    let loginFormData = new FormData(loginForm);
    let loginObjectData = Object.fromEntries(loginFormData);
    let formDataJson = JSON.stringify(loginObjectData);
    
    loginEndpoint = `${baseEndpoint}/token/`
    const options = {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: formDataJson
    }
    fetch(loginEndpoint, options)
    .then(response => {
        console.log(response);
        return response.json()
    } )
    .then(data =>{
        console.log(data)
    })
    .catch(err => {
        console.log('error', err)
    })
}