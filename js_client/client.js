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
        handleAuthData(data);
        getProducts();
    })
    .catch(err => {
        console.log('error', err)
    })
}

function handleAuthData(authData){
    localStorage.setItem("access", authData.access);
    localStorage.setItem("refresh", authData.refresh);
}

function getProducts(){
    const endpoint = `${baseEndpoint}/products/`;
    const method = "GET";
    options = getFetchOptions(method);
    fetch(endpoint, options)
    .then(response => response.json())
    .then(data =>{
        console.log(data);
        writeToDocument(data.results);
    }).catch(err => {
        console.log("error", err);
    });
}

function getFetchOptions(method){
    return {
        method: method,
        headers: {
            "Content-Type": "application/json",
            "Authorization": `Bearer ${localStorage.getItem("access")}`
        }
    }
}

function writeToDocument(Data){
    let productList = document.getElementById("productlist");
    console.log(typeof(Data));
    Data.forEach(element => {
        const datapoint = document.createElement("div");
        datapoint.innerHTML = `
        <p>${element.body}</p>
        <p>${element.price}</p>
        `;
        productList.appendChild(datapoint);
    });

}