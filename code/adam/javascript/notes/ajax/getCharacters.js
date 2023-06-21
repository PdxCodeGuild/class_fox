

async function getCharactersAxios(){
    let response = await axios.get('https://hp-api.onrender.com/api/characters')
    
    for(character of response.data){

        // if(character.image === ""){
        //     continue
        // }
        // if(character.actor === ""){
        //     continue
        // }

        //  create elements
        let container = document.createElement("article")
        let h1 = document.createElement("h1")
        let img = document.createElement("img")
        let h4 = document.createElement("h4")
        
        
        // modify elements
        img.src = character.image
        h1.textContent = character.name
        h4.textContent = character.actor === "" ? "no actor": `Played By:${character.actor} `
        img.alt = character.name
        img.width = "200"
        
        
        // add elements to DOM
        container.appendChild(h1)
        container.append(h4)
        document.body.appendChild(container)
        container.appendChild(img)

        
    }
}
getCharactersAxios()