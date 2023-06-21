async function getInspirationalQuote(){
    let response = await axios.get("https://api.goprogram.ai/inspiration")

    let container = document.createElement("p")
    let h1 = document.createElement("h1")
    let h2 = document.createElement("h2")
    let h4 = document.createElement("h5")


    h1.textContent = `Quote of the day`
    h2.textContent = `"${response.data.quote}"`
    h4.textContent = `-${response.data.author}`

    container.appendChild(h1)
    container.appendChild(h2)
    container.appendChild(h4)
    document.body.appendChild(container)
}

getInspirationalQuote()