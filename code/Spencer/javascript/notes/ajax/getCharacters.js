async function getCharactersAxios(){
    let response = await axios.get("https://hp-api.onrender.com/api/characters")

    for(character of response.data){

        if(character.image === ""){
            continue
        }
        if(character.actor === ""){
            continue
        }

        let container = document.createElement("article")
        let h1 = document.createElement("h1")
        let h4 = document.createElement("h4")
        let img = document.createElement("img")

        h1.textContent = character.name
        h4.textContent = `Played by: ${character.actor}`
        img.src = character.image
        img.alt = character.name
        img.width = "200"
        
        container.appendChild(h1)
        container.appendChild(h4)
        container.appendChild(img)
        document.body.appendChild(container)
    }
}

getCharactersAxios()