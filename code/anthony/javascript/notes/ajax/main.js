
// promise chaining with .then
let promise = fetch("https://hp-api.onrender.com/api/characters")

promise.then(function(response){
    return response.json()
}).then(function(data){
    // code goes here :)
    // console.log(data)
})

// async/await
async function getCharacters() {
    let response = await fetch("https://hp-api.onrender.com/api/characters")
    let data = await response.json()
    // code goes here :)
    console.log(data)
}
// getCharacters()


axios.get("https://hp-api.onrender.com/api/characters")
.then(function(response){
    // console.log(response)
})

async function getCharactersAxios(){
    let response = await axios.get("https://hp-api.onrender.com/api/characters")
    console.log(response)
}

// getCharactersAxios()