

async function getCharactersAxios(){
    let response = await axios.get("https://hp-api.onrender.com/api/characters")
    
    for(character of response.data){

        // if character has no image or actor go to next character
        // if(character.image === ""){
        //     continue
        // }
        // if(character.actor === ""){
        //     continue
        // }

        // Create elements
        let container = document.createElement("article")
        let h1 = document.createElement("h1")
        let h4 = document.createElement("h4")
        let img = document.createElement("img")

        // modify elements
        h1.textContent = character.name
        h4.textContent = character.actor === "" ? "no actor" : `Played by: ${character.actor}`
        img.src = character.image
        img.alt = character.name
        img.width = "200"

        // add elements to DOM
        container.appendChild(h1)
        container.appendChild(h4)
        container.appendChild(img)
        document.body.appendChild(container)
    }
}

getCharactersAxios()